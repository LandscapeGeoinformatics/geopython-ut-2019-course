Installation and verifying setup for Python + GIS
=================================================

.. note::

    In the University computer lab you DO NOT have to install Anaconda or Miniconda or any other Python distribution.
    If you are attending the course in the University computer lab, please jump to `Verifying the installation <Installing_Miniconda_GIS.html#verifying-the-installation>`_ and create the working environment.
    This section only for general info if you want to install Python on your own computer, and for remote students.

Install Python + GIS on Windows
-------------------------------

**How to start doing GIS with Python on a computer?**

Well, first you need to install Python and necessary Python modules that are used to perform various GIS-tasks. The purpose of this page is to help you
out installing Python and all those modules into your own computer. Even though it is possible to install Python from their `homepage <https://www.python.org/>`_,
**we highly recommend using** `Miniconda <https://conda.io/miniconda.html>`_ or `Anaconda <https://www.anaconda.com/distribution/>`_ which is an open source distribution of the Python and R programming
languages for large-scale data processing, predictive analytics, and scientific computing, that aims to simplify package management and deployment. In short,
it makes life much easier when installing new tools on your Python to play with.

.. note::

    **Miniconda** is an encapsulated versatile virtual python environment installer,
    that works under the hood of the big Anaconda python distribution.
    Miniconda is basically a mini version of Anaconda that includes only the conda package manager and its dependencies!


https://conda.io/miniconda.html

Following steps have been tested to work on Windows 7 and 10 with Anaconda/Miniconda 64 bit.

`Download Miniconda installer (64 bit) <https://repo.continuum.io/miniconda/Miniconda3-latest-Windows-x86_64.exe>`_ a Python 3.6, 64-bit (exe installer) for Windows.

.. admonition:: BEWARE:

    - To install miniconda SYSTEM-WIDE for ALL users, this does require administrator permissions;
      every users can then create their own environments with the conda tool.
    - Please do NOT make Conda the default python for the system if you don't want it to interfere with other Python installations you might have,
      eg. Pythons of ArcGIS and QGis etc

Install Miniconda on your computer by double clicking the installer and install it into a directory you want.

Install it to **all users** and use default settings.

Additional install information:
https://conda.io/projects/conda/en/latest/user-guide/index.html

Verifying the installation
--------------------------

.. note::

    As a convention, whenever I demonstrate Python codes or using commands on the the shell/cmd commandline,
    using the ``#`` symbol implies a ``comment``. This line, respectively everything after that symbol is NOT to be executed.


In order to test that the ``conda`` package manager works we have to go through a few more steps:
After successful installation you should have a menu entry in the Windows Start Menu:

``Anaconda Prompt``

This is a Windows CMD (Commandline window, that "knows" about, where your Miniconda/Anaconda installation lies, and where to find the ``conda`` tool (without interfering other Python installations on your computer).
After it opens it should display somehow like so:

.. code::

    (base) C:\Users\Alexander>

    or

    (C:\dev\conda3) C:\Users\Alexander>

On the command line type command ``conda --version`` in order to see if the command is successful, it should show the version of the conda tool.

.. code::

    (base) C:\Users\Alexander> conda --version
    conda 4.7.12

Creating environments and install packages
------------------------------------------

How to use the conda command? Open the Anaconda/conda command prompt from the Start menu:

``conda`` basically represents a typical Python virtualenv command. You can create a several distinct environments, with different Python version, and with different packages to be installed.
This will come in very handy to *try out* new libraries/packages/tools, without breaking you working installation.

https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html

We want to use a modern Python version 3.7. Here it becomes obvious how practical virtual environments can be.
They help you to keep various Python versions around without messing up your system, and at the same time, keep several working environments with different, possibly conflicting versions of different Python packages.

There are two main ways of creating a ``conda`` environment. 

The alternative and possibly more professional/reproducible way is to use a so called ``environment.yml`` file. In the file the environment name, the package channels, Python version and all desired packages are declared.
This way, you should be able to install the same environment in different computers, therfore improving the reliability of having the same packages etc installed. You can even go so far as to specify the exact package version.

In order to be well organised throughout the course, please create a working folder/directory, where you will put your scripts and data files for the lab sessions and homeworks.
On Windows you have your local user folder, typically ``C:\Users\Alexander``. Open with the Windows File Explorer and create a new folder in this folder, with the name ``geopython2019``.

.. admonition:: BEWARE:

    Make sure you are using the correct folder on the University computers. In the Windows File Explorer, go via ``this PC``, ``c:\Users`` to ``your account name`` folder. In this folder create your working directory ``geopython2019``!

Please download the prepared `enviroment.yml <../_static/data/environment.yml>`_ file and save it to your newly created working folder.

.. code::

    (C:\dev\conda3) cd C:\Users\Alexander\geopython2019
    (C:\dev\conda3) conda env create -f environment.yml
  

This will take some time.

The other variant is typically more widely used in exploratory setups. It is a step-by-step procedure. Here we are making sure that Python in version 3.7 will be installed and that we want to explicitly use the additional package channels pyviz and conda-forge.
And we gibe the environment a name ( -n ).

.. admonition:: BEWARE:

    Please don't do this, because you already have the environment install via the ``enviroment.yml`` configuration above.

.. code::

    (C:\dev\conda3) conda create -n geopy2019 python=3.7 -c pyviz -c conda-forge

Ok, now that we have installed a Python working environment with our desired library packages, we can check installed environments just to be sure.
In order to show all environments that have already been created you can ask conda to list these:

.. code::

    (C:\dev\conda3)  conda env list

Now we want to activate that environment and start working with it:

.. code::

    (C:\dev\conda3)  activate geopy2019

    (geopy2019)


Install GIS related packages with conda (and pip) by running in command prompt following commands (in the same order as they are listed).
Make sure you are in the correct enviroment (don't install into ``base``, install new packages ideally only into your designated created environments)

.. code::

    (C:\dev\conda3) activate geopy2019

    (geopy2019) conda install -c pyviz -c conda-forge numpy pandas gdal fiona shapely geopandas geoviews

    # Install matplotlib
    (geopy2019) conda install -c pyviz -c conda-forge install matplotlib

    # Install scipy
    (geopy2019) conda install -c pyviz -c conda-forge install scipy

    #Install Jupyter Notebook
    (geopy2019) conda install -c pyviz -c conda-forge install jupyter

    # Install rasterio and rasterstats
    (geopy2019) conda install -c pyviz -c conda-forge install rasterio rasterstats

    # Install seaborn
    (geopy2019) conda install -c pyviz -c conda-forge install seaborn

    # Install geoplot and cartopy
    (geopy2019) conda install -c pyviz -c conda-forge install geoplot cartopy

    # Install pysal and mapclassify
    (geopy2019) conda install -c pyviz -c conda-forge install pysal mapclassify

    # Install bokeh
    (geopy2019) conda install -c pyviz -c conda-forge install bokeh

    # Install Folium
    (geopy2019) conda install -c pyviz -c conda-forge folium


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


Test that everything works
~~~~~~~~~~~~~~~~~~~~~~~~~~

You can test that the installations have worked by running following commands in a Python console.
At first start the Python console:

.. code::

    (geopy2019) python

    Type "help", "copyright", "credits" or "license" for more information.
    >>>

.. code:: python

     import numpy as np
     import pandas as pd
     import matplotlib.pyplot as plt
     import seaborn
     import scipy
     import shapely
     import gdal
     import fiona
     import shapely
     import geopandas as gpd
     import pysal
     import bokeh
     import cartopy
     import mapclassify
     import geoviews
     import rasterstats
     import rasterio
     import geoplot
     import folium


If you don't receive any errors, everything should be working!

To exit a Python console:

.. code::

    (geopy2019) >>> exit()


Recap, setting up your project folder and Jupyter Notebook
----------------------------------------------------------

You need to organise your files and scripts in a folder, that you find again, is easy to navigate to, and sits on a hard drive on your computer.

On Windows you have your local user folder, typically ``C:\Users\Alexander``. Open with the Windows File Explorer and check that you have created a new folder here with the name ``geopython2019``.

If you don't have the Anaconda Prompt open, please open it. ``Anaconda Prompt`` can be found by clicking on the Windows start menu button and start typing ``Anaconda Prompt``.
Then always activate your correct Python environment

.. code::

    (C:\dev\conda3)  activate geopy2019

    (geopy2019)

As this is still the "normal" Windows command line, you can navigate through the folders. Change your working directory of the Command line window to your "geopython" folder:

.. code::

    c:
    cd C:\Users\Alexander\geopython

You can see which files are inside this folder by using the ``dir`` command. (On Mac and Linux it is ``ls``) and it will print information and files of your current folder.

.. code::

    c:
    cd C:\Users\Alexander\geopython2019
    
    dir

    ... output below
    
    Volume in drive C is Windows
    Volume Serial Number is 5E4C-FED5
    
    Directory of C:\Users\Alexander\geopython2019
    
    29.10.2019  15:00    <DIR>          .
    29.10.2019  15:00    <DIR>          ..
    29.10.2019  08:51 AM            693 environment.yml


It is important to understand, that you are always "residing" somewhere in some folder. Therefore, make sure you navigate explicitly into your correct working folder "geopython2019".
This will in particular important to make sure that you find your Jupyter Notebooks and the working data, which ideally reside under the same directory hierarchy.

The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code,
equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling,
data visualization, machine learning, and much more.

Before we start Python coding we will make this newly created conda Python environment known to the Jupyter notebook system by installing the kernel, basically the execution engine link from Jupyter web notebook to our Python environment:
Make sure the ``geopy2019`` conda environment is activated:

.. code::

    (C:\dev\conda3)  activate geopy2019

    (geopy2019) python -m ipykernel install --user --name geopy2019

That should be it. You should now be able to start the Jupyter notebook server:

.. code::

    (geopy2019) python -m ipykernel install --user --name geopy2019

This should open a webpage in your default webbrowser. we'll take it from there in the next section.


Final Remarks
~~~~~~~~~~~~~



We saw that in some installations importing of ``import matplotlib.pyplot as plt`` crashed the Python.
If that happens we had success in re-installing **matplotlib** again: ``conda install matplotlib``.

Furthermore, a warning can appear, that a package (mkl-random) might require "cython" and complain that it is not installed. So far we can ignore that.

Also, a warning occured in some instances that ``pip`` was in an older version (9.x) and it was recommended to upgrade pip to a newer version (10.x). The warning shows the command to update pip in this conda environment.

In order to close the Python interpreter type ``exit()`` or press **Ctrl+Z** plus Return to exit.
