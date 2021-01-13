<!--- Do not delete this line, it is needed for jinja_markdown to render this page correctly -->

## Accessing cosmoDC2

If you use cosmoDC2 in your work, please cite [Korytov et al. (LSST DESC), ApJS, 245, 26 (2019)](https://ui.adsabs.harvard.edu/abs/2019ApJS..245...26K/abstract). In addition, if you use `GCRCatalogs` as described here to access cosmoDC2, please also cite [Mao et al. (LSST DESC), ApJS, 234, 36 (2018)](https://ui.adsabs.harvard.edu/abs/2018ApJS..234...36M/abstract).


### Step 1: Download cosmoDC2 catalog files

Follow [these instructions](download) to download "CosmoDC2 v1.1.4" data files.
You can download the full data set or, if space is at a premium, a recommended subset of files.
Note that the full catalog is partitioned into sky areas by healpixels and also by redshift ranges.


### Step 2: Prepare `GCRCatalogs`

See [these instructions](install_gcr) to install and configure `GCRCatalogs`.

### Step 3: Load cosmoDC2 with GCRCatalogs

```python
import GCRCatalogs
cat = GCRCatalogs.load_catalog("desc_cosmodc2")
```

### Step 4: Get familiar with GCRCatalogs and cosmoDC2

There are many tutorial notebooks showing you how to use GCRCatalogs and how to play with the cosmoDC2 data.
Note that if you see the tutorial notebooks load `cosmoDC2_v1.1.4_small` or `cosmoDC2_v1.1.4_image`,
you will need to change the catalog name to `desc_cosmodc2`.

Note that in some tutorials you may see instructions of loading other catalogs with `GCRCatalogs`. Those instructions will *not* work on your local machine. You will only be able to access public DESC catalogs that you have downloaded to your machine.

- [Basic usage of `GCRCatalogs`](https://nbviewer.jupyter.org/github/LSSTDESC/gcr-catalogs/blob/master/examples/GCRCatalogs%20Demo.ipynb)
- [Tutorial: Redshift distributions](https://nbviewer.jupyter.org/github/LSSTDESC/DC2-analysis/blob/rendered/tutorials/extragalactic_gcr_redshift_dist.nbconvert.ipynb)
- [Tutorial: Halo Occupation Distribution](https://nbviewer.jupyter.org/github/LSSTDESC/DC2-analysis/blob/rendered/tutorials/extragalactic_gcr_hod.nbconvert.ipynb)
- [Tutorial: mass relations](https://nbviewer.jupyter.org/github/LSSTDESC/DC2-analysis/blob/rendered/tutorials/extragalactic_gcr_mass_relations.nbconvert.ipynb)
- [Tutorial: cluster colors](https://nbviewer.jupyter.org/github/LSSTDESC/DC2-analysis/blob/rendered/tutorials/extragalactic_gcr_cluster_colors.nbconvert.ipynb)
- [Tutorial: cluster members](https://nbviewer.jupyter.org/github/LSSTDESC/DC2-analysis/blob/rendered/tutorials/extragalactic_gcr_cluster_members.nbconvert.ipynb)
