import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t = np.arange(0, 100, 0.1)
g = 9.8

def kuvshinka_func(S, t):
    dS_dt = k * R * 
    return dS_dt



plt.grid()

S_0 = 1600
k = 1360.8

S_t = odeint(kuvshinka_func, S_0, t)

plt.plot(t, S_t[:,0])
plt.savefig("tochka.png")