Exercise 3 hints
================

Problem 1
---------

- when renaming columns, either do it *inplace*, meeaning changing the dataframe immediately, or assign the dataframe with the changed column names to a variable:

.. code::

    # compare and see in the raster lecture
    demstats_df.rename(columns={'mean':'dem_mean','std':'dem_std'}, inplace=True)
    # or reassign, without using the 'inplace' keyword
    demstats = demstats_df.rename(columns={'mean':'dem_mean','std':'dem_std'})


- plotting the scale while ignoring the nodata values can be achieved with the vmin and vmax keywords for the plot functions. Check the histogram which values to consider for vmin and vmax. 

- you can very easily plot a histogram from Pandas or Geopandas dataframe in th esame way, how to plot graphs or maps:

.. code::

    fig, (ax_map, ax_hist) = plt.subplots(1, 2, figsize=(13,8))
    geo_df.plot(ax=ax_map, column="col_a", cmap="viridis", legend=True)
    geo_df.hist(ax=ax_hist, column="col_a")
    plt.title("a title for col_a")
    plt.show()


- see `Pandas documentation on historgram <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.hist.html>`_



Problem 2
---------

- Documentation of the Travel Time Matrix dataset and explanation for different column names can be found at the Accessibility Research Group website: `Helsinki Region Travel Time Matrix 2015 <http://blogs.helsinki.fi/accessibility/helsinki-region-travel-time-matrix-2015>`__


- Note that the input travel time data is stored in text files when reading in the data.
- Keep columns `'from_id'`,`'to_id'`,`'pt_r_tt'` and `'car_r_t'` in the travel time data files
- Join the data using columns `'from_id'` from the travel time data, and `'YKR_ID'` in the grid-shapefile
- See hints for joining the travel time data to the grid shapefile from our earlier materials from the lesson regarding classifying the bogs via the landuse legend file.
- Plotting the data might take a while (be patient!)

