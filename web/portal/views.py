import requests
import os
from flask import (abort, flash, redirect, render_template, request, session,
                   url_for)
from globus_sdk import (RefreshTokenAuthorizer, TransferAPIError,
                        TransferClient, TransferData)

from portal import app, database, datasets
from portal.decorators import authenticated
from portal.utils import (get_portal_tokens, get_safe_redirect,
                          load_portal_client)

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


@app.route('/', methods=['GET'])
def home():
    if 'source_endpoint' not in session:
        session['source_endpoint'] = 1
    return render_template('home.jinja2')

@app.route('/.well-known/acme-challenge/<letsencrypturl>')
def letsenc(letsencrypturl):
    return app.config["LETSENCRYPT_SECRET"]

@app.route('/doc/<doc_name>')
def render_doc(doc_name):
    return render_template('doc_template.jinja2', doc_name=doc_name)

@app.route('/signup', methods=['GET'])
def signup():
    """Send the user to Globus Auth with signup=1."""
    return redirect(url_for('authcallback', signup=1))


@app.route('/login', methods=['GET'])
def login():
    """Send the user to Globus Auth."""
    return redirect(url_for('authcallback'))


@app.route('/logout', methods=['GET'])
@authenticated
def logout():
    """
    - Revoke the tokens with Globus Auth.
    - Destroy the session state.
    - Redirect the user to the Globus Auth logout page.
    """
    client = load_portal_client()

    # Revoke the tokens with Globus Auth
    for token, token_type in (
            (token_info[ty], ty)
            # get all of the token info dicts
            for token_info in session['tokens'].values()
            # cross product with the set of token types
            for ty in ('access_token', 'refresh_token')
            # only where the relevant token is actually present
            if token_info[ty] is not None):
        client.oauth2_revoke_token(
            token, additional_params={'token_type_hint': token_type})

    # Destroy the session state
    session.clear()

    redirect_uri = url_for('home', _external=True)

    ga_logout_url = []
    ga_logout_url.append(app.config['GLOBUS_AUTH_LOGOUT_URI'])
    ga_logout_url.append('?client={}'.format(app.config['PORTAL_CLIENT_ID']))
    ga_logout_url.append('&redirect_uri={}'.format(redirect_uri))
    ga_logout_url.append('&redirect_name=LSSTDESC Data Portal')

    # Redirect the user to the Globus Auth logout page
    return redirect(''.join(ga_logout_url))


@app.route('/profile', methods=['GET', 'POST'])
@authenticated
def profile():
    """User profile information. Assocated with a Globus Auth identity."""
    if request.method == 'GET':
        identity_id = session.get('primary_identity')
        profile = database.load_profile(identity_id)

        if profile:
            name, email, institution, source_endpoint = profile

            session['name'] = name
            session['email'] = email
            session['institution'] = institution
            session['source_endpoint'] = source_endpoint
        else:
            flash(
                'Please complete any missing profile fields and press Save.')

        if request.args.get('next'):
            session['next'] = get_safe_redirect()

        return render_template('profile.jinja2')
    elif request.method == 'POST':
        print("inside profile post")
        name = session['name'] = request.form['name']
        email = session['email'] = request.form['email']
        institution = session['institution'] = request.form['institution']
        source_endpoint = session['source_endpoint'] = 0 # int(request.form['endpoint'])

        database.save_profile(identity_id=session['primary_identity'],
                              name=name,
                              email=email,
                              institution=institution,
                              source_endpoint=source_endpoint)

        flash('Thank you! Your profile has been successfully updated.')

        if 'next' in session:
            redirect_to = session['next']
            session.pop('next')
        else:
            redirect_to = url_for('profile')

        return redirect(redirect_to)


@app.route('/authcallback', methods=['GET'])
def authcallback():
    """Handles the interaction with Globus Auth."""
    # If we're coming back from Globus Auth in an error state, the error
    # will be in the "error" query string parameter.
    if 'error' in request.args:
        flash("You could not be logged into the portal: " +
              request.args.get('error_description', request.args['error']))
        return redirect(url_for('home'))

    # Set up our Globus Auth/OAuth2 state
    # AUTHCALLBACK_SCHEME="https" allows portal to run behind SSL-terminating
    # reverse proxy or ingress.
    redirect_uri = url_for(
        'authcallback',
        _external=True,
        _scheme=app.config.get("AUTHCALLBACK_SCHEME")
    )

    client = load_portal_client()
    client.oauth2_start_flow(
        redirect_uri,
        refresh_tokens=True,
        requested_scopes=app.config['USER_SCOPES']
    )

    # If there's no "code" query string parameter, we're in this route
    # starting a Globus Auth login flow.
    if 'code' not in request.args:
        additional_authorize_params = (
            {'signup': 1} if request.args.get('signup') else {})

        auth_uri = client.oauth2_get_authorize_url(
            additional_params=additional_authorize_params)

        return redirect(auth_uri)
    else:
        # If we do have a "code" param, we're coming back from Globus Auth
        # and can start the process of exchanging an auth code for a token.
        code = request.args.get('code')
        tokens = client.oauth2_exchange_code_for_tokens(code)

        id_token = tokens.decode_id_token(client)
        session.update(
            tokens=tokens.by_resource_server,
            is_authenticated=True,
            name=id_token.get('name', ''),
            email=id_token.get('email', ''),
            institution=id_token.get('organization', ''),
            primary_username=id_token.get('preferred_username'),
            primary_identity=id_token.get('sub'),
        )

        profile = database.load_profile(session['primary_identity'])

        if profile:
            name, email, institution, source_endpoint = profile

            session['name'] = name
            session['email'] = email
            session['institution'] = institution
            session['source_endpoint'] = source_endpoint
        else:
            return redirect(url_for('profile',
                            next=url_for('transfer')))

        return redirect(url_for('transfer'))


@app.route('/browse', methods=['GET', 'POST'])
@app.route('/browse/dataset/<dataset_id>', methods=['GET', 'POST'])
@app.route('/browse/endpoint/<endpoint_id>/<path:endpoint_path>',
           methods=['GET', 'POST'])
@authenticated
def browse(dataset_id=None, endpoint_id=None, endpoint_path=None):
    """
    - Get list of files for the selected dataset or endpoint ID/path
    - Return a list of files to a browse view

    The target template (browse.jinja2) expects an `endpoint_uri` (if
    available for the endpoint), `target` (either `"dataset"`
    or `"endpoint"`), and 'file_list' (list of dictionaries) containing
    the following information about each file in the result:

    {'name': 'file name', 'size': 'file size', 'id': 'file uri/path'}

    If you want to display additional information about each file, you
    must add those keys to the dictionary and modify the browse.jinja2
    template accordingly.
    """

    if request.method == 'GET':
        assert bool(dataset_id) != bool(endpoint_id and endpoint_path)

        if dataset_id:
            try:
                dataset = next(ds for ds in datasets if ds['id'] == dataset_id)
            except StopIteration:
                abort(404)

            endpoint_id = app.config['NERSC_ENDPOINT_ID'] if session['source_endpoint'] else app.config['ANL_ENDPOINT_ID']
            endpoint_path = (app.config['NERSC_ENDPOINT_BASE'] + dataset['path']) if session['source_endpoint'] else (app.config['ANL_ENDPOINT_BASE'] + dataset['path'])
  #          endpoint_id = app.config['DATASET_ENDPOINT_ID'] 
  #          endpoint_path = app.config['DATASET_ENDPOINT_BASE'] + dataset['path']

        else:
            endpoint_path = '/' + endpoint_path

        transfer_tokens = session['tokens']['transfer.api.globus.org']

        authorizer = RefreshTokenAuthorizer(
            transfer_tokens['refresh_token'],
            load_portal_client(),
            access_token=transfer_tokens['access_token'],
            expires_at=transfer_tokens['expires_at_seconds'])

        transfer = TransferClient(authorizer=authorizer)

        try:
            transfer.endpoint_autoactivate(endpoint_id)
            listing = transfer.operation_ls(endpoint_id, path=endpoint_path)
        except TransferAPIError as err:
            flash('Error [{}]: {}'.format(err.code, err.message))
            return redirect(url_for('browse'))

        file_list = [e for e in listing if e['type'] == 'file']
        if dataset_id and 'example' in dataset:
            for e in file_list:
                e['is_example_set'] = (e['name'] in dataset['example'])

        ep = transfer.get_endpoint(endpoint_id)

        https_server = ep['https_server']
        endpoint_uri = https_server + endpoint_path if https_server else None
        webapp_xfer = 'https://app.globus.org/file-manager?' + \
            urlencode(dict(origin_id=endpoint_id, origin_path=endpoint_path))

        return render_template('browse.jinja2', endpoint_uri=endpoint_uri,
                           target="dataset" if dataset_id else "endpoint",
                           description=(dataset['name'] if dataset_id
                                        else ep['display_name']),
                           mypath=(dataset['path'] if dataset_id
                                        else None),
                           myid=(dataset['id'] if dataset_id
                                        else None),
                           has_example_set=(dataset_id and 'example' in dataset),
                           doc_name=(dataset.get("doc_name") if dataset_id else None),
                           file_list=file_list, webapp_xfer=webapp_xfer)

    if request.method == 'POST':
        if not request.form.get('file'):
            flash('Please select at least one file.')
            return redirect(url_for('browse', dataset_id=dataset_id))

        params = {
            'method': 'POST',
            'action': url_for('submit_transfer', _external=True,
                              _scheme='https'),
            'filelimit': 0,
            'folderlimit': 1
        }

        browse_endpoint = 'https://app.globus.org/file-manager?{}' \
            .format(urlencode(params))

        session['form'] = {
            'dirselect': False,
            'datasets': request.form.getlist('file'),
            'path': request.form.getlist('path'),
            'id': request.form.getlist('id')
        }

        return redirect(browse_endpoint)


@app.route('/transfer', methods=['GET', 'POST'])
@authenticated
def transfer():
    """
    - Save the submitted form to the session.
    - Send to Globus to select a destination endpoint using the
      Browse Endpoint helper page.
    """
    if request.method == 'GET':
        return render_template('transfer.jinja2', datasets=datasets)

    if request.method == 'POST':
        if not request.form.get('dataset'):
            flash('Please select at least one dataset.')
            return redirect(url_for('transfer'))

        params = {
            'method': 'POST',
            'action': url_for('submit_transfer', _external=True,
                              _scheme='https'),
            'filelimit': 0,
            'folderlimit': 1
        }

        browse_endpoint = 'https://app.globus.org/file-manager?{}' \
            .format(urlencode(params))

        session['form'] = {
            'dirselect': True,
            'datasets': request.form.getlist('dataset')
        }

        return redirect(browse_endpoint)


@app.route('/submit-transfer', methods=['POST'])
@authenticated
def submit_transfer():
    """
    - Take the data returned by the Browse Endpoint helper page
      and make a Globus transfer request.
    - Send the user to the transfer status page with the task id
      from the transfer.
    """
    browse_endpoint_form = request.form

    dirselect = session['form']['dirselect']
    selected = session['form']['datasets']
    if dirselect:
        filtered_datasets = [ds for ds in datasets if ds['id'] in selected]
    else:
        path = session['form']['path']
        myid = session['form']['id']
        filtered_datasets = [{'name':name, 'path': path, 'id': myid}
              for name, path, myid in zip(selected, path, myid)
              ]

    transfer_tokens = session['tokens']['transfer.api.globus.org']

    authorizer = RefreshTokenAuthorizer(
        transfer_tokens['refresh_token'],
        load_portal_client(),
        access_token=transfer_tokens['access_token'],
        expires_at=transfer_tokens['expires_at_seconds'])

    transfer = TransferClient(authorizer=authorizer)

    #source_endpoint_id = app.config['DATASET_ENDPOINT_ID']
    #source_endpoint_base = app.config['DATASET_ENDPOINT_BASE']
    source_endpoint_id = app.config['NERSC_ENDPOINT_ID'] if session['source_endpoint'] else app.config['ANL_ENDPOINT_ID']
    source_endpoint_base =  app.config['NERSC_ENDPOINT_BASE'] if session['source_endpoint'] else app.config['ANL_ENDPOINT_BASE']
    destination_endpoint_id = browse_endpoint_form['endpoint_id']
    destination_folder = browse_endpoint_form.get('folder[0]')

    transfer_data = TransferData(transfer_client=transfer,
                                 source_endpoint=source_endpoint_id,
                                 destination_endpoint=destination_endpoint_id,
                                 label=browse_endpoint_form.get('label'))

    for ds in filtered_datasets:
        print("printing ds")
        print(ds)
        if dirselect:
            source_path = source_endpoint_base + ds['path']
        else:
            source_path = source_endpoint_base + ds['path'] + "/" + ds['name']

        dest_path = browse_endpoint_form['path']

        if destination_folder:
            dest_path += destination_folder + '/'

        if dirselect:
            dest_path +=  ds['path'] + '/'
        else:
            dest_path += ds['path'] + '/' + ds['name']

        transfer_data.add_item(source_path=source_path,
                               destination_path=dest_path,
                               recursive=dirselect)

    transfer.endpoint_autoactivate(source_endpoint_id)
    transfer.endpoint_autoactivate(destination_endpoint_id)
    task_id = transfer.submit_transfer(transfer_data)['task_id']

    flash('Transfer request submitted successfully. Task ID: ' + task_id)

    return(redirect(url_for('transfer_status', task_id=task_id)))


@app.route('/status/<task_id>', methods=['GET'])
@authenticated
def transfer_status(task_id):
    """
    Call Globus to get status/details of transfer with
    task_id.

    The target template (tranfer_status.jinja2) expects a Transfer API
    'task' object.

    'task_id' is passed to the route in the URL as 'task_id'.
    """
    transfer_tokens = session['tokens']['transfer.api.globus.org']

    authorizer = RefreshTokenAuthorizer(
        transfer_tokens['refresh_token'],
        load_portal_client(),
        access_token=transfer_tokens['access_token'],
        expires_at=transfer_tokens['expires_at_seconds'])

    transfer = TransferClient(authorizer=authorizer)
    task = transfer.get_task(task_id)

    return render_template('transfer_status.jinja2', task=task)

