import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-5, 5, 0.1)

def diff_func(c, t):
    x, y, z = c
    dx_dx = 3*x - y + z
    dy_dx = x + y + z
    dz_dx = 4*x - y + 4*z
    return dx_dx, dy_dx, dz_dx

x = 600
x0 = -71
y0 = 1
z0 = -3

c0 = y0, x0, z0

sol = odeint(diff_func, c0, t)

plt.plot(t, sol[:, 0], t, sol[:, 1], t, sol[:, 2])

plt.savefig('diff_func3.png')