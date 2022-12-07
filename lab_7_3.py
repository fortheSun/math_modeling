import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')

def babochka():
    t = np.arange(0, 12 * np.pi, 0.01)
    x = np.sin(t) * (np.exp ** np.cos(t) - 2 * np.cos(4 * t) + np.sin(t / 12) ** 5)
    y = np.cos(t) * (np.exp ** np.cos(t) - 2 * np.cos(4 * t) + np.sin(t / 12) ** 5)
    return x, y

edge = 10000
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate():
    ball.set_data(babochka())

ani = FuncAnimation(fig, animate, frames = 100, interval = 30)

ani.save('lec_7_animation.gif')