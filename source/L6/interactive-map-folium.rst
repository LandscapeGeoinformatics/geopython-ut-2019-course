Interactive maps on Leaflet
===========================

Whenever you go into a website that has some kind of interactive map, it
is quite probable that you are wittnessing a map that has been made with
a JavaScipt library called `Leaflet <http://leafletjs.com/>`_ (the
other popular one that you might have wittnessed is called
`OpenLayers <https://openlayers.org/>`_).

There is also a Python module called
`Folium <https://python-visualization.github.io/folium/>`_ that makes
it possible visualize data that's been manipulated in Python on an
interactive Leaflet map.


Creating a simple interactive web-map
-------------------------------------

Let's first see how we can do a simple interactive web-map without any data on it. We just visualize OpenStreetMap on a specific location of the a world.

First thing that we need to do is to create a Map instance.
There are few parameters that we can use to adjust how in our Map instance that will affect how the background map will look like.
We should already be able to see what our map looks like. More details can be found in `module API documentation <https://python-visualization.github.io/folium/modules.html>`_.

.. ipython:: python

    import folium

    # Create a Map instance
    m = folium.Map(location=[58.37, 26.72], zoom_start=11, control_scale=True, prefer_canvas=True, width=600, height=450)


The first parameter ``location`` takes a pair of lat, lon values as list as an input which will determine where the map will be positioned when user opens up the map. ``zoom_start`` -parameter adjusts the default zoom-level for the map (the higher the number the closer the zoom is). ``control_scale`` defines if map should have a scalebar or not.

Now we can check how it looks, by either displaying it directly in the Jupyter Notebook:

.. code:: python

    # To display it in a Jupyter notebook, simply ask for the object representation
    m


or by saving it into a html file which we can open in the browser:

.. ipython:: python

    # Filepath to the output
    outfp = "source/_static/img/folium_base_map.html"

    # Save the map
    m.save(outfp)


.. raw:: html
    :file: ../_static/img/folium_base_map.html



It will now just show the basemap in such a way that we initialized it.

Take a look at the map by clicking it with right mouse and open it with Google Chrome which then opens it up in a web browser.

- Let's change the basemap style to ``Stamen Toner`` and change the location of our map slightly. The ``tiles`` -parameter is used for changing the background map provider and map style (see here for all possible ones).

.. ipython:: python

    # Let's change the basemap style to 'Stamen Toner'
    m = folium.Map(location=[58.37, 26.72], tiles='Stamen Toner', zoom_start=11, control_scale=True, prefer_canvas=True, width=600, height=450)


.. code:: python

    # To display it in a Jupyter notebook, simply ask for the object representation
    m


- And in order to save the file:

.. ipython:: python

    # Filepath to the output
    outfp = "source/_static/img/folium_base_map_toner.html"

    # Save the map
    m.save(outfp)


.. raw:: html
    :file: ../_static/img/folium_base_map_toner.html


.. todo:: Task

    Play around with the parameters and save the map and see how those changes affect the look of the map.



Adding layers to the map
------------------------

Adding layers to a web-map is fairly straightforward with Folium and similar procedure as with Bokeh
and we can use familiar tools to handle the data, i.e. Geopandas.
Our ultimate aim is to create a plot like this where population in Tartumaa,
road network and the schools are plotted on top of a web-map.


First we need to prepare the data.

.. ipython:: python

    import geopandas as gpd
    from fiona.crs import from_epsg
    from shapely.geometry import LineString, MultiLineString

    # Filepaths
    grid_fp = "source/_static/data/L6/population_square_km.shp"
    roads_fp = "source/_static/data/L6/roads.shp"
    schools_fp = "source/_static/data/L6/schools_tartu.shp"

    # Read files
    grid = gpd.read_file(grid_fp)
    roads = gpd.read_file(roads_fp)
    schools = gpd.read_file(schools_fp)

    # Re-project to WGS84, Folium requires all data to be in WGS84
    grid['geometry'] = grid['geometry'].to_crs(epsg=4326)
    roads['geometry'] = roads['geometry'].to_crs(epsg=4326)
    schools['geometry'] = schools['geometry'].to_crs(epsg=4326)

    # Make a selection (only data above 0 and below 1000)
    grid = grid.loc[(grid['Population'] > 0)]

    # Create a Geo-id which is needed by the Folium (it needs to have a unique identifier for each row)
    grid['geoid'] = grid.index.astype(str)
    roads['geoid'] = roads.index.astype(str)
    schools['geoid'] = schools.index.astype(str)

    # Select data
    grid = grid[['geoid', 'Population', 'geometry']]
    roads = roads[['geoid', 'TYYP', 'geometry']]
    schools = schools[['geoid', 'name', 'geometry']]

    # convert the dataframe to geojson
    grid_jsontxt = grid.to_json()
    roads_jsontxt = roads.to_json()
    schools_jsontxt = schools.to_json()


Now we have our data stored in the ``grid_jsontxt`` etc. variables as GeoJSON format which basically contains the
data as text in a similar way that it would be written in a ``.geojson`` -file.

Now we can start visualizing our data with Folium.

.. ipython:: python

    m = folium.Map(location=[58.37, 26.72], zoom_start=11, control_scale=True, prefer_canvas=True, width=600, height=450)

    folium.GeoJson(grid_jsontxt).add_to(m)
    folium.GeoJson(roads_jsontxt).add_to(m)
    folium.GeoJson(schools_jsontxt).add_to(m)


.. code:: python

    # To display it in a Jupyter notebook, simply ask for the object representation
    m


- And in order to save the file:

.. ipython:: python

    # Filepath to the output
    outfp = "source/_static/img/folium_geojson_plain.html"

    # Save the map
    m.save(outfp)


.. raw:: html
    :file: ../_static/img/folium_geojson_plain.html


While we can see the geometries, shapes etc, it is not really a helpful map. The roads are barely visible, and the school point markers are fancy, but there are too many on top of each other.

So let's prepare our visualisation step by step. At first we want to make a choropleth map. You remember, the classic map with coloured polygons based on an attribute value.


colormaps: https://nbviewer.jupyter.org/github/python-visualization/folium/blob/master/examples/Colormaps.ipynb


.. ipython:: python

    # create the base map
    m = folium.Map(location=[58.37, 26.72], tiles='Stamen terrain', zoom_start=8, control_scale=True, prefer_canvas=True, width=600, height=450)

    # Create Choropleth map from the polygons where the colors are coming from a column "Population".
    # Notice: 'geoid' column that we created earlier needs to be assigned always as the first column

    # create a basic choropleth map, just polygons with some style information
    folium.Choropleth(
        geo_data=grid_jsontxt,
        fill_color='red',
        fill_opacity=0.3,
        line_weight=1,
    ).add_to(m)

    folium.LayerControl(collapsed=True).add_to(m)


.. code:: python

    # To display it in a Jupyter notebook, simply ask for the object representation
    m


- And in order to save the file:

.. ipython:: python

    # Filepath to the output
    outfp = "source/_static/img/folium_choropleth_plain.html"

    # Save the map
    m.save(outfp)


.. raw:: html
    :file: ../_static/img/folium_choropleth_plain.html


Lets take it a bit further, by classifiying the population column again with Natural Breaks from PySAL.
Create Choropleth map where the colors are now related to the column "pop_km2".

Notice, we also need the 'geoid' column that we created earlier. And it needs to be assigned always as the first column.
And we are adding a LayerControl widget to the map, so we can activate/deactivate layers.

For more infoprmation and configuration examples, you can check `Folium GeoJSON and Choropleth examples here <https://nbviewer.jupyter.org/github/python-visualization/folium/blob/master/examples/GeoJSON_and_choropleth.ipynb>`_.

.. ipython:: python
    :okwarning:

    import pysal.viz.mapclassify as mc

    # Initialize the classifier and apply it
    classifier = mc.NaturalBreaks.make(k=5)

    grid['pop_km2'] = grid[['Population']].apply(classifier)
        
    m = folium.Map(location=[58.37, 26.72],
                tiles='Stamen terrain',
                zoom_start=8,
                control_scale=True,
                prefer_canvas=True,
                width=600,
                height=450)

    # Create Choropleth map where the colors are coming from a column "Population".
    # Notice: 'geoid' column that we created earlier needs to be assigned always as the first column
    folium.Choropleth(
        geo_data=grid_jsontxt,
        data=grid,
        columns=['geoid', 'pop_km2'],
        key_on="feature.id",
        fill_opacity=0.5,
        line_opacity=0.2,
        line_color='white',
        line_weight=0,
        legend_name='Population classified Natural Breaks in Tartu',
        name='Population Grid',
        highlight=False,
        fill_color='RdBu'
    ).add_to(m)

    # and we are adding a LayerControl widget to the map, so we can activate/deactivate the layer
    folium.LayerControl(collapsed=True).add_to(m)


.. code:: python

    # To display it in a Jupyter notebook, simply ask for the object representation
    m


- And in order to save the file:

.. ipython:: python

    # Filepath to the output
    outfp = "source/_static/img/folium_choropleth_nb1.html"

    # Save the map
    m.save(outfp)


.. raw:: html
    :file: ../_static/img/folium_choropleth_nb1.html


Now, we prepare the road lines:

.. ipython:: python

    # define the function to extract the linestring coordinates
    def getLinesAsPointList(row, geom):
        """Returns a list of coordinate pair tuples for the line ('lat', 'lon') of a LineString geometry"""
        if isinstance(row[geom], MultiLineString):
            return []
        else:
            list_x = list(row[geom].coords.xy[0])
            list_y = list(row[geom].coords.xy[1])
            # we need lat lon order for the folium map!!!
            return list(zip(list_y, list_x))


.. ipython:: python

    # Calculate x and y coordinates of the line
    roads['points_list'] = roads.apply(getLinesAsPointList, geom='geometry', axis=1)

    # list of lat lon coordinate pair tuples
    # roadpoints = [a for a in roads['points_list'].tolist() if len(a) >=2 ]
    roadpoints = []
    for a in roads['points_list'].tolist():
        if len(a) >=2:
            roadpoints.append(a)
    
    m = folium.Map(location=[58.37, 26.72],
                tiles='Stamen toner',
                zoom_start=8,
                control_scale=True,
                prefer_canvas=True,
                width=600,
                height=450)
    
    for road in roadpoints:
        folium.PolyLine(locations=road, color="red", weight=2.5, opacity=1).add_to(m)


.. code:: python

    # To display it in a Jupyter notebook, simply ask for the object representation
    m


- And in order to save the file:

.. ipython:: python

    # Filepath to the output
    outfp = "source/_static/img/folium_choropleth_roads.html"

    # Save the map
    m.save(outfp)


.. raw:: html
    :file: ../_static/img/folium_choropleth_roads.html


And finally let's see how we can put points on a map with a bit more control:

.. ipython:: python

    # define the function to extract the linestring coordinates
    from shapely.geometry import Point

    def getPoints(row, geom):
        """Returns coordinate pair tuples for the point ('lat', 'lon') of a Point geometry"""
        if isinstance(row[geom], Point):
            # we need lat lon order for the folium map!!!
            return (row[geom].y, row[geom].x)
        else:
            return ()


Then we create a fresh new map instance and add the schools programmatically:

.. ipython:: python

    m = folium.Map(location=[58.37, 26.72],
                tiles='Stamen terrain',
                zoom_start=8,
                control_scale=True,
                prefer_canvas=True,
                width=600,
                height=450)

    # Calculate x and y coordinates of the line
    schools['points_tuple'] = schools.apply(getPoints, geom='geometry', axis=1)
    
    for idx, school in schools.iterrows():
        folium.CircleMarker(location=school['points_tuple'], popup=school['name'], color="yellow", radius=2.5, opacity=0.9).add_to(m)


.. code:: python

    # To display it in a Jupyter notebook, simply ask for the object representation
    m


- And in order to save the file:

.. ipython:: python

    # Filepath to the output
    outfp = "source/_static/img/folium_better_circle.html"

    # Save the map
    m.save(outfp)


.. raw:: html
    :file: ../_static/img/folium_better_circle.html


This works ok. But now let's try something new to reduce the clutter of many points.
For this we add a "clustering" functionality, so that you see how many points are in an area, without seeing each point.
When you zoom in, this display adapts and shows more spatial details. This way you can provide summary overviews and drill down to each point when desired.

.. ipython:: python

    from folium.plugins import MarkerCluster

    # Get lat and lon of points
    latlon = [[tup[0], tup[1]] for tup in schools['points_tuple'].tolist()]

    m = folium.Map(location=[58.37, 26.72],
                tiles='Stamen terrain',
                zoom_start=8,
                control_scale=True,
                prefer_canvas=True,
                width=600,
                height=450)

    # This function creates clusters for the points that are in the same area
    # and then places them on the map
    MarkerCluster(locations=latlon, fill_color='#2b8cbe', name="Schools", number_of_sides=6, radius=6).add_to(m)

    # we also add a layer control to handle the clustered points as a single layer.
    folium.LayerControl().add_to(m)


.. code:: python

    # To display it in a Jupyter notebook, simply ask for the object representation
    m


- And in order to save the file:

.. ipython:: python

    # Filepath to the output
    outfp = "source/_static/img/folium_marker_cluster.html"

    # Save the map
    m.save(outfp)


.. raw:: html
    :file: ../_static/img/folium_marker_cluster.html


We can also visualise dense point concentrations on a map with a heatmap.
Folium provides `various plugins for extended functionality <https://python-visualization.github.io/folium/plugins.html>`_ 

.. ipython:: python

    from folium.plugins import HeatMap
    import numpy as np

    # you can use weights for the heatmap, in order to make points more important. To demonstrate I use random values, though.
    random_weights = np.random.randint(low=1, high=10, size=len(schools))

    # we add lat, lon, and also weights, into each data point tuple
    heat_data = []

    # Get lat and lon of points, you can do that with or without weights
    for idx, row in schools.iterrows():
        tup = row['points_tuple']
        elem = [tup[0], tup[1], int(random_weights[idx])]
        heat_data.append(elem)

    # create the base map
    m = folium.Map(location=[58.37, 26.72],
                tiles='Stamen toner',
                zoom_start=8,
                control_scale=True,
                prefer_canvas=True,
                width=600,
                height=450)

    # This function creates the heatmap based on the points and weights that are in close area
    # and then places them on the map
    HeatMap(data=heat_data,
            name="schools density",
            min_opacity=0.5,
            max_zoom=18,
            max_val=1.0,
            radius=25,
            blur=15,
            overlay=True,
            control=True).add_to(m)

    # and we add the layer control
    folium.LayerControl().add_to(m)


.. code:: python

    # To display it in a Jupyter notebook, simply ask for the object representation
    m


- And in order to save the file:

.. ipython:: python

    # Filepath to the output
    outfp = "source/_static/img/folium_heatmap.html"

    # Save the map
    m.save(outfp)


.. raw:: html
    :file: ../_static/img/folium_heatmap.html


For mor edetailed API information, `consult the docs <https://python-visualization.github.io/folium/plugins.html#folium.plugins.HeatMap>`_.

And now we can put it all together in one map:

.. ipython:: python

    # basemap
    m = folium.Map(location=[58.37, 26.72],
                tiles='Stamen toner',
                zoom_start=8,
                control_scale=True,
                prefer_canvas=True,
                width=600,
                height=450)

    # coloured polygon layer
    folium.Choropleth(
        geo_data=grid_jsontxt,
        data=grid,
        columns=['geoid', 'pop_km2'],
        key_on="feature.id",
        fill_color='RdBu',
        fill_opacity=0.5,
        line_opacity=0.2,
        line_color='white',
        line_weight=0,
        legend_name='Population in Tartu',
        name='Population Grid',
        highlight=False
    ).add_to(m)

    # heatmap layer
    HeatMap(data=heat_data,
            name="schools density",
            min_opacity=0.5,
            max_zoom=18,
            max_val=1.0,
            radius=25,
            blur=15,
            overlay=True,
            control=True).add_to(m)

    # initalise a road layer holing object
    roads_layer = folium.FeatureGroup(name="roads layer")

    # add the roads to the intermediate layer object, and not directly to the map
    for road in roadpoints:
        folium.PolyLine(locations=road, color="grey", weight=2.5, opacity=1).add_to(roads_layer)

    # then we add the roads layer to the map
    roads_layer.add_to(m)

    # This function creates clusters for the points that are in the same area
    marker_cluster = MarkerCluster(name="Schools marker cluster", number_of_sides=6, radius=6)

    # and then places them in the marker cluster
    for idx, school in schools.iterrows():
        folium.Marker(location=school['points_tuple'],
                            popup=school['name'],
                            color="yellow",
                            radius=5,
                            opacity=0.9).add_to(marker_cluster)

    # and add the marker cluster to the map
    marker_cluster.add_to(m)

    # create another layer object for the circle markers
    circles_layer = folium.FeatureGroup(name="circles layer")

    # the yellow school circles as reference
    for idx, school in schools.iterrows():
        folium.CircleMarker(location=school['points_tuple'],
                            popup=school['name'],
                            color="yellow",
                            radius=2.5,
                            opacity=0.9).add_to(circles_layer)

    # and add the circle layer to the map
    circles_layer.add_to(m)

    # add the layer control switch, which can now control the separate layer holding objects for the single points and roads
    folium.LayerControl().add_to(m)


That's it! Now we have a cool interactive map with markers, clustered markers, roads, a heatmap and a choropleth grid showing the population in the Tartumaa Region on top of a basemap.
You can save it and open it with your browser and see the result.

.. code:: python

    # To display it in a Jupyter notebook, simply ask for the object representation
    m


- And in order to save the file:

.. ipython:: python

    # Filepath to the output
    outfp = "source/_static/img/folium_full_map.html"

    # Save the map
    m.save(outfp)


.. raw:: html
    :file: ../_static/img/folium_full_map.html
