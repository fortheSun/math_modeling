import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from lab_3_module import G


t = np.arange(0, 100, 0.1)
m = 5.9742 * (10**24)
h = 40000
v = 0.1
R = 6371000
M = 5.9722 * 10 ** 24
v_0 = 10
x = np.arange(0, h, 100)

def meteorite_func(v, x):
    dv_dr =  (G * M) / ((v * h + R - x) ** 2)
    return dv_dr

v_r = odeint(meteorite_func, v_0, x)
plt.plot(x, v_r[:,0])

plt.savefig('meteorite.png')