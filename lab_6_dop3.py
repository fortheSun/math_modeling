import matplotlib.pyplot as plt
import numpy as np

def func(x, a, b):
    y = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] < a:
            y[i] = a ** 2
        elif a <= x[i] <= b:
            y[i] = x[i] ** 2
        else:
            y[i] = b ** 2
            return y


x = np.linspace(-10, 10, 1000)
y = func(x, -3, 5)

plt.plot(x, y)
plt.savefig("lab_6_dop3.png")