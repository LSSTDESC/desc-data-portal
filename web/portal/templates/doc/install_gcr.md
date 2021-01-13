<!--- Do not delete this line, it is needed for jinja_markdown to render this page correctly -->
## Install and Configure `GCRCatalogs`

You can install [`GCRCatalogs`](https://github.com/LSSTDESC/gcr-catalogs) with [conda](https://docs.conda.io/) or [pip](https://pip.pypa.io/),
depending on your local Python environment.

### Install with conda

Before installation, you may want to create a new conda environment.
If you do,
[see instructions here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

`GCRCatalogs` is available on [conda-forge](https://conda-forge.org/).
To check if you are ready to obtain packages from conda-forge,
run the following command and see if "conda-forge" appears in the output.

```bash
conda config --show channels
```

If you do _not_ see "conda-forge", you can add it by running:

```bash
conda config --add channels conda-forge
conda config --set channel_priority strict
```

To install `GCRCatalogs` with conda, run

<!-- Remove "-c conda-forge/label/lsstdesc-gcr-catalogs_rc" from below when v1.2.0 is ready -->
```bash
conda install lsstdesc-gcr-catalogs -c conda-forge/label/lsstdesc-gcr-catalogs_rc
```

### Install with pip

Before installation, you may want to create a new virtual environment.
If you do,
[see instructions here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment).

Before installing `GCRCatalogs` with pip, you may want to first install `wheel`.
This will allow pip to fetch pre-built binary files. To install `wheel`, run

```bash
pip install wheel  # optional
```

To install `GCRCatalogs` with pip, run

<!-- Change "v1.2.0rc2" to "v1.2.0" below when v1.2.0 is ready -->
```bash
pip install https://github.com/LSSTDESC/gcr-catalogs/archive/v1.2.0rc2.tar.gz#egg=GCRCatalogs[full]
```

### Configure: Setting up `root_dir` for GCRCatalogs

After you [downloaded the data files]({{url_for('render_doc', doc_name='download')}}) and [installed `GCRCatalogs`]({{url_for('render_doc', doc_name='install_gcr')}}),
you need to tell `GCRCatalogs` where these downloaded files sit on your machine.

When you used Globus transfer, if you downloaded the files to `/path/to/the/download/directory`, then run in a terminal

```bash
python -m GCRCatalogs.user_config set root_dir /path/to/the/download/directory
```

Here `/path/to/the/download/directory` should contain the `lsstdesc-public` folder that Globus transfer creates.
If you have moved it, you should change `/path/to/the/download/directory` to the directory that contains the `lsstdesc-public` folder.
Do not change the directory structure within `lsstdesc-public`.

You only need to set this once.
