import numpy as np
import matplotlib.pyplot as plt
import h5py
# import the right axis class to give us the 3D option
from mpl_toolkits.mplot3d import Axes3D

h5_file = h5py.File("test_ssx_particle_trajectory.h5", 'r')
position_array = h5_file['r'][()]

xarray, yarray, zarray = np.split(position_array, 3, 1)


# create a 3D axis object
ax = plt.gcf().add_subplot(111, projection='3d')
# make a plot of a trajectory given x, y, and z arrays as a function of time
ax.plot(xarray, yarray, zarray)

plt.show()
