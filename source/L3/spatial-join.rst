
Spatial join
============

`A Spatial join <http://wiki.gis.com/wiki/index.php/Spatial_Join>`_ is
yet another classic GIS problem. Getting attributes from one layer and
transferring them into another layer based on their spatial relationship
is something you most likely need to do on a regular basis.

The previous materials focused on learning how to perform a `Point in Polygon query <point-in-polygon.html>`_.
We could now apply those techniques and create our
own function to perform a spatial join between two layers based on their
spatial relationship. We could for example join the attributes of a
polygon layer into a point layer where each point would get the
attributes of a polygon that ``contains`` the point.

Luckily, `spatial joins <http://geopandas.org/mergingdata.html#spatial-joins>`_
(``gpd.sjoin()`` -function) is already implemented in Geopandas, thus we
do not need to create it ourselves. There are three possible types of
join that can be applied in spatial join that are determined with ``op``
-parameter:

-  ``"intersects"``
-  ``"within"``
-  ``"contains"``

Sounds familiar? Yep, all of those spatial relationships were discussed
in the `previous materials <point-in-polygon.html>`_, thus you should know how they work.

Let's perform a spatial join between the species  `Shapefile (addresses.shp) <../_static/data/L3/addresses.zip>`_
and a Polygon layer that is a 250m x 250m grid showing the amount of people living in Helsinki Region.


Download and clean the data
~~~~~~~~~~~~~~~~~~~~~~~~~~~

For this lesson we will be using publicly available `Corine Landuse Cover for the Porijogi region <../_static/data/L3/porijogi_corine_landuse.zip>`_ in Tartumaa.

-  Unzip the file into into your L3 folder

.. code::

    porijogi_corine_landuse.dbf  porijogi_corine_landuse.shp
    porijogi_corine_landuse.prj  porijogi_corine_landuse.shx

You should now have the files listed above in your Data folder.

-  Let's read the data into geopandas and see what we have.

.. ipython:: python

    import geopandas as gpd

    # Filepath
    fp = "source/_static/data/L3/porijogi_corine_landuse.shp"

    # Read the data
    lulc = gpd.read_file(fp)

.. ipython:: python

    # See the first rows
    lulc.head()

Okey so we have multiple columns in the dataset but the most important
one here is the column ``clc_int`` (*corine landuse code*) that
tells the type of landuse cover under that polygon.

In order to know what the codes mean, we will merge a lookup table to our spatial landuse cover GeoDataframe.

.. ipython:: python

    import pandas as pd
    codes = pd.read_csv('source/_static/data/L3/corine_landuse_codes.csv', sep=';')
    codes


This table contains a field ``CLC_CODE`` which we use to connect the correct mapping to our landuse cover GeoDataframe, which has a field ``clc_int``.
We will now merge the lookup table ``codes`` (a Pandas dataframe) into our ``lulc`` GeoDataframe, based on the identifiers in the mentioned fields: 


.. ipython:: python

    lulc = lulc.merge(codes, left_on='clc_int', right_on='CLC_CODE')
    lulc.sample(10)


.. ipython:: python

    # See the column names and confirm that we now have a column called LABEL2, that gives us some textual description for the landuse codes
    lulc.columns

-  Let's also get rid of all unnecessary columns by selecting only
   columns that we need i.e. ``Landuse``, ``LABEL2`` and ``geometry``

.. ipython:: python

    # Columns that will be sected
    selected_cols = ['Landuse', 'LABEL2','geometry']

    # Select those columns
    lulc = lulc[selected_cols]

    # Let's see 10 randomly sampled rows
    lulc.sample(10)


Now we have cleaned the data and have only those columns that we need
for our analysis.


Join the layers
~~~~~~~~~~~~~~~

Now we are ready to perform the spatial join between the two layers that
we have. The aim here is to get information about **how many species sightings (of which species) happened in which landuse types?** . Thus, we want
to join attributes from the landuse layer we just modified into the already used and 
prepared monitoring GeoPackage file, `category_3_species_porijogi.gpkg <../_static/data/L3/category_3_species_porijogi.gpkg>`_.

-  Read the category_3_species_porijogi.gpkg layer into memory

.. ipython:: python

    # protected species under class 3 monitoring sightings
    species_fp = "source/_static/data/L3/category_3_species_porijogi.gpkg"
    
    # Read data
    species = gpd.read_file(species_fp, layer='category_3_species_porijogi', driver='GPKG')



-  Let's make sure that the coordinate reference system of the layers
   are identical

.. ipython:: python

    # Check the crs of landuse
    lulc.crs
    
    # Check the crs of species layer in case we need to reproject the geometries to make them comparable
    species.crs

    # Do they match? - We can test that
    lulc.crs == species.crs

They are identical. Thus, we can be sure that when doing spatial
queries between layers the locations match and we get the right results
e.g. from the spatial join that we are conducting here.

-  Let's now join the attributes from ``lulc`` (2) GeoDataFrame into
   ``species`` GeoDataFrame (1) by using ``gpd.sjoin()`` -function

.. ipython:: python

    # Make a spatial join
    join = gpd.sjoin(species, lulc, how="inner", op="within")
    
    # Let's check the result
    join.head()

Awesome! Now we have performed a successful spatial join where we got
two new columns into our ``join`` GeoDataFrame, i.e. ``index_right``
that tells the index of the matching polygon in the ``lulc`` layer and
``species``.

-  Let's save this layer into a new Shapefile

.. code:: python

    # Output path
    outfp = "source/_static/data/L3/landuse_per_species.shp"
    
    # Save to disk
    join.to_file(outfp)

Do the results make sense? Let's evaluate this a bit by grouping and querying the
resulting ``join`` for largest landuse type and species types combinations:

.. ipython:: python

    join['NIMI'].value_counts()


.. ipython:: python
    
    join['LABEL2'].value_counts()


.. ipython:: python

    for species_id, species_group in join.groupby('NIMI'):
        lulc_count = species_group['LABEL2'].value_counts()
        top = lulc_count.head(1)
        # display(type(top))
        # print(top)
        print("species_id: {}, number of sightings: {}, top lulc: {}, number: {}".format(species_id, len(species_group), top.index[0], top[0] ))
