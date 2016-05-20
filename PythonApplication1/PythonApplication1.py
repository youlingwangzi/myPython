# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:24:01 2015

@author: 晓坤
"""

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
fig = plt. figure()
ax = fig. gca(projection='3d' )
X = np.arange(-500, 500, 10)
Y = np.arange(-500, 500, 10)
X, Y = np.meshgrid(X, Y)	

Z = (X * np.sin(np.sqrt(np.abs(X))));
Z = Z + (Y * np.sin(np.sqrt(np.abs(Y))));
Z = Z + 2*418.9826

surf = ax. plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.cool,
linewidth=0, antialiased=False)
ax. set_zlim(0, 1800)
fig. colorbar(surf, shrink=0.5, aspect=5)
plt.show()