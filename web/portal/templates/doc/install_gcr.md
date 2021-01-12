<!--- Do not delete this line, it is needed for jinja_markdown to render this page correctly -->
# Install GCRCatalogs

You can install [`GCRCatalogs`](https://github.com/LSSTDESC/gcr-catalogs) with [conda](https://docs.conda.io/) or [pip](https://pip.pypa.io/),
depending on your local Python environment.

### Install with conda

You may want to create a new conda environment before installation.
If you do, [see instructions here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

To install, simply run

```bash
conda install lsstdesc-gcr-catalogs -c conda-forge/label/lsstdesc-gcr-catalogs_rc
```

### Install with pip

You may want to create a virtual environment before installation.
If you do, [see instructions here](https://docs.python.org/3/library/venv.html).

To install, simply run

```bash
pip install https://github.com/LSSTDESC/gcr-catalogs/archive/v1.2.0rc2.tar.gz#egg=GCRCatalogs[full]
```

## Install JupyterLab (optional)

If you're planning to run the example notebooks and don't already have JupyterLab on your laptop, see [these instructions](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html).

