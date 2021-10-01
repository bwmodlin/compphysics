import numpy as np
import matplotlib.pyplot as plt
import h5py
# import the right axis class to give us the 3D option
from mpl_toolkits.mplot3d import Axes3D


# create a 3D axis object
ax = plt.gcf().add_subplot(111, projection='3d')
# make a plot of a trajectory given x, y, and z arrays as a function of time
ax.plot(xarray, yarray, zarray, )
