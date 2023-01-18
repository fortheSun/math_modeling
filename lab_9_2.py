import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.1)

def factory_func(v, t):
    dn_dt = -k * v * t
    return dn_dt
plt.grid()

v_0 = 1000
k = 0.08

v_t = odeint(factory_func, v_0, t)

plt.plot(t, v_t[:,0])
plt.savefig("factory.png")