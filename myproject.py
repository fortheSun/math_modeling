import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
arrow, = plt.plot([], [], 'o', color='r')
arrow_ballistic, = plt.plot([],[], '-', color = 'r')

def arrow_move(v0, alpha, t):
    
    vx0 = v0 * np.cos(alpha*np.pi/180)
    vy0 = v0 * np.sin(alpha*np.pi/180)

    x = vx0 * t
    y = vy0 * t - 10 * (t ** 2 /2)

    return x, y

edge = 10
plt.axis('scaled')
ax.set_xlim(0, edge)
ax.set_ylim(0, 5)

xdata, ydata = [], []

def animate(i):
    x, y = arrow_move(10, 45, t=i)
    xdata.append(x)
    ydata.append(y)
    arrow_ballistic.set_data(xdata, ydata)
    arrow.set_data(arrow_move(10,  45, t=i))

ani = FuncAnimation(fig, animate, frames = np.arange(0, 40, 0.1), interval = 30)

ani.save('myproject.gif')