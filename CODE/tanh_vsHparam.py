# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:39:25 2020
"""
"""
@author: nlpl9
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math as m

# Plasma parameters
#u0 = [0.2, 0.4, 0.7]
#V0 = [0.8, 1.0, 1.2]
#delta = [0.1, 0.3, 0.5, 0.7]
#eta = [0.5, 1.0, 2.5]
#beta = [0.33, 2.618, 5.42 ]
#H = [1,2,3]
# Define the functions for the diff eq. params...

u0=0.5
V0=1.2
delta=0.1
eta=1
beta=5.42

p = 3/(V0 - u0)**4 + ((delta**2)/12)/(V0 - u0)**3 + 1/(2*(V0 - u0)**3)
q = eta/2
t = 1 # Fix the time

# Define the solution you wish to use... and vectorize it
def r(H):
    r = delta*H**2/(8*beta) + 0.5*(V0-u0)**3 + (H**2)/(8*(V0-u0))
    return r

@np.vectorize
def g(x,H):
    g = m.sqrt(6*r(H)/p)*(1 + m.tanh(x - 8*r(H)*t))
    return g

x = np.linspace(0,10, 200)
h = np.linspace(1,3, 100)
X,H = np.meshgrid(x, h)
Z = g(X, H)

fig = plt.figure()
ax = plt.gca(projection="3d")
ax.set_xlabel('x')
ax.set_ylabel('H')
ax.set_zlabel(r'$\phi(x,t)$')
surf = ax.plot_surface(X, H, Z, rstride=1, cstride=1, cmap='gnuplot2')
fake2Dline = mpl.lines.Line2D([0],[0], linestyle="none", c='b', marker = 'o')
plt.legend([fake2Dline], [r'$u_0$=.5, $V_0$=1.2, $\delta$=0.1, $\beta$=5.42'], numpoints = 1)
ax.view_init(20, 210)
plt.savefig('C:\\Users\\nlpl9\\Desktop\\plasma-proj\\Graphs\\tanh_phivsH.jpg', transperant=True, dpi=144)
plt.show()