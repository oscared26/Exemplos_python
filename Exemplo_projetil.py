import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from sympy import *

from matplotlib.animation import FuncAnimation
import math

g=9.8
vo=40
yo=0
xo=0
angle=math.radians(45)

t= symbols("t")
eq1=yo + vo*math.sin(angle)*t -0.5*g*t**2
eq2=diff(eq1, t)
eq3=diff(eq2, t)

eq4=xo+vo*cos(angle)*t


f = sym.lambdify(t,eq1)         # Creates a python function f(x)
g = sym.lambdify(t,eq2)         # Creates a python function g(x)
h = sym.lambdify(t,eq3)         # Creates a python function h(x)
k = sym.lambdify(t,eq4)         # Creates a python function h(x)


# create a figure with an axes
fig, ax = plt.subplots()
# set the axes limits
ax.axis([0,200,0,50])


xx = np.linspace(0,20,360) # xx so that it doesn't collide with symbolic x
yy1=f(xx)
yy2=k(xx)
#y3=h(xx)



# create a point in the axes
point, = ax.plot(0, 0, marker="o",markersize=15)
line, = ax.plot(yy2,yy1, 'r-', linewidth=1)
ax.grid()



#print(point.set_data(xx[0],y1[0]))

def update(i):
  y1=f(i)
  y2=k(i)
  point.set_data([y2],[y1])
  return point,

# create animation with 10ms interval, which is repeated,
# provide the full circle (0,2pi) as parameters
ani = FuncAnimation(fig, update, interval=10, blit=True, repeat=True,
                    frames=np.linspace(0,20,360, endpoint=False))

plt.show()

    
