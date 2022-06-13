## Install and Configure `GCRCatalogs`

You can install [`GCRCatalogs`](https://github.com/LSSTDESC/gcr-catalogs) with [conda](https://docs.conda.io/) or [pip](https://pip.pypa.io/),
depending on your local Python environment.

### Install with conda

#### Preliminaries

Before installation, you may want to create a new conda environment.
If you do,
[see instructions here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

`GCRCatalogs` is available on [conda-forge](https://conda-forge.org/), not on conda's "defaults" channel.
If you are using the "defaults" channel (for example, if you haven't heard of conda-forge),
you can still install `GCRCatalogs` directly using the instruction below.
However, please consider switching to the conda-forge channel;
see [instructions](https://conda-forge.org/docs/user/introduction.html#how-can-i-install-packages-from-conda-forge)
and [why](https://conda-forge.org/docs/user/tipsandtricks.html#using-multiple-channels).

*NOTE:* In order to access the latest catalogs (as of June 2022) you need `GCRCatalogs`
version v1.4.0 or later. When using either of the install methods described below you will get a suitable released version. If you have already installed `GCRCatalogs` for an earlier
data release, you can update instead.

#### Install

To install `GCRCatalogs` with conda, run

```bash
conda install -c conda-forge lsstdesc-gcr-catalogs
```

#### Update

To update with conda, run

```bash
conda update -c conda-forge lsstdesc-gcr-catalogs
```

### Install with pip

#### Preliminaries

Before installation, you may want to create a new virtual environment.
If you do,
[see instructions here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment).

You may want to first install `wheel`,
which will allow pip to fetch pre-built binary files.
To install `wheel`, run

```bash
pip install wheel  # optional
```

#### Install

To install `GCRCatalogs` with pip, run

```bash
pip install https://github.com/LSSTDESC/gcr-catalogs/archive/v1.4.0.tar.gz#egg=GCRCatalogs[full]
```

#### Update

To update with pip, use the `--upgrade` option:

```bash
pip install --upgrade https://github.com/LSSTDESC/gcr-catalogs/archive/v1.4.0.tar.gz#egg=GCRCatalogs[full]
```

### Configure: Setting up `root_dir` for GCRCatalogs

After you [download the data files]({{url_for('render_doc', doc_name='download')}}) and [install `GCRCatalogs`]({{url_for('render_doc', doc_name='install_gcr')}}),
you need to tell `GCRCatalogs` where these downloaded files sit on your machine.

When you used Globus transfer, if you downloaded the files to `/path/to/the/download/directory`, then run in a terminal

```bash
python -m GCRCatalogs.user_config set root_dir /path/to/the/download/directory
```

Here `/path/to/the/download/directory` should contain the `lsstdesc-public` folder that Globus transfer creates.
If you have moved it, you should change `/path/to/the/download/directory` to the directory that contains the `lsstdesc-public` folder.
Do not change the directory structure within `lsstdesc-public`.

You only need to set this once.

### Checking that everything is ready

You can use the following Python code to check if you have `GCRCatalogs` installed and `root_dir` correctly set.

```python
import GCRCatalogs
GCRCatalogs.get_root_dir()
```

To see the list of public catalogs that may be available to you, run:

```python
GCRCatalogs.get_public_catalog_names()
```

Note that the above function returns the list of public catalogs that DESC has published,
but it does not check if those catalog files exist on your machine.
You will need to download them manually following [these instructions](download).

To confirm that GCRCatalogs has access to the files you've downloaded see the specific instructions for either [cosmoDC2](cosmodc2) or the [DC2 Simulated Sky Survey](dc2_sim_sky_survey).
