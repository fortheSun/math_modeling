import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from lab_3_module import G

fig, ax = plt.subplots()
arrow, = plt.plot([], [], '-', color='r')

def arrow_move(S, vx0, v0, vx, vy0, vy, time):
    alpha = np.arange(0, 2* np.pi, 0.1)
    vx0 = v0 * np.cos(alpha)
    vx = vx0
    x = vx0 * time
    vy0 = v0 * np.sin(alpha)
    vy = vy0 - G * time
    y = vy0 * time - G * time ** 2 /2
    return x, y

edge = 100
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    arrow.set_data(arrow_move(S=50, vx0=5, v0=0, vx=3, vy0=10, vy = 6, time=i))

ani = FuncAnimation(fig, animate, frames = 100, interval = 30)

ani.save('myproject.gif')