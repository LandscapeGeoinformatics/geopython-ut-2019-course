Exercise 3 hints
================

Problem 1
---------


demstats_df.rename(columns={'mean':'dem_mean','std':'dem_std'}, inplace=True)


fig, (ax1, ax2) = plt.subplot(1, 2)
geoplot(ax1)
histplot(ax2)
title
plt.show


Problem 2
---------

- Documentation of the Travel Time Matrix dataset and explanation for different column names can be found at the Accessibility Research Group website: `Helsinki Region Travel Time Matrix 2015 <http://blogs.helsinki.fi/accessibility/helsinki-region-travel-time-matrix-2015>`__


- Note that the input travel time data is stored in text files when reading in the data.
- Keep columns `'from_id'`,`'to_id'`,`'pt_r_tt'` and `'car_r_t'` in the travel time data files
- Join the data using columns `'from_id'` from the travel time data, and `'YKR_ID'` in the grid-shapefile
- See hints for joining the travel time data to the grid shapefile from our earlier materials from the lesson regarding classifying the bogs via the landuse legend file.
- Plotting the data might take a while (be patient!)

