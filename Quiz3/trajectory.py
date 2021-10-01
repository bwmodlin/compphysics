import numpy as np
import matplotlib.pyplot as plt
import h5py
# import the right axis class to give us the 3D option
from mpl_toolkits.mplot3d import Axes3D

h5_file = h5py.File("test_ssx_particle_trajectory.h5", 'r')
position_array = h5_file['r'][()]

xarray, yarray, zarray = np.split(position_array, 3, 1)
x1d = np.array([])
y1d = np.array([])
z1d = np.array([])
for i in range(10000):
    x1d = np.append(x1d, xarray[i][0])
    y1d = np.append(y1d, yarray[i][0])
    z1d = np.append(z1d, zarray[i][0])

h5_file.close()

# create a 3D axis object
ax = plt.gcf().add_subplot(111, projection='3d')
# make a plot of a trajectory given x, y, and z arrays as a function of time
ax.plot(x1d, y1d, z1d)

plt.show()
