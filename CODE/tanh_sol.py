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

u0=0.5
V0=1.2
delta=0.3
eta=0.5
beta=5.42
H=1.4

p = 3/(V0 - u0)**4 + ((delta**2)/12)/(V0 - u0)**3 + 1/(2*(V0 - u0)**3)
q = eta/2
r = delta*H**2/(8*beta) + 0.5*(V0-u0)**3 + ((H**2)/8)/(V0 - u0)
@np.vectorize
def f(x,t):
    f = m.sqrt(6*r/p)*(1 + m.tanh(x - 8*r*t))
    return f

# Define some time and space interval preferably a 200 by 200 grid with 200*2 samples..
# (I love my computer...) otherwise use N**2 grid sampling.
x = np.linspace(60, 140, 200)
t = np.linspace(20, 30, 100)

#p = np.zeros((200, 100), dtype=float)
"""
for i in range(0,100):
    # Iterating time values
    for j in range(0,200):
        # Iterating through spatial values..
        p[j][i] = f(x[j], t[i])
"""

X,T = np.meshgrid(x, t)
Z = f(X, T)

fig = plt.figure()
ax = plt.gca(projection="3d")
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel(r'$\phi(x,t)$')
fake2Dline = mpl.lines.Line2D([0],[0], linestyle="none", c='b', marker = 'o')
plt.legend([fake2Dline], [r'$u_0$=0.5, $V_0$=1.2, $\delta$=0.3, H=1.4, $\beta$=5.42, $\eta$=0.5'], numpoints = 1)
surf = ax.plot_surface(X, T, Z, rstride=1, cstride=1, cmap='gnuplot2', alpha=1.0)
ax.view_init(20, 220)
plt.savefig('C:\\Users\\nlpl9\\Desktop\\plasma-proj\\Graphs\\tanh_t20--30.jpg', dpi=144)
plt.show()