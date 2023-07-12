Assorted work/code used for various astro data reduction/processing

All work here can be used for future reference and be transferred across workstations

Data analysis:
- landolt.py (read in data from list of landolt standard stars and plot their magnitudes as a function of color and their RA/DEC positions)

CCD calibration:
- ccd_darkcurrent.py (plots/fits mean dark counts as a function of exposure time, calculate dark current)

List/array manipulation:
- listmax_remove.py (remove 2 largest values from list1 and associated values from list2 asuuming both are in same order)

Other:
- jupyterthemes.ipynb (set jupyter notebook to darkmode)
  - If there are issues displaying matplotlib plots, use command 'plt.style.use('default')' or 'plt.style.use('dark_background')' for improved visibility
