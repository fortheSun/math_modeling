import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 365
seconds_in_year = 365 * 24 * 60 * 60
years = 4
t = np.linspace(0, seconds_in_year, frames)

def move_func(s, t):
    (xearth, v_xearth, yearth,  v_yearth,
    xmerc, v_xmerc, ymerc, v_ymerc,
    xven, v_xven, yven,  v_yven,
    xmars, v_xmars, ymars, v_ymars,
    xfae, v_xfae, yfae, v_yfae) = s

    dxdtearth = v_xearth
    dv_xdtearth = - G * m * xearth / (xearth ** 2 + yearth ** 2) ** 1.5
    dydtearth = v_yearth
    dv_ydtearth = -G * m * yearth / (xearth ** 2 + yearth ** 2) ** 1.5

    dxdtmerc = v_xmerc
    dv_xdtmerc = - G * m * xmerc / (xmerc ** 2 + ymerc ** 2) ** 1.5
    dydtmerc = v_ymerc
    dv_ydtmerc = -G * m * ymerc / (xmerc ** 2 + ymerc ** 2) ** 1.5

    dxdtven = v_xven
    dv_xdtven = - G * m * xven / (xven ** 2 + yven ** 2) ** 1.5
    dydtven = v_yven
    dv_ydtven = -G * m * yven / (xven ** 2 + yven ** 2) ** 1.5

    dxdtmars = v_xmars
    dv_xdtmars = - G * m * xmars / (xmars ** 2 + ymars ** 2) ** 1.5
    dydtmars = v_ymars
    dv_ydtmars = -G * m * ymars / (xmars ** 2 + ymars ** 2) ** 1.5

    dxdtfae = v_xfae
    dv_xdtfae = - G * m * xfae / (xfae ** 2 + yfae ** 2) ** 1.5
    dydtfae = v_yfae
    dv_ydtfae = - G * m * yfae / (xfae ** 2 + yfae ** 2) ** 1.5
    return (dxdtearth, dv_xdtearth, dydtearth, dv_ydtearth,
            dxdtmerc, dv_xdtmerc, dydtmerc, dv_ydtmerc,
            dxdtven, dv_xdtven, dydtven, dv_ydtven,
            dxdtmars, dv_xdtmars, dydtmars, dv_ydtmars,
            dxdtfae, dv_xdtfae, dydtfae, dv_ydtfae)

G = 6.67 * 10 **(-11)
m = 1.98 * 10 **(30)
v_q = G * m * (2 / 20.929 * 10**9 - 1 / 190 * 10**9)

xearth0 = 149 * 10 ** 9
v_xearth0 = 0
yearth0 = 0
v_yearth0 = 30000

xmerc0 = 0
v_xmerc0 = -47360
ymerc0 = 0.387 * 149 * 10 ** 9
v_ymerc0 = 0

xven0 = -0.723332 * 149 * 10**9
v_xven0 = 0
yven0 = 0
v_yven0 = 35020

xmars0 = 0
v_xmars0 = -24077
ymars0 = 1.523662 * 149 * 10**9
v_ymars0 = 0

xfae0 = 190 * 149 * 10**9
v_xfae0 = 0
yfae0 = 0
v_yfae0 = v_q


s0 = (xearth0, v_xearth0, yearth0, v_yearth0,
       xmerc0, v_xmerc0, ymerc0, v_ymerc0,
       xven0, v_xven0, yven0, v_yven0,
       xmars0, v_xmars0, ymars0, v_ymars0,
       xfae0, v_xfae0, yfae0, v_yfae0)

sol = odeint(move_func, s0, t)
def solve_func(i, key):
    if key == 'point':
        xearth = sol[i, 0]
        yearth = sol[i, 2]
        xmerc = sol[i, 4]
        ymerc = sol[i, 6]
        xven = sol[i, 8]
        yven = sol[i, 10]
        xmars = sol[i, 12]
        ymars = sol[i, 14]
        xfae = sol[i, 16]
        yfae = sol[i, 18]
    else:
        xearth = sol[:i, 0]
        yearth = sol[:i, 2]
        xmerc = sol[:i, 4]
        ymerc = sol[:i, 6]
        xven = sol[:i, 8]
        yven = sol[:i, 10]
        xmars = sol[:i, 12]
        ymars = sol[:i, 14]
        xfae = sol[:i, 16]
        yfae = sol[:i, 18]
    return ((xearth, yearth),
            (xmerc, ymerc),
            (xven, yven),
            (xmars, ymars),
            (xfae, yfae))

fig, ax = plt.subplots()

ball_earth, = plt.plot([], [], 'o', color = 'b')
ball_line_earth, = plt.plot([], [], '-', color = 'b')

ball_merc, = plt.plot([], [], 'o', color = 'r')
ball_line_merc, = plt.plot([], [], '-', color = 'r')

ball_ven, = plt.plot([], [], 'o', color = 'b')
ball_line_ven, = plt.plot([], [], '-', color = 'b')

ball_mars, = plt.plot([], [], 'o', color = 'r')
ball_line_mars, = plt.plot([], [], '-', color = 'r')

ball_fae, = plt.plot([], [], 'o', color = 'r')
ball_line_fae, = plt.plot([], [], '-', color = 'r')

plt.plot([0], [0], 'o', color = 'y', ms = 20)

def animate(i):
    ball_earth.set_data(solve_func(i, 'point')[0])
    ball_line_earth.set_data(solve_func(i, 'line')[0])

    ball_merc.set_data(solve_func(i, 'point')[1])
    ball_line_merc.set_data(solve_func(i, 'line')[1])

    ball_ven.set_data(solve_func(i, 'point')[2])
    ball_line_ven.set_data(solve_func(i, 'line')[2])

    ball_mars.set_data(solve_func(i, 'point')[3])
    ball_line_mars.set_data(solve_func(i, 'line')[3])

    ball_fae.set_data(solve_func(i, 'point')[4])
    ball_line_fae.set_data(solve_func(i, 'line')[4])

ani = FuncAnimation(fig,
                    animate,
                    frames = frames,
                    interval = 30)

plt.axis('equal')
edge = 2*xmars0
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('lab_12_1.gif')