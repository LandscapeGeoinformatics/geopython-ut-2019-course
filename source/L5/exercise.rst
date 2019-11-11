Exercise 3
==========

This lesson we will practice how to do data classification and aggregation in Geopandas for vector and raster data

- Don't forget to check out the [hints for this lesson's exercise](exercise-hints.html) if you're having trouble.

- Scores on this exercise are out of **10 points**.

Sections
--------

Problem 1: Join accessibility datasets into a grid and visualize them by using a classifier (5 points)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The overall aim this task is to understand the *dominance area* \[0\] for **one** of the shopping centers in Helsinki with different travel modes (Public transport, private car).

The *dominance area* is the geographical area from where the given service (shopping center) is the closest one to reach in terms of travel time.


**Steps:**

 - Download a dataset from `**here** <../../_static/exercises/Exercise-4/data/E4.zip>`_ that includes 7 text files containing data about accessibility in Helsinki Region and a Shapefile that contains a Polygon grid that can be used to visualize and analyze the data spatially. The datasets are:

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
 - Submit the code as Jupyter notebook or Python Script and the map(s) you have visualized (as png).
 
 
Problem 2: Create a map of one phenomenon from raster data (5 points)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 In this excercise you will practice making heatmaps with jupyter gmap.

 You may use example dataset about Earthquakes which you can download here `(earthquake dtabase) <https://www.kaggle.com/usgs/earthquake-database>`_
 or you may also try to use your own dataset or find some interesting dataset from Kaggle `(Kaggle datasets) <https://www.kaggle.com/datasets>`_

**Steps:**

 - Download an `earthquake datasets <https://www.kaggle.com/usgs/earthquake-database>`_
    **OR** use your own dataset which has to be initially in csv format (not shp)
    **OR**  find some interesting `dataset from Kaggle <https://www.kaggle.com/datasets>`_. The dataset has to be in csv format (not shp)

 - Read in your csv file and create point geometry from your coordinates
 - Transform the coordinate system into a suitable one
 - Create a heatmap using gmaps
 - Submit the code as Jupyter notebook or Python Script and the heatmap you have visualized (as png).


Problem 3: Classifying population based on population density (optional task for advanced students, additional max 3 points)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the lesson `Classification based on common classification schemes <reclassify.html#classification-based-on-common-classification-schemes>`_ we use again the ``population_admin_units.shp`` dataset.
As we saw, the visualisation of the classification of the administrative units based on population is a bit deceiving as it is not taking into account the amount of people living per km2.
In this task you should redo the classification of the population of the administrative units like we did in the course materials,
but this time **do not** immediately classify the ``population_int`` column, but at first calculate a population density column, which is amount of people per area:

- load the ``population_admin_units.shp`` dataset into a geodataframe
- convert the string-based ``population`` column into a numerical ``population_numeric`` column
- calculate the area in square kilometers (into a column ``area_km2`` ) for each administrative unit, make sure your dataframe is in a projected coordinate system and check the units (meter)
- calculate the population density (into a ``pop_density`` column), population density is ``population_numeric / area_km2``
- now classify ``pop_density`` column and plot again, with at least one of ``Natural_Breaks`` , ``Equal_interval``, ``Quantiles``, OR ``Std_Mean``
- submit code and figure, as usual
