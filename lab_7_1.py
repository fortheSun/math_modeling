import numpy as np
import matplotlib.pyplot as plt

def cicloida(R):
    t = np.arange(-10, 10, 0.01)
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))

    plt.axis('equal')
    plt.plot(x, y)
    plt.savefig('lec_7_1.png')

cicloida(5)

def astroida(R):
    t = np.arange(-10, 10, 0.01)
    x = R * np.cos(t) ** 3
    y = R * np.sin(t) ** 3

    plt.axis('equal')
    plt.plot(x, y)
    plt.savefig('lec_7_1_astroida.png')


astroida(5)