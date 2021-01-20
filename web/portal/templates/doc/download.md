## How To Download Data

The [LSSTDESC Data Portal](https://lsstdesc-portal.nersc.gov/) allows anyone to transfer the DC2 Public Release data using Globus.

To get started click Login to authenticate into Globus using your organizational login or existing GlobusID. If needed, create a GlobusID using the "Sign Up" link.

If you want to download files to a local machine (e.g., your laptop), you will need to [set up Globus Personal Connect]({{url_for('render_doc', doc_name='globus_personal')}}) on your local machine first.

Once authenticated with Globus, users may transfer either whole directories or individual files by clicking on Transfer from the Home page.  You will be brought to a page like:

![Transfer](/static/img/transfer.png)

### Choosing the LSSTDESC Data Source

The LSSTDESC data is mirrored on two separate Globus endpoints, one at NERSC and the other at Argonne National Lab (ANL).  You may choose which endpoint you wish to use as your LSSTDESC data source.  Your currently chosen data source will be indicated on the Transfer page.  

If you wish to change which data source you use for your transfers, you can visit the [Profile page]({{url_for('profile')}}) and click on a data source and then click Save. All future data transfers will use your chosen LSSTDESC data source until you change it again on the Profile page.  

If you are satisfied with the chosen data source, you can proceed to download data.

![Profile](/static/img/profile.png)

### Download Data

If you wish to download whole directories, select the datasets to download and then click Transfer at the bottom of the page.

If you would prefer to download individual files, click on one of the Datasets and you will see a full listing of the dataset directory.

![File Selection](/static/img/fileselect.png)

Choose your files, and then click Transfer. You may optionally choose a predefined subset of the dataset by clicking the "Select Example Subset" button.  When finished choosing your files, click Transfer, and you will be taken to a Globus page where you will choose the destination for your download.

![Globus](/static/img/globus.png)

Click on Search in the Collection text box and choose a [Collection](https://docs.globus.org/how-to/get-started/#access_a_collection) as your desitination.  You may then select a path on that Collection, optionally create a label for this transfer and then click Submit.  If successful, a transfer submission window will appear:

![TransferStarted](/static/img/success.png)

You may monitor the transfer by clicking Refresh until the portal reports the transfer has successfully completed, or visit www.globus.org, login if necessary, and use the [Activity](https://docs.globus.org/how-to/get-started/#confirm_transfer_completion) tab.

