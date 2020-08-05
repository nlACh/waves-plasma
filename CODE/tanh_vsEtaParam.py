# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 21:08:47 2020

@author: nlpl9
Variation of the solution with delta parameter...
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
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
#delta=0.1
eta=1
beta=5.42
H=1

#p = 3/(V0 - u0)**4 + ((delta**2)/12)/(V0 - u0)**3 + 1/(2*(V0 - u0)**3)
q = eta/2
#r = delta*H**2/(8*beta) + 0.5*(V0-u0)**3 + ((H**2)/8)/(V0 - u0)
t = 1 # Fix the time

# Define the solution you wish to use... and vectorize it
def r(d):
    r = d*H**2/(8*beta) + 0.5*(V0-u0)**3 + ((H**2)/8)/(V0 - u0)
    return r

def p(d):
    p = 3/(V0 - u0)**4 + ((d**2)/12)/(V0 - u0)**3 + 1/(2*(V0 - u0)**3)
    return p

@np.vectorize
def g(x,D):
    R = r(D)
    P = p(D)
    g = m.sqrt(6*R/P)*(1 + m.tanh(x))# - 8*R*t))
    return g

# Define some time and space interval preferably a 200 by 200 grid with 200*2 samples..
# (I love my computer...) otherwise use N**2 grid sampling.
x = np.linspace(-10, 10, 200)
#t = np.linspace(5,60, 400)
d = np.linspace(0.1, 0.7, 200)

#p = np.zeros((200, 100), dtype=float)
"""
for i in range(0,100):
    # Iterating time values
    for j in range(0,200):
        # Iterating through spatial values..
        p[j][i] = f(x[j], t[i])
"""

X,D = np.meshgrid(x, d)
Z = g(X, D)

fig = plt.figure()
#ax = plt.gca(projection="3d")
#ax.plot_wireframe(X, T, Z, color='green')
#ax.set_xlabel('x')
#ax.set_ylabel(r'$\delta$')
#ax.set_zlabel(r'$\phi(x,t)$')
#surf = ax.plot_surface(X, D, Z, rstride=1, cstride=1)
fake2Dline = mpl.lines.Line2D([0],[0], linestyle="none", c='b', marker = 'o')
plt.legend([fake2Dline], ['u0=.5, V0=1.2, delta=.1, eta=.5, beta=5.42'], numpoints = 1)
#ax.set_title(r'$\sqrt{\frac{6r}{p}}(1+tanh(x-8rt))$')
#ax.view_init(30, 220)
#fig.colorbar(surf, shrink=0.5)
plt.savefig('C:\\Users\\nlpl9\\Desktop\\plasma-proj\\Graphs\\tanh_phivsH_legend', transperant=True, dpi=144)
plt.show()

