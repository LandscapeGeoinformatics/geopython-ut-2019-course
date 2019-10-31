Exercise 1
==========

**Working with Geometric Objects**

This lesson we will practice how to create geometric objects using Shapely module and how to find out different useful attributes from those geometries.
We will also take advantage of what we have learned earlier, specifically functions, that you should use for making different GIS operations easier to use
in the future. We will also use Pandas to read data from a file.

Write all your codes for all the challenges here into a single ``exercise1.ipynb`` -file, `**submit for grading in Moodle Exercise 1** <https://moodle.ut.ee/mod/assign/view.php?id=528469>`_ by Tuesday, 5 November 2019 , 14:00 pm (EET Tartu time)
Use common sense to structure your Jupyter Notebook file with several cells according to solving the problems from this exercise.
Include comments in order to document your functions and codes.



- Don't forget to check out the `hints for this lesson's exercise <exercise-hints.html>`_ if you're having trouble.

- Scores on this exercise are out of **10 points**.

Sections
--------

 - Problem 1: Creating basic geometries problem-1-creating-basic-geometries_
 - Problem 2: Attributes of geometries problem-2-attributes-of-geometries_
 - Problem 3: Reading coordinates from a file and creating a geometries problem-3-Reading-coordinates-from-a-file-and-creating-a-geometries_
 - Problem 4 (optional): Creating LineStrings that represent the movements problem-4-Creating-LineStrings-that-represent-the-movements-optional-task-for-advanced-students_

.. _problem-1-creating-basic-geometries:

Problem 1: Creating basic geometries (3 Points)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create a function called ``createPointGeom()`` that has two parameters (x_coord, y_coord). Function should create a shapely Point geometry object and return that.
Demonstrate the usage of the function by creating 3 Point -objects with the function.

2. Create a function called ``createLineGeom()`` that takes a list of Shapely Point objects as parameter and returns a
LineString object of those input points. Ideally, the function should try to check that the input list really contains Shapely Point(s).
Demonstrate the usage of the function by creating 2 LineString -objects with the function (one with coordinate tuples, and one with list of shapely Points).

3. Create a function called ``createPolyGeom()`` that takes a list of coordinate tuples **OR** a list of Shapely Point objects and creates/returns
a Polygon object of the input data. Both ways of passing the data to the function should be working.
Demonstrate the usage of the function by passing data first with coordinate-tuples and then with Point -objects.

.. _problem-2-attributes-of-geometries:

Problem 2: Attributes of geometries (3 Points)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create a function called ``getCentroid()`` that takes any kind of Shapely's geometric -object as input and returns a centroid of that geometry. Demonstrate the usage of the function.

2. Create a function called ``getArea()`` that takes a Shapely's Polygon -object as input and returns the area of that geometry. Demonstrate the usage of the function.

3. Create a function called ``getLength()`` takes either a Shapely's LineString or Polygon -object as input. Function should check the type of the input and returns the length of
the line if input is LineString and length of the exterior ring if input is Polygon. If something else is passed to the function,
it should tell the user --> ``"Error: LineString or Polygon geometries required!"``.  Demonstrate the usage of the function.

.. _problem-3-Reading-coordinates-from-a-file-and-creating-a-geometries:

Problem 3: Reading coordinates from a file and creating a geometries (4 Points)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One of the "classical" problems in GIS is the situation where you have a set of coordinates in a file and you need to get them into a map (or into a GIS-software). Python is a really handy
tool to solve this problem as with Python it is basically possible to read data from any kind of input datafile (such as csv-, txt-, excel-, or gpx-files (gps data) or from different databases).
So far, I haven't faced any kind of data or file that would be impossible to read with Python.

Thus, let's see how we can read data from a file and create Point -objects from them that can be saved e.g. as a new Shapefile (we will learn this next lesson).
Our dataset ** `Years.2015-2017.ibtracs_wmo.storms.csv <../_static/data/Exercise1/Years.2015-2017.ibtracs_wmo.storms.csv>`_ ** consist of tracked 
paths of tropical storms, hurricanes etc in the years 2015-2017. The first four rows of our data looks like this:

.. code::

    Name,Serial_Num,year,Basin,Sub_basin,Num,Latitude_first,Longitude_first,Latitude_last,Longitude_last,ISO_time_first,ISO_time_last,Nature
    ADJALI,2014319S06066,2015, SI, MM,1,-6.7,66.4,-11.9,51.4,2014-11-15 06:00:00,2014-11-24 06:00:00, TS
    0220142015:TWO,2014327S08077,2015, SI, MM,2,-8.0,77.3,-28.9,62.5,2014-11-23 06:00:00,2014-12-02 00:00:00, TS
    KATE,2014356S08101,2015, SI, WA,4,-7.5,100.5,-30.0,89.6,2014-12-21 15:00:00,2015-01-04 12:00:00, NR


Thus, we have many columns of data, but the few important ones are:

+------------------+---------------------------------------------------------+
| Column           | Description                                             |
+==================+=========================================================+
| Longitude_first  | Longitude-coordinate of the **first** time of tracking  |
+------------------+---------------------------------------------------------+
| Latitude_first   | Latitude-coordinate of the **first** time of tracking   |
+------------------+---------------------------------------------------------+
| Longitude_last   | Longitude-coordinate of the **last** time of tracking   |
+------------------+---------------------------------------------------------+
| Latitude_last    | Latitude-coordinate of the **last** time of tracking    |
+------------------+---------------------------------------------------------+


**Tasks**

1. Save the ``Years.2015-2017.ibtracs_wmo.storms.csv`` into your computer.
2. We will use only 4 columns, i.e. 'Longitude_first' (x), 'Latitude_first' (y), 'Longitude_last', 'Latitude_last'  from the data in.
3. Iterate over the rows of your DataFrame and create Shapely Point -objects for ``orig_points`` and ``dest_points`` representing the origin locations and destination locations of the storm paths rows, accordingly. Therefore, create two additional columns called ``orig_points`` and ``dest_points`` by applying a function that creates shapely points from the coordinates. Think through, how to make a step-by-step approach based on the lecture and hints provided.

.. _problem-4-Creating-LineStrings-that-represent-the-movements-optional-task-for-advanced-students:

Problem 4: Creating LineStrings that represent the movements (optional task for advanced students, additional max 3 points)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is an optional extra task for those who likes to learn even more.

1. Create an additional column called ``lines``: Iterate over the dataframe again, row by row, and use the origin and destination fields from above and create a Shapely LineString -object between the origin and destination point and add as a new column to your dataframe
2. Find out what is the average (Euclidian) distance of all the origin-destination LineStrings that we just created, and print it; see `Pandas calculate mean for a dataframe. <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mean.html>`_

Consider: To make things more reusable: write creation of the LineString and calculating the average distance into dedicated functions and use them.


