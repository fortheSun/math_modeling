import matplotlib.pyplot as plt
import numpy as np

def figure(A = 3, B = 3, a = I, b = B):

    t = np.arange(-10, 11, 0.0001)

    x = (A * (np.sin(a * t + (np.pi / 2))))
    y = (B * (np.sin(b * t)))

    plt.plot(x, y)
    plt.grid()
    plt.savefig('lab_6_dop1.png')

    figure()
