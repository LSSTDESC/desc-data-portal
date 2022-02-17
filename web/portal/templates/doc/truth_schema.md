## Additional Truth Tables and Their Schemas

| Object type | Table name                | SQLite basename               | Parquet basename                      |
| ----------- | ------------------------- | ----------------------------- | ------------------------------------- |
| Star        | truth_summary             | star_truth_summary_trimmed.db | star_truth_summary_trimmed.parquet    |
| Star        | stellar_variability_truth | star_variability_truth.db     | star_variability_truth_int_id.parquet |
| Star        | stellar_variability_stats | star_lc_stats_trimmed.db      | star_lc_stats_trimmed.parquet         |
| SN          | truth_summary             | sum-variabile-31mar.db        | sn_truth_summary.parquet              |
| SN          | sn_variability_truth      | sum-variabile-31mar.db        | sn_variability_truth.parquet          |
| SN          | sne_params                | sne_cosmoDC2_v1.1.4_MS_DDF.db | N/A



### Star truth_summary

| Column         | Type (SQLite) | Type (parquet) | Description/Comments
| -------------- | ------------- | -------------- | -------------------------------------------------------------
| id             | TEXT          | String         | id for the star. Though nominally a string, convertible to int
| host_galaxy    | BIGINT        | int64          | id of host galaxy
| ra             | DOUBLE        | double         | right ascension
| dec            | DOUBLE        | double         | declination
| redshift       | FLOAT         | float          | redshift
| is_variable    | INT           | int32          | True if variable, even if variation is small. Most are variable
| is_pointsource | INT           | int32          | Always true for stars
| flux_u         | DOUBLE        | float          | flux in u-band
| flux_g         | DOUBLE        | float          | flux in g-band
| flux_r         | DOUBLE        | float          | flux in r-band
| flux_i         | DOUBLE        | float          | flux in i-band
| flux_z         | DOUBLE        | float          | flux in z-band
| flux_y         | DOUBLE        | float          | flux in y-band
| flux_u_noMW    | DOUBLE        | float          | flux in u-band ignoring Milky Way extinction
| flux_g_noMW    | DOUBLE        | float          | flux in g-band ignoring Milky Way extinction
| flux_r_noMW    | DOUBLE        | float          | flux in r-band ignoring Milky Way extinction
| flux_i_noMW    | DOUBLE        | float          | flux in i-band ignoring Milky Way extinction
| flux_z_noMW    | DOUBLE        | float          | flux in z-band ignoring Milky Way extinction
| flux_y_noMW    | DOUBLE        | float          | flux in y-band ignoring Milky Way extinction

### stellar_variability_truth

| Column         | Type (SQLite) | Type (parquet) | Description/Comments
| -------------- | ------------- | -------------- |---------------------------------------------------------------
| id             | TEXT          | int64          | id stored here as int in parquet for efficient queries
| obsHistID      | INT           | int32          | identifies observation (visit)
| MJD            | DOUBLE        | double         | modified Julian date of observation
| bandpass       | TEXT          | String         | bandpass used for this observation
| delta_flux     | DOUBLE        | float          | delta from mean flux for this bandpass (see stats table below)

### stellar_lc_stats

| Column         | Type (SQLite) | Type (parquet) | Description/Comments
| -------------- | ------------- | -------------- | --------------------
| id             | TEXT          | String         | id for star
| model          | TEXT          | String         | variability model, e.g. "MLT"
| mean_u         | DOUBLE        | float          | mean flux in u-band
| mean_g         | DOUBLE        | float          | mean flux in g-band
| mean_r         | DOUBLE        | float          | mean flux in r-band
| mean_i         | DOUBLE        | float          | mean flux in i-band
| mean_z         | DOUBLE        | float          | mean flux in z-band
| mean_y         | DOUBLE        | float          | mean flux in y-band
| stdev_u        | DOUBLE        | float          | std dev of flux in u-band
| stdev_g        | DOUBLE        | float          | std dev of flux in g-band
| stdev_r        | DOUBLE        | float          | std dev of flux in r-band
| stdev_i        | DOUBLE        | float          | std dev of flux in i-band
| stdev_z        | DOUBLE        | float          | std dev of flux in z-band
| stdev_y        | DOUBLE        | float          | std dev of flux in y-band

### SN truth_summary

For description of columns see star truth_summary above. The only difference is for SN id must
be a string; values are generally not convertible to integers.

| Column         | Type (SQLite) | Type (parquet)
| -------------- | ------------- | --------------
| id             | TEXT          | String
| host_galaxy    | BIGINT        | int64
| ra             | DOUBLE        | double
| dec            | DOUBLE        | double
| redshift       | DOUBLE        | float
| is_variable    | INT           | int32
| is_pointsource | INT           | int32
| flux_u         | DOUBLE        | float
| flux_g         | DOUBLE        | float
| flux_r         | DOUBLE        | float
| flux_i         | DOUBLE        | float
| flux_z         | DOUBLE        | float
| flux_y         | DOUBLE        | float
| flux_u_noMW    | DOUBLE        | float
| flux_g_noMW    | DOUBLE        | float
| flux_r_noMW    | DOUBLE        | float
| flux_i_noMW    | DOUBLE        | float
| flux_z_noMW    | DOUBLE        | float
| flux_y_noMW    | DOUBLE        | float

## sn_variability_truth

| Column         | Type (SQLite) | Type (parquet) | Description/Comments
| -------------- | ------------- | -------------- | --------------------------------------------------------------
| id             | TEXT          | String         | id of object
| obsHistID      | INT           | int32          | identifies observation (visit)
| MJD            | DOUBLE        | double         | modified Julian date of observation
| bandpass       | TEXT          | String         | bandpass used for this observation
| delta_flux     | DOUBLE        | float          | delta from mean flux for this bandpass (mean is typically zero)

## sne_params

| Column          | Type         | Description/Comments
| --------------- | ----------   | --------------------
| htmid_level_6   | INT          | used for spatial indexing
| galaxy_id       | BIGINT       | host galaxy id
| mB              | DOUBLE       | model parameter
| t0_in           | DOUBLE       | model parameter
| x0_in           | DOUBLE       | model parameter
| x1_in           | DOUBLE       | model parameter
| z_in            | DOUBLE       | model parameter
| snid_in         | TEXT         | id of object
| snra_in         | DOUBLE       | right ascension
| sndec_in        | DOUBLE       | declination
