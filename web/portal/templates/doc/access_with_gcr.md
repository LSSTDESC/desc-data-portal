<!--- Do not delete this line, it is needed for jinja_markdown to render this page correctly -->
## Access Data Files with GCRCatalogs

### Setting up `root_dir` for GCRCatalogs

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

### Checking that everything is ready

You can use the following Python code to check if you have `GCRCatalogs` installed and `root_dir` correctly set.
The lower two lines should print out the tracts that you have downloaded for Object and Truth tables, respectively.

```python
import GCRCatalogs
print(GCRCatalogs.load_catalog('desc_dc2_run2.2i_dr6_object').available_tracts)
print(GCRCatalogs.load_catalog('desc_dc2_run2.2i_dr6_truth').available_tracts)
```

### Following the notebooks to access data

You can find examples of using `GCRCatalogs` in our [tutorial notebooks](https://github.com/LSSTDESC/DC2-Public-Release/tree/main/notebooks).

