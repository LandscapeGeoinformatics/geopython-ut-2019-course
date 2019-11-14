Exercise 3
==========

This lesson we will practice how to do data classification and aggregation in Geopandas for vector and raster data

- Don't forget to check out the [hints for this lesson's exercise](exercise-hints.html) if you're having trouble.

- Scores on this exercise are out of **10 points**.

Sections
--------


At first download the exercise 3 datasets `Exercise3.zip <../_static/data/Exercise3/Exercise3.zip>`_


Problem 1: Create a map of a phenomenon from raster data and classify with zonal statistics (5 points)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. read in data

   - read in the European countries shapefile ``europe_lowres.shp``
   - read in the raster of precipitation data ``gpcc_precip_2018_11.tif`` (gridded monthly totals of rainfall in November 2018 in mm), Meyer-Christoffer, Anja; Becker, Andreas; Finger, Peter; Schneider, Udo; Ziese, Markus (2018): GPCC Climatology Version 2018 at 0.25°: Monthly Land-Surface Precipitation Climatology for Every Month and the Total Year from Rain-Gauges built on GTS-based and Historical Data. `DOI: 10.5676/DWD_GPCC/CLIM_M_V2018_025 <https://opendata.dwd.de/climate_environment/GPCC/html/gpcc_normals_v2018_doi_download.html>`_

2. basic plot

   - check coordinate systems (CRS) of both datasets and transform into the same if necessary
   - Create a map by plotting the raster with a suitable colormap (https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html) and the polygons on top, so that we can still see the raster pixels (no filling for the polygons)

3. zonal raster statictics

   - summarise the absolute amount of rainfall per country with zonal mean, sum and range statistic ``zonal_stats`` -> ``mean, sum, range`` and these to the countries geodataframe. ``sum`` summarises, aka adds up, all numbers of grid cells/pixels under each polygon. ``range`` calculates the difference between the minimum and maximum of grid cell/pixel value under each polygon and provides
   - rename the columns into ``mean_rainfall``, ``sum_rainfall`` and ``delta_rainfall``
   - visualize each of these statistics in a plot as map and basic histogram to understand the spatial distribution and value frequencies to better understand the data, use titles on the plots to make sure we know which variable is plotted

4. Classify

- reproject your europe countries dataframe with the statistics columns included in the projected coordinate system EPSG:3035 (`ETRS89 / LAEA Europe <https://epsg.io/3035>`_)
- calculate the area in square kilometers for each country (into a column ``area_km2`` )
- calculate the average rainfall (into a ``average_precip_km2`` column), which is ``sum_rainfall / area_km2``
- now classify ``average_precip_km2`` column and plot again, with at least one of ``NaturalBreaks`` , ``EqualInterval``, ``Quantiles``, OR ``StdMean``

5. Answer questions and submit all results

- compare ``average_precip_km2`` with ``mean_rainfall``, what do you observe?
- Which country has had the highest variability in rainfall in that month?
- submit code and figures, as usual as Jupyter notebook and the maps you have visualized (as png).


Problem 2: Join accessibility datasets into a grid and visualize them by using a classifier (5 points)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The overall aim this task is to understand the *dominance area* \[0\] for **one** of the shopping centers in Helsinki with different travel modes (Public transport, private car).

The *dominance area* is the geographical area from where the given service (shopping center) is the closest one to reach in terms of travel time.


**Steps:**

- Download a exercise datasets include 7 text files containing data about accessibility in Helsinki Region and a Shapefile that contains a Polygon grid that can be used to visualize and analyze the data spatially. The datasets are:

   - ``travel_times_to_[XXXXXXX]_[NAME-OF-THE-CENTER].txt`` including travel times and road network distances to specific shopping center
   - ``MetropAccess_YKR_grid_EurefFIN.shp`` including the Polygon grid with 'YKR_ID' column that can be used to join the grid with the accessibility data

- Read the travel_time data file for one of the shopping centres with Pandas and select only following columns from them:

   - pt_r_tt:  travel mode Public tranport
   - car_r_t: travel mode private car
   - from_id: travel start from (refering to a YKR_ID grid "coordinate")
   - to_id: travel destination (the YKR_ID frid coordinate of the shopping centre), that's why it is staying the same per shopping centre file

- load the MetropAccess shapefile with geopandas
- join/merge the shopping centre dataframe with the Metro grid dataframe based on the ID / YKR_ID column
- create a classifier (custom or common one) based on the materials that we went through in the `lesson materials <reclassify.html>`_
- You need to classify the data into a new column in your GeoDataFrame. For classification, you can **either**:

   - Use the `common classifiers from pysal <reclassify.html>`_

   - **OR** create your own `custom classifiers from pysal <reclassify.html>`_. If you create your own, remember to document it well how it works! Write a general description of it and comment your code as well.

- Visualize the **classified** travel times (Public transport AND Car) of the shopping centre with appropriate plots.
- submit code and figures, as usual as Jupyter notebook and the maps you have visualized (as png).


Optional task for advanced students (additional max 3 points)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clip the precipitation raster file (while still in EPSG:4326) for European countries and then reproject (into EPSG:3035) and plot it with the Europe countries shapefile (in EPSG:3035). Make it look good.