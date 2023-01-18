import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 3, 0.1)

def bacteria_func(n, t):
    dn_dt = n * k
    return dn_dt
plt.grid()

n_0 = 10
k = 1

n_t = odeint(bacteria_func, n_0, t)

plt.plot(t, n_t[:,0])
plt.savefig("bacteria.png")