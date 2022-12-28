import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')

def circle_move(R, k, time):
    R = k * time
    alpha = np.arange(0, 2* np.pi, 0.1)
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    return x, y

edge = 100
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    ball.set_data(circle_move(R=0.5, k=1, time=i))

ani = FuncAnimation(fig, animate, frames = 100, interval = 30)

ani.save('lec_7_2.gif')