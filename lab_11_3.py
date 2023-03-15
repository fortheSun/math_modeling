import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 500
t = np.arange(0, 5, frames)

def gruz_negr(sys, t):
    y, vy = sys
    dy_dt = vy
    dvy_dt = - k / m * y - g
    return dy_dt, dvy_dt

F0 = 1
g = 9.8
m = 0.5
delta_x = 0.08
k = F0 / delta_x


y0 = - delta_x
vy0 = 0.5
sys0 = y0, vy0

solve = odeint(gruz_negr, sys0, t)

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color = 'b')
ball_line, = plt.plot([], [], '-', color = 'b')

coord_x = np.zeros(frames)

def animate(i):
    ball.set_data(coord_x[i], solve[i, 0])
    ball_line.set_data(coord_x[:i], solve[:i, 0])

ax.set_xlim(-1, 1)
ax.set_ylim(-5, 0)

animation = FuncAnimation( 
                         fig,
                         animate, 
                         frames = frames, 
                         interval=30
                         )

animation.save("lab_11_3.gif")