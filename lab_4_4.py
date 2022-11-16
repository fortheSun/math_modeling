import numpy as np

def y(a, b, N):
  x = np.linspace(a,b, N)
  return x ** 2
print(y(-10, 10, 100))