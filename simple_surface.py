#!/usr/bin/python2.7

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
z = 10 * np.random.rand(len(y))
print zip(x, y, z)

ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
        antialiased=False)

ax.scatter(x, y, z)

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

plt.show()
