## CosmoDC2

CosmoDC2 is a large synthetic galaxy catalog designed to support precision dark energy science with LSST,
covering 440 sq. deg. of sky area to a redshift of z = 3, with a magnitude depth of 28 in the r band.
A wide range of galaxy properties are available in cosmoDC2.
To learn more about cosmoDC2, please see

- [Korytov et al. (LSST DESC), ApJS, 245, 26 (2019)](https://ui.adsabs.harvard.edu/abs/2019ApJS..245...26K/abstract).

Follow the steps below to access cosmoDC2.
If you use cosmoDC2 in your work, we ask that you cite the publication above.

### Step 1: Download cosmoDC2 catalog files

Follow [these instructions](download) to download "CosmoDC2 v1.1.4" data files.
You can download the full data set or, if space is at a premium, a recommended subset of files.
The data files you downloaded are in HDF5 format, partitioned into sky areas (by healpixels) and redshift ranges.
The data schema can be found [here](
https://github.com/LSSTDESC/gcr-catalogs/blob/master/GCRCatalogs/SCHEMA.md#extragalactic-catalogs).

While you can access these files by standard tools, we recommend that you use `GCRCatalogs` to access the catalog
because some quantities described in the [cosmoDC2 schema](
https://github.com/LSSTDESC/gcr-catalogs/blob/master/GCRCatalogs/SCHEMA.md#extragalactic-catalogs)
are only available when you access with `GCRCatalogs`, but not in the raw files.

### Step 2: Prepare `GCRCatalogs`

See [these instructions](install_gcr) to install and configure `GCRCatalogs`.

If you use `GCRCatalogs` as described here to access cosmoDC2, please also cite
[Mao et al. (LSST DESC), ApJS, 234, 36 (2018)](https://ui.adsabs.harvard.edu/abs/2018ApJS..234...36M/abstract).

### Step 3: Load cosmoDC2 with GCRCatalogs

```python
import GCRCatalogs
cat = GCRCatalogs.load_catalog("desc_cosmodc2")
```

### Step 4: Get familiar with GCRCatalogs and cosmoDC2

There are many tutorial notebooks showing you how to use GCRCatalogs and how to play with the cosmoDC2 data.
Note that if you see the tutorial notebooks load `cosmoDC2_v1.1.4_small` or `cosmoDC2_v1.1.4_image`,
you will need to change the catalog name to `desc_cosmodc2`.

Note that in some tutorials you may see instructions for loading other catalogs with `GCRCatalogs`. Those instructions will *not* work on your local machine. You will only be able to access public DESC catalogs that you have downloaded to your machine.

- [Basic usage of `GCRCatalogs`](https://nbviewer.jupyter.org/github/LSSTDESC/gcr-catalogs/blob/master/examples/GCRCatalogs%20Demo.ipynb)
- [Tutorial: Redshift distributions](https://nbviewer.jupyter.org/github/LSSTDESC/DC2-analysis/blob/rendered/tutorials/extragalactic_gcr_redshift_dist.nbconvert.ipynb)
- [Tutorial: Halo Occupation Distribution](https://nbviewer.jupyter.org/github/LSSTDESC/DC2-analysis/blob/rendered/tutorials/extragalactic_gcr_hod.nbconvert.ipynb)
- [Tutorial: mass relations](https://nbviewer.jupyter.org/github/LSSTDESC/DC2-analysis/blob/rendered/tutorials/extragalactic_gcr_mass_relations.nbconvert.ipynb)
- [Tutorial: cluster colors](https://nbviewer.jupyter.org/github/LSSTDESC/DC2-analysis/blob/rendered/tutorials/extragalactic_gcr_cluster_colors.nbconvert.ipynb)
- [Tutorial: cluster members](https://nbviewer.jupyter.org/github/LSSTDESC/DC2-analysis/blob/rendered/tutorials/extragalactic_gcr_cluster_members.nbconvert.ipynb)
