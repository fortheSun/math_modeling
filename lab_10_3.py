import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-5, 5, 0.1)

def diff_func(c, t):
    x, y = c
    dy_dx = y
    dz_dx = np.sin(t) + np.cos(t) - y
    return dy_dx, dz_dx

x = 600
x0 = 0
y0 = 3

c0 = y0, x0 

sol = odeint(diff_func, c0, t)

plt.plot(t, sol[:, 1], sol[:, 0])

plt.savefig('diff_func10.png')