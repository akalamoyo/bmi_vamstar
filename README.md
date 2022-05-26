# Statsmetrics data model #

## Description: ##
This repository contains information on:
- adding and updating metrics/sectors data to the database
- transforming data using forecast, predictive and other statistics models
- creating and saving dynamic reports

### Additional info ###
Database (db) details:

db platform: MongoDB

db name: stats

db collections:
- stats_data - for storing metrics data
- stats_sector - for storing sector data
- run_instance - for storing execution/run information

All *ids* used across collections are unique and serve as unique identifiers for both metric data points and sector data. *ids* for metric data are composed of the sector category plus underscore plus a number which is assigned according to order in which data is collected.

Examples of id for metric data and sector data respectively is:
```sh
education_1, sector_1
```

## 1: How to run program ##
The `main.py` file located in the root folder is the single entry point of the program regardless of whether it is adding, updating data or creating report.
```sh
run main.py
```
The program uses a set of defined configuration available in config.py which must be correctly inputted in the environment in which the program would be run.

When the program is run, it reads in the data folders and where there are additions, these are processed accordingly.

**NB:** No two metric/ sector can have the same *_id*. Ensure *_ids* are correctly and properly defined when inputing to db. There should be no gaps in *_ids*. Meaning that if the last *_id* is *education_1*, the next should be *education_2*.

Every run is captured as a run_instance with all relevant metrics associated with that run stored in the db under `run_instance collection`.

**NB:** A unique identifier is generated on an increment basis for every run

## 2: How to add data to database ##

Input and update data should be added to the data folder as one huge list of dictionaries. The simple way to add data is to fill the data dictionary with the required details and add to the list in `input_metric.json`/`input_sector.json` respectively.

Template for `input_metric.json`:
```sh
{
    "_id": "education_1",
    "metric": "Children per year",
    "description": "Number of children in Nigeria",
    "sector": "education",
    "value_to_transform": null,
    "reference": "Update.com",
    "model": null,
    "params": null,
    "value_type": "actual",
    "value": 19,
    "date_added": "2022-04-30 22:45:43.942880",
    "date_last_updated": "2022-05-09 22:59:52.939133",
    "report": "https://drive.google.com/file/d/1zFirv2lfdcGJ71UYmNHSdnE1Nv9tq6WJ/view?usp=sharing",
    "historic_data": "{'2016': 34, '2017': 47, '2018': 43, '2019': 20, '2020': 36}"
}
```
Template for `input_sector.json`:
```sh
{
    "_id": "sector_1",
    "name": "education",
    "description": "Educational sector comprising of tertiary, primary and secondary",
    "date_added": "2022-05-07 19:36:32.489563",
    "date_last_updated": ""
}
```
## 3: How to update data in database ##
Updating data is quite staright forward. Specify the *_id* of the data point which is to be updated and specify the key which needs to be updated. The *_id* must always be given for any update.

Example: To update reference key of metric, *education_1*, simply add the dictionary below to the update list in `update_metric.json`
```sh
{
	"_id": "education_1",
	"reference": "example.com"
}
```
## 4: How to transform data ##
A huge component of the project is to transform data using a couple of statistical and predictive model.

In order to do this in a standard way across the project, the approach is to define the data to be trasformed in a dictionary format and add to the list in the `transform_metric.json` file located the data folder.

Data to be transform should be defined in the *value_to_transform* key. The model to use for the transform should be defined in the *model* key

Template for transform_metric:
```sh
{
    "_id": "education_3",
    "metric": "Universities in Nigeria",
    "description": "Number of universities in Nigeria",
    "sector": "education",
    "value_to_transform": [20,30,4,16,20],
    "reference": "statista.com",
    "model": "avg_perc_growth",
    "params": ""
}
```

## 5: How to create/update reports ##
Report components are stored in the *reports* folder. As not all metric/sector would have reports, *ids* of those metrics/sectors with reports is saved in the `ids_with_reports.json` file.
- *id*: metric/sector data point with a report.
- *ids_used*: number of *ids* to be used for the report. This is particularly useful for building reports for sectors where more than one metric data points might be used.
- *plot_titles*: title of the plots/graphs in report.
- *plot_types*: types of plots e.g bar, to be used for the graphs in the report.

**NB:** For reports with more than one plot, the order in the lists must be preserved. Meaning that titles in *plot_titles* and types in *plot_types* must correspond to ids order in ids_used key.

Template for defining report:
```sh
{
    "id": "education_1",
    "ids_used": ["education_1"],
    "plot_titles": ["Children per year over time"],
    "plot_type": "bar"
}
```
New templates to be used for a report should be stored as a `.docx` file in a templates folder in the report folder.

Created reports are saved as `.docx` file in the output folder in the report folder which is then uploaded to google drive afterwards.

Once a report is uploaded to googel drive, the permanent download link to the file is updated to 'report' key of the metric/sector data point.

## 6: Unit testing ##
The program uses pytest to unit test functions used in the program. Each test is defined in the `tests` folder located in the root folder of the project.
Each functional unit test comprises of:
- a folder with prefix: `test_{name_of_function_to_test}`
- an `input_data.json` file containg the test data
- an `output_data.json` file containg the output results
- a python file with prefix: `test_{name_of_function_to_test}.py`

**NB:** Every transformation/forecast/predictive model must have a unit test created.