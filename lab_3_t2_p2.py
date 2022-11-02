from lab_3_module1 import k
from lab_3_module1 import E
from lab_3_module1 import h
import numpy as np
T = 200
e = 300
H = 100

x1 = 2 / np.pi ** 0.5
x2 = (h / ((k * T) ** 3 / 2))
x3 = (E ** (-e / (k * T)))
x4 = (e ** (T / 2))

N = x1 * x2 * x3 * x4
print(N)