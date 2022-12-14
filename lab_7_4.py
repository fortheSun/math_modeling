import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
frakt, = plt.plot([], [], 'o', color='b')

plt.axis('equal')

frames = 100
x0 = 0.1
y0 = 0.1
c = 0.3
d = 0.33
edge = 1

x = []
y = []

for i in range(frames):
    xn = x0 ** 2 - y0 ** 2 + c
    yn = 2 * x0 * y0 + d

    x.append(xn)
    y.append(yn)

    x0 = xn
    y0 = yn


ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)


def animate(i):
    frakt.set_data(x[:i], y[:i])

ani = FuncAnimation(fig, animate, frames = frames, interval = 30)
ani.save('lab_7_4.gif')

