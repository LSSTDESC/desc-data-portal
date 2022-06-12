## DC2 Simulated Sky Survey

_Updated June 15, 2022: The most up-to-date version for the public DC2 data sets is `v4`. Previous versions have been deprecated._

The DC2 Simulated Sky Survey is a 300-sq-deq simulated survey
in six optical bands with observations following a reference LSST observing cadence.

To learn more about the DC2 Simulated Sky Survey, you can read:

* [DESC DC2 Simulated Sky Survey Paper](https://ui.adsabs.harvard.edu/abs/2020arXiv201005926L/abstract):
  a comprehensive description about the DC2 Simulated Sky Survey, including design choices and production details.
* [DESC DC2 Data Release Note](https://arxiv.org/abs/2101.04855):
  a brief note about the released dataset, including data file format, data partition scheme, and schema tables.

Two kinds of datasets are provided: [Tables](#tables) (including object and truth tables) and [intermediate data products](#intermediate-data-products).
Follow the instructions below for the data sets you wish to download.

If you use the DC2 Simulated Sky Survey in your work, we ask that you cite both publications above.

### Tables

#### Step 1: Download the Table files

Follow [these instructions](download) to download "Object DPDD", "Truth Match", and/or "Unmerged Truth" data files
from the DC2 Simulated Sky Survey.
You can find the description and table schema of these data sets in the [Data Release Note](https://arxiv.org/abs/2101.04855).
You can download the full data set or, if space is at a premium, a recommended subset of files.

For "Object DPDD" and "Truth Match" data sets, the files are in Parquet format and are partitioned into sky regions called "tracts"
(see Sec. 4.1 of the [Release Note](https://arxiv.org/abs/2101.04855) for details).

For "Unmerged Truth Star" and "Unmerged Truth SN" data sets, you can choose to download in Parquet format or in SQLite.
The latter is larger in size but have better running performance if you are matching across tables.

For "Unmerged Truth Galaxy", the files are in Parquet format and are partitioned into healpixels.

You can access all Parquet files by any standard tools that read Parquet format.
We additionally provide a high-level Python package `GCRCatalogs` to facilitate easy access (see below).
Note that on some very old (e.g., older than 10 years) machines, reading Parquet files may be difficult.
If that is a problem for you, please [let us know](https://github.com/LSSTDESC/desc-data-portal/discussions).

#### Step 2: Prepare `GCRCatalogs`

See [these instructions](install_gcr) to install and configure `GCRCatalogs`.

If you use `GCRCatalogs` to access the data, please also cite
[Mao et al. (LSST DESC), ApJS, 234, 36 (2018)](https://ui.adsabs.harvard.edu/abs/2018ApJS..234...36M/abstract).

#### Step 3: Verify access to the data

For the DC2 Object and Truth tables specifically, you can use the following code to print out the tracts that you have downloaded.

```python
import GCRCatalogs
print(GCRCatalogs.load_catalog('desc_dc2_run2.2i_dr6_object').available_tracts)
print(GCRCatalogs.load_catalog('desc_dc2_run2.2i_dr6_truth').available_tracts)
```

#### Step 4: Follow the notebooks to access data

You can find examples of using `GCRCatalogs` in our [tutorial notebooks](https://github.com/LSSTDESC/desc-data-portal/tree/main/notebooks).

If you're planning to run the example notebooks and don't already have JupyterLab on your laptop, see [these instructions](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html).

## Intermediate data products

We provide a subset of intermediate data products from the LSST Science Pipelines, including raw images, calibrated exposures, and coadded images.
Unlike the Table datasets, it is not possible to choose a even smaller subset of the intermediate data products that we provided.
For a detailed description of these data products and associated files included, please see Section 3.4 of the [Data Release Note](https://arxiv.org/abs/2101.04855).
To see how these intermediate data products are organized, please see Appendix C of the [Data Release Note](https://arxiv.org/abs/2101.04855).
