import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 365
seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, seconds_in_year, frames)

def move_func(s, t):
    (xearth, v_xearth, yearth,  v_yearth,
    xmerc, v_xmerc, ymerc, v_ymerc) = s
    dxdtearth = v_xearth
    dv_xdtearth = - G * m * xearth / (xearth ** 2 + yearth ** 2) ** 1.5
    dydtearth = v_yearth
    dv_ydtearth = -G * m * yearth / (xearth ** 2 + yearth ** 2) ** 1.5

    dxdtmerc = v_xmerc
    dv_xdtmerc = - G * m * xmerc / (xmerc ** 2 + ymerc ** 2) ** 1.5
    dydtmerc = v_ymerc
    dv_ydtmerc = -G * m * ymerc / (xmerc ** 2 + ymerc ** 2) ** 1.5
    return (dxdtearth, dv_xdtearth, dydtearth, dv_ydtearth,
            dxdtmerc, dv_xdtmerc, dydtmerc, dv_ydtmerc)

G = 6.67 * 10 **(-11)
m = 1.98 * 10 **(30)

xearth0 = 149 * 10 ** 9
v_xearth0 = 0
yearth0 = 0
v_yearth0 = 30000

xmerc0 = 0
v_xmerc0 = -47360
ymerc0 = 0.387 * 149 * 10 ** 9
v_ymerc0 = 0

s0 = (xearth0, v_xearth0, yearth0, v_yearth0,
       xmerc0, v_xmerc0, ymerc0, v_ymerc0)

sol = odeint(move_func, s0, t)
def solve_func(i, key):
    if key == 'point':
        xearth = sol[i, 0]
        yearth = sol[i, 2]
        xmerc = sol[i, 4]
        ymerc = sol[i, 6]
    else:
        xearth = sol[:i, 0]
        yearth = sol[:i, 2]
        xmerc = sol[:i, 4]
        ymerc = sol[:i, 6]
    return ((xearth, yearth),
            (xmerc, ymerc))

fig, ax = plt.subplots()

ball_earth, = plt.plot([], [], 'o', color = 'b')
ball_line_earth, = plt.plot([], [], '-', color = 'b')

ball_merc, = plt.plot([], [], 'o', color = 'r')
ball_line_merc, = plt.plot([], [], '-', color = 'r')

plt.plot([0], [0], 'o', color = 'y', ms = 20)

def animate(i):
    ball_earth.set_data(solve_func(i, 'point')[0])
    ball_line_earth.set_data(solve_func(i, 'line')[0])

    ball_merc.set_data(solve_func(i, 'point')[1])
    ball_line_merc.set_data(solve_func(i, 'line')[1])

ani = FuncAnimation(fig,
                    animate,
                    frames = frames,
                    interval = 30)

plt.axis('equal')
edge = 2*xearth0
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('merc_earth_sun.gif')