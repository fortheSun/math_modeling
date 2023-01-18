import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t = np.arange(0, 100, 0.1)
v = 50
b = 10
g = 9.8

def tochka_func(v, t):
    dv_dt = (b - k * t) / m 
    return dv_dt



plt.grid()

v_0 = 50
k = 0.5

v_t = odeint(tochka_func, v_0, t)

plt.plot(t, v_t[:,0])
plt.savefig("tochka.png")