<!--- Do not delete this line, it is needed for jinja_markdown to render this page correctly -->
## Accessing the DC2 Simulated Sky Survey

If you use the DC2 Simulated Sky Survey in your work, we ask that you cite the following publications.

* [DESC DC2 Simulated Sky Survey Paper](https://ui.adsabs.harvard.edu/abs/2020arXiv201005926L/abstract)
* [DESC DC2 Data Release Note](https://arxiv.org/abs/2101.00000)

In addition, if you use `GCRCatalogs` to access the data, please also cite [Mao et al. (LSST DESC), ApJS, 234, 36 (2018)](https://ui.adsabs.harvard.edu/abs/2018ApJS..234...36M/abstract).

### Step 1: Download the catalog files

Follow [these instructions](download) to download dpdd object or truth match data files from the DC2 Simulated Sky Survey.
You can download the full data set or, if space is at a premium, a recommended subset of files.

### Step 2: Prepare `GCRCatalogs`

See [these instructions](install_gcr) to install and configure `GCRCatalogs`.

### Step 3: Verify access to the data

For the DC2 Object and Truth tables specifically, you can use the following code to print out the tracts that you have downloaded.

```python
import GCRCatalogs
print(GCRCatalogs.load_catalog('desc_dc2_run2.2i_dr6_object').available_tracts)
print(GCRCatalogs.load_catalog('desc_dc2_run2.2i_dr6_truth').available_tracts)
```

### Following the notebooks to access data

You can find examples of using `GCRCatalogs` in our [tutorial notebooks](https://github.com/LSSTDESC/desc-data-portal/tree/main/notebooks).

If you're planning to run the example notebooks and don't already have JupyterLab on your laptop, see [these instructions](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html).
