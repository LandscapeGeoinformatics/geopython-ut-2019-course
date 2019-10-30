Alternative installation method for Conda environments
------------------------------------------------------

In the previous section we installed our specific conda Python environment wit ha pre-defined environment configuration file. In this section we show an alternative variant how you can install conda environments in a more flexible way if you need to.


.. admonition:: BEWARE:

    Please don't do the following steps, because you already have the environment install via the ``enviroment.yml`` configuration above.

The other variant is typically more widely used in exploratory setups. It is a step-by-step procedure. Here we are making sure that Python in version 3.7 will be installed and that we want to explicitly use the additional package channels pyviz and conda-forge.
And we gibe the environment a name (-n).

If you would create your environment manually, it would go like that:
Open the ``Anaconda prompt`` from the Start Menu and type the command below.

.. code::

    (C:\dev\conda3) conda create -n geopy2019alt python=3.7 -c pyviz -c conda-forge

Ok, now that we have installed a Python working environment with the name ``geopy2019alt`` with our desired library packages, we can check installed environments just to be sure.
In order to show all environments that have already been created you can ask conda to list these:

.. code::

    (C:\dev\conda3)  conda env list

Now we want to activate that environment, install additional packages and start working with it:

.. code::

    (C:\dev\conda3)  activate geopy2019alt

    (geopy2019alt)


Install GIS related packages with conda by running in command prompt following commands (in the same order as they are listed).
Make sure you are in the correct enviroment (don't install into ``base``, install new packages ideally only into your designated created environments)

.. code::

    (geopy2019alt) conda install -c pyviz -c conda-forge numpy pandas gdal fiona shapely geopandas geoviews

    # Install matplotlib
    (geopy2019alt) conda install -c pyviz -c conda-forge matplotlib

    # Install scipy
    (geopy2019alt) conda install -c pyviz -c conda-forge scipy

    #Install Jupyter Notebook
    (geopy2019alt) conda install -c pyviz -c conda-forge jupyter

    # Install rasterio and rasterstats
    (geopy2019alt) conda install -c pyviz -c conda-forge rasterio rasterstats

    # Install seaborn
    (geopy2019alt) conda install -c pyviz -c conda-forge seaborn

    # Install geoplot and cartopy
    (geopy2019alt) conda install -c pyviz -c conda-forge geoplot cartopy

    # Install pysal and mapclassify
    (geopy2019alt) conda install -c pyviz -c conda-forge pysal mapclassify

    # Install bokeh
    (geopy2019alt) conda install -c pyviz -c conda-forge bokeh

    # Install Folium
    (geopy2019alt) conda install -c pyviz -c conda-forge folium


.. commented out
    # Install networkx (v 1.11) --> bundled with decorator (v 4.1.2)
    conda install networkx
    # Install PySpark (v 2.2.0) --> bundled with py4j (v 0.10.6)
    conda install pyspark
    # Install osmnx (v 0.5.4) --> bundled with altair, bleach, branca, colorama, entrypoints, folium, geopy, html5lib, ipykernel, ipython, ipython_genutils, jedi, jsonschema, jupyter_client, jupyter_core, mistune, nbconvert, nbformat, notebook, pandoc, pandocfilters, pickleshare, prompt_toolkit, pygments, pyzmq, simplegeneric, testpath, traitlets, vega, vincent, wcwidth, webencodings
    conda install -c conda-forge osmnx
    # Install Dash using Pip
    pip install dash==0.19.0  # The core dash backend
    pip install dash-renderer==0.11.1  # The dash front-end
    pip install dash-html-components==0.8.0  # HTML components
    pip install dash-core-components==0.14.0  # Supercharged components
    pip install plotly --upgrade  # Plotly graphing library

In the next step we will verify the installation of our conda Python environment and configure Jupyter Notebooks.
