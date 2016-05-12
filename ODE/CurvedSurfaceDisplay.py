import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
from sympy import *
from matplotlib import cm
import sys

fig = plt.figure()
ax = fig.gca(projection = '3d')
plt.hold(True)

x_surf=np.arange(-10, 10, 0.1)                # generate a mesh
y_surf=np.arange(-10, 10, 0.1)
x_surf, y_surf = np.meshgrid(x_surf, y_surf)
#z_surf = x_surf ** 2 + y_surf ** 2             # ex. function, which depends on x and y
z_surf = ((x_surf - 5) ** 2 * (x_surf + 5) ** 2 + y_surf ** 4) / 5 ** 4
ax.plot_surface(x_surf, y_surf, z_surf, cmap=cm.hot);    # plot a 3d surface plot

plt.show()
