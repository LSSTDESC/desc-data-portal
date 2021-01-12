<!--- Do not delete this line, it is needed for jinja_markdown to render this page correctly -->
## Access Data Files with GCRCatalogs

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

For the DC2 Object and Truth tables specifically, you can use the following code to print out the tracts
that you have downloaded.

```python
import GCRCatalogs
print(GCRCatalogs.load_catalog('desc_dc2_run2.2i_dr6_object').available_tracts)
print(GCRCatalogs.load_catalog('desc_dc2_run2.2i_dr6_truth').available_tracts)
```

### Following the notebooks to access data

You can find examples of using `GCRCatalogs` in our [tutorial notebooks](https://github.com/LSSTDESC/desc-data-portal/tree/main/notebooks).

If you're planning to run the example notebooks and don't already have JupyterLab on your laptop, see [these instructions](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html).
