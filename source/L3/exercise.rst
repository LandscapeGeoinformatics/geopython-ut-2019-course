Exercise 2
==========

This lesson we will focus on how to create geometries in Geopandas and how to re-project data and do some basic
geometric calculations.

- Don't forget to check out the `hints for this lesson's exercise <exercise-hints.html>`_ if you're having trouble.
- Scores on this exercise are out of **10 points**.

Sections
--------

 - `Problem 1: Create Polygon from lists of coordinates <#problem-1-create-polygon-from-lists-of-coordinates>`_
 - `Problem 2: Points to map <#problem-2-points-to-map>`_
 - `Problem 3: How long distance have storms travelled? <#problem-3-movements-of-individual-storms>`_

Problem 1: Create Polygon from lists of coordinates (2 points)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the first problem you should:

 - create a Polygon out of the the x and y coordinates that are provided in the ``create_polygon.py`` -script.
 - insert the polygon into a GeoDataFrame
 - save the Polygon into a Shapefile.
 - plot and save a figure out of the Polygon.

The `**create_polygon.py** <../_static/data/Exercise2/create_polygon.py>`_ starter script has all necessary steps listed and also some hints are provided.
Copy the code into your Jupyter notebook for the exercise.
There are all together 6 steps that you need to fill to accomplish the problem 1.
Each step that you need to fill is marked with capital P -letter (P1 to P6).

Problem 2: Points to map (3 points)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The problem 2 this lesson continues the process that we started last lesson, i.e. creating geometric point -objects and putting them into a map.
Here our aim is to plot a set of x and y coordinates that we should read from the `**Years.2015-2017.ibtracs_wmo.storms.north_atlantic.csv** <../_static/data/Exercise2/Years.2015-2017.ibtracs_wmo.storms.north_atlantic.csv>`_ comma separated file that contains following kind of data:

.. code::

    Serial_Num,Season,Num,Basin,Sub_basin,Name,ISO_time,Nature,Latitude,Longitude,Wind(WMO),Pres(WMO),Center,Wind(WMO) Percentile,Pres(WMO) Percentile,Track_type
    2014356S08101,2015,4, SI, WA,KATE,2014-12-21 15:00:00, NR,-7.5,100.5,15.0,1007.0,bom,0.16899999999999998,0.828,main
    2014356S08101,2015,4, SI, WA,KATE,2014-12-21 18:00:00, NR,-7.71,100.63,15.0,1007.0,bom,0.16899999999999998,0.828,main
    2014356S08101,2015,4, SI, WA,KATE,2014-12-21 22:07:00, NR,-8.0,100.8,-1.0,-1.0,bom,-100.0,-100.0,main


The data has 1627 rows and consists of locations, times and addirional informations of tracked storms, hurricanes etc. in the North Atlantic for the years 2015-2017:

+------------------+---------------------------------------------------------+
| Column           | Description                                             |
+==================+=========================================================+
| Latitude         | y-coordinate of the post                                |
+------------------+---------------------------------------------------------+
| Longitude        | x-coordinate of the post                                |
+------------------+---------------------------------------------------------+
| Serial_Num       | a unique ID for each on-going storm                     |
+------------------+---------------------------------------------------------+
| Name             | A name assigned to a large individual storm             |
+------------------+---------------------------------------------------------+

.. note::

    The data only contains storms for the North Atlantic. Also, names are assigned on a yearly basis and might or might not be 
    used for different storms in different years.


- `Download the data **Years.2015-2017.ibtracs_wmo.storms.north_atlantic.csv** <../_static/data/Exercise2/Years.2015-2017.ibtracs_wmo.storms.north_atlantic.csv>`_ (Click on the link ==> CNTRL + S)
- Read the data into memory using Pandas
- Create an empty column called ``geometry`` where you will store shapely Point objects
- Iterate over the rows of the DataFrame and insert Point objects into the column geometry (for example, via apply or using .loc indexer to update the row, `see materials <../L2/geopandas-basics.html#creating-geometries-into-a-geodataframe>`_
- Convert that DataFrame into a GeoDataFrame, `see hints <exercise-hints.html>`_
- set the CRS for coordinate system as WGS84 (i.e. epsg code: 4326)
- Save the data into a Shapefile called ``storm_track_positions.shp``
- Create a simple map of those points using the ``.plot()`` -function in Python. Save it as a png file (storm_track_positions.png).


Problem 3: How long distance individual storms have travelled? (3 points)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this problem the aim is to calculate the distance in kilometers that the individual storms have travelled according to
their tracking points (distances in kilometers from first tracking to last tracking point along their tracked paths).

Write your codes into the same notebook for the previous Problem (2).

In your code you should:

 - Group the data by userid
 - Create an empty GeoDataFrame called ``movements``
 - Set the CRS of the ``movements`` GeoDataFrame to ``EPSG:4326``

 - For each user:
    - `sort <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html>`_ the rows by timestamp
    - create LineString objects based on the points
    - `add <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.append.html>`_ the geometry and the userid into the GeoDataFrame you created in the last step
 
  - Save the movements of into a Shapefile called ``Some_movements.shp``

- Reproject the data from WGS84 into the `EPSG:4087 <https://epsg.io/4087>`_ WGS 84 / World Equidistant Cylindrical -projection to transform the data into a distance-preserving metric-based system.
- load world countries shapefile, reproject into same CRS and plot together with storm paths
- Calculate the lenghts of the storm lines into a new column called ``distance`` in ``movements`` GeoDataFrame.

2. Calculate the storm path distances again based on the ``EPSG:3857 <https://epsg.io/3857>`_ web mercator -projection? What do you observe?

Questions
---------

Write your answers below the solved problems in your code file.
You should also print the answers to the questions in your code.

 - What was the shortest distance travelled in kilometers?
 - What was the mean distance travelled in kilometers?
 - What was the maximum distance travelled in kilometers?

Optional task for advanced students (additional max 3 points)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Which storm(s) made landfall in the USA? Make appropriate geographic queries (e.g. PIP, touch or intersect) to find out which storm paths are passing over USA continental territory (``'name'=='United States of America'``).
2. Define an Azimuthal Equi-Distant projection centered in the middle (centroid) of all the storms (tracking positions or paths) in order to re-calculate the distances even more correctly.

See lesson, where we recentered the European projection string definition.

.. code:: Python

    from shapely.geometry import MultiPoint
    p = MultiPoint([v for v in geo_df['geometry'].values]).centroid
    print(p)
    POINT (-58.02241566920573 26.17170837867247)
