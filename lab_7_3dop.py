import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
star, = plt.plot([], [], '.', color='b')
plt.axis('equal')

t = np.arange(0, 4 * np.pi, 0.01)

def starlol():
    x = 12 * np.cos(t) + 8 * np.cos(1.5 * t)
    y = 12 * np.sin(t) - 8 * np.sin(1.5 * t)
    return x, y

def animate(i):
    x, y = starlol()
    X = x * np.cos(i) - y * np.sin(i)
    Y = y * np.cos(i) + x * np.sin(i)
    star.set_data(X, Y)
    return star,

ax.set_xlim(-35, 35)
ax.set_ylim(-35, 35)

ani = FuncAnimation(fig, animate, frames = 300, interval=100)
ani.save('lab_7_3dop.gif')