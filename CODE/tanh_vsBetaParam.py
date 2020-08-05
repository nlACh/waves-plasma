# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 20:23:16 2020
"""
"""
@author: nlpl9
Plot the value of the function as beta is varied
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
#beta=5.42
H=1
p = 3/(V0 - u0)**4 + ((delta**2)/12)/(V0 - u0)**3 + 1/(2*(V0 - u0)**3)
q = eta/2
t = 1 # Fix the time

# Define the solution you wish to use... and vectorize it
def r(b):
    r = delta*H**2/(8*b) + 0.5*(V0-u0)**3 + ((H**2)/8)/(V0 - u0)
    return r

@np.vectorize
def g(x, beta):
    R = r(beta)
    g = m.sqrt(6*R/p)*(1 + m.tanh(x - 8*R*t))
    return g


x = np.linspace(-10, 10, 200)
beta = np.linspace(0.2, 6, 100)

X,B = np.meshgrid(x, beta)
Z = g(X, B)

fig = plt.figure()
ax = plt.gca(projection="3d")

ax.set_xlabel('x')
ax.set_ylabel(r'$\beta$')
ax.set_zlabel(r'$\phi(x,t)$')
surf = ax.plot_surface(X, B, Z, rstride=1, cstride=1, cmap='gnuplot2')
fake2Dline = mpl.lines.Line2D([0],[0], linestyle="none", c='b', marker = 'o')
plt.legend([fake2Dline], ['u0=.5, V0=1.2, delta=.1, eta=.1, H=1'], numpoints = 1)
ax.view_init(20, 120)
plt.savefig('C:\\Users\\nlpl9\\Desktop\\plasma-proj\\Graphs\\tanh_phivsBeta.jpg', transperant=True, dpi=144)
plt.show()