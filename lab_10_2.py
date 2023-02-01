import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.01)

def diff_func(c, t):
    x, y = c
    dy_dx = 3*x - 2*y + np.exp(3*t) / np.exp(t) + 1
    dz_dx = x - np.exp(3*t) / np.exp(t) + 1
    return dy_dx, dz_dx

x = 600
x0 = 5
y0 = -7

c0 = y0, x0 

sol = odeint(diff_func, c0, t)

plt.plot(t, sol[:, 0])

plt.savefig('diff_func01.png')