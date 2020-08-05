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

V0=1.2
delta=0.1
eta=1
beta=5.42
H=1

q = eta/2
t = 1 # Fix the time

# Define the solution you wish to use... and vectorize it
def r(u):
    r = delta*H**2/(8*beta) + 0.5*(V0-u)**3 + ((H**2)/8)/(V0 - u)
    return r

def p(u):
    p = 3/(V0 - u)**4 + ((delta**2)/12)/(V0 - u)**3 + 1/(2*(V0 - u)**3)
    return p

@np.vectorize
def g(x,U0):
    g = m.sqrt(6*r(U0)/p(U0))*(1 + m.tanh(x - 8*r(U0)*t))
    return g


x = np.linspace(-10,50, 100)
u = np.linspace(0.1,0.7, 100)
X,U0 = np.meshgrid(x, u)
Z = g(X, U0)

fig = plt.figure()
ax = plt.gca(projection="3d")
ax.set_xlabel('x')
ax.set_ylabel('$u_0$')
ax.set_zlabel(r'$\phi(x,t)$')
surf = ax.plot_surface(X, U0, Z, rstride=1, cstride=1, cmap='gnuplot2')
fake2Dline = mpl.lines.Line2D([0],[0], linestyle="none", c='b', marker = 'o')
plt.legend([fake2Dline], [r'$V_0$=1.2, $\delta$=0.1, H=1, $\beta$=5.42'], numpoints = 1)
ax.view_init(20, 120)
plt.savefig('C:\\Users\\nlpl9\\Desktop\\plasma-proj\\Graphs\\tanh_phivsU0.jpg', transperant=True, dpi=144)
plt.show()