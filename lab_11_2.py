import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 25, 0.01)

def move_func(c, t):
    x, y = c
    dx_dt = (A - x - y) * k1
    dy_dt = (A - x - y) * k2
    return dx_dt, dy_dt

A = 100
x = 0
y = 0
k1 = 0.15
k2 = 0.2

c_0 = x, y

sol = odeint(move_func, c_0, t)
plt.plot(t, sol[:, 0], t, sol[:, 1])
plt.savefig("lab_11_2.png")