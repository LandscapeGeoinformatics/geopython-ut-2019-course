Exercise 2 hints
================


Hints regarding the some_posts.csv dataset
------------------------------------------

- You are not supposed to manually work with the data (e.g. Excel or something)
- Reuse your "create_lineGeom" function from Exercise 1
- be defensive, so that either you get a valid line_string, or otherwise don't use that users movement in the new movements geodataframe
- reuse your calculate lengths from exercise 1, as it is now in a metric-unit projected coordinate system, the lengths are already meaningful

Converting Pandas DataFrame into a GeoDataFrame
-----------------------------------------------

Quite often you are in a situation where you have read data e.g. from text file into a Pandas DataFrame where you have latitude and longitude columns representing the location of a record.

- Let's continue with the previous example and consider that we have a column where we have stored the shapely geometries:

.. code:: python

     >>> print(data)
         value  lat  lon     geometry
     0      0    2    4  POINT (4 2)
     1      5    1    6  POINT (6 1)
     2      2    6    1  POINT (1 6)
     3      6    6    3  POINT (3 6)
     4      5    5    1  POINT (1 5)


- Notice that now our data is still a Pandas **DataFrame**, not a GeoDataFrame:

.. code:: python

    >>> type(data)
    pandas.core.frame.DataFrame


We need to convert the DataFrame into a GeoDataFrame, so that we can e.g. save it into a Shapefile.
It is easily done by passing the DataFrame into a GeoDataFrame object.
Now we need to determine     which column contains the geometry information (needs to be always a column called 'geometry'),
and optionally we can also determine the coordinate reference system when creating the GeoDataFrame:

.. code:: python

    # Convert DataFrame into a GeoDataFrame (providing the "geomtry" column from the pandas dataframe explicitly for GeoPandas dataframe as the geometry per feature)
    geo = gpd.GeoDataFrame(data, geometry='geometry', crs=from_epsg(4326))

    >>> type(geo)
    geopandas.geodataframe.GeoDataFrame

    >>> geo.crs
    {'init': 'epsg:4326', 'no_defs': True}

Now we have converted Pandas DataFrame into a proper GeoDataFrame that we can export into a Shapefile for instance.


Different variants to join two list
-----------------------------------

- side note: checking the length of a list, how many elements it contains

.. code::

    my_length = len(list_1)


- via a dataframe building column-wise:

.. code::

    # dataframe from dict { 'column_name': list_of_data ... }
    # if you have several lists, ideally they should be of same length
    dfp = pd.DataFrame( {'xcoords': list_1, 'ycoords': list_2} )

    def make_pair(row):
        return (row['xcoords'], row['ycoords'])

    dfp['coord_pairs'] = dfp.apply(make_pair, axis=1)
    dfp['coord_pairs'].tolist()


- manual iterating over list positioning:

.. code::

    list_length = len(list_1)
    coordpairs = []
    for x in range(0, list_length):
        coordpairs.append((list_1[i], list_2[i]))


- the special Python zip method (imagine a zipper):

.. code::

    # zipped variable here is in a state of waiting to be iterated over, zipped itself is not yet a list again
    zipped = zip(list_1, list_2)
    # trying to make a python list out of something list-like or something that can be iterated over
    coord_list = list(zipped)


Sorting and Adding "advanced functions usage on the dataframes
--------------------------------------------------------------

- use the sort_values `sort <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html>`_ to sort the rows by timestamp
- In this case, we actually want to sort and work the "whole" thing, and therefore use axis=0 (NOT axis=1 like with functions apply) or just omit axis keyword should do just fine.
- no need to translate the "text" based timestamp into a date format, because the "timestamp" is formatted iso, year first then month etc, text or string-wise sorting is working ok
- in order to `add/append <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.append.html>`_ new rows to our new empty dataframe - here are two examples, but in both you ideally collect the new rows at first in a separate list:

.. code::

    # version 1:
    # append row by row, gives you more control based on how you stored the intermediate new rows in your list (e.g. as tuple or [] pair)
    for idx in range(0, len(new_rows)):
        newdata = newdata.append({'userid': new_rows[idx][0], 'geometry': new_rows[idx][1]}, ignore_index=True)

.. code::

    # version 2:
    # directly create a temporary dataframe and use collected rows-list;
    # the rows-list needs to be a "list of lists", where each "sublists" consists of the entries for each row
    temp_df = pd.DataFrame(new_rows, columns=['userid','geometry'])
    # and then "just" append the temp dataframe onto the other dataframe
    newdata = newdata.append(temp_df, sort=False)

