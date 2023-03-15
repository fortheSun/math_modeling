import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 5, frames)

def move_func(c, t):
    v_y, y0 = c
    dy_dt = v_y
    dvy_dt = -g - u * v_y
    return dy_dt, dvy_dt

g = 9.8
v_y0 = 20
u = 0.1
y0 = 0
c_0 = v_y0, y0

solvers = odeint(move_func, c_0, t)
plt.plot(t, solvers[:, 0])
plt.savefig("lab_11_1.png")

#def solve_func(i, key):
#    sol = odeint(move_func, c_0, t)
#    if key == 'point':
#        x = sol[i, 0]
#        y = sol[i, 2]
#    else:
#        x = sol[:i, 0]
#        y = sol[:i, 2]
#    return x, y

#fig, ax = plt.subplots()

#ball, = plt.plot([], [], 'o', color = 'r')
#ball_line, = plt.plot([], [], '-', color = 'r')

#def animate(i):
#    ball.set_data(solve_func(i, 'point'))
#   ball_line.set_data(solve_func(i, 'line'))
#ani = FuncAnimation(fig,
#                    animate,
#                   frames = frames,
#                    interval = 30
#                    )
#
#edge = 10
#ax.set_xlim(0, edge)
#ax.set_ylim(0, edge)

#ani.save('lab11_1.gif')