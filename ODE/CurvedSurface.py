import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
from sympy import *

x, y=symbols('x y')

gll=[[4*x**2 + 1, 4*x*y], [4*x*y, 4*y**2 + 1]]

def Gammaull(x, y):
	return [[[-16*x*y**2/(4*x**2 + 4*y**2 + 1) + 4*x*(16*x**2*y**2/((4*x**2 + 1)*(4*x**2 + 4*y**2 + 1)) + 1/(4*x**2 + 1)), 0], [0, -16*x*y**2/(4*x**2 + 4*y**2 + 1) + 4*x*(16*x**2*y**2/((4*x**2 + 1)*(4*x**2 + 4*y**2 + 1)) + 1/(4*x**2 + 1))]], [[-16*x**2*y/(4*x**2 + 4*y**2 + 1) + 4*y*(4*x**2 + 1)/(4*x**2 + 4*y**2 + 1), 0], [0, -16*x**2*y/(4*x**2 + 4*y**2 + 1) + 4*y*(4*x**2 + 1)/(4*x**2 + 4*y**2 + 1)]]]

def func(y, t):
	return [-sum([sum([Gammaull(y[2], y[3])[0][i][j]*y[i]*y[j] for i in range(2)]) for j in range(2)]), -sum([sum([Gammaull(y[2], y[3])[1][i][j]*y[i]*y[j] for i in range(2)]) for j in range(2)]), y[0], y[1]]

x0=[1, 0]
theta0=math.pi*3/2
v0=[math.cos(theta0), math.sin(theta0)]
mag=sum([sum([gll[d1][d2].subs(x, x0[0]).subs(y, x0[1])*v0[d1]*v0[d2] for d1 in range(2)]) for d2 in range(2)])
v0=list(map(lambda n:n/math.sqrt(mag), v0))

y0 = [v0[0], v0[1], x0[0], x0[1]]
t = np.arange(0, 100, 0.01)

traj = odeint(func, y0, t)

z=(traj[:, 2])**2 + (traj[:, 3])**2

fig = plt.figure()
#ax = fig.gca(projection='3d')
#ax.plot(traj[:, 2], traj[:, 3], z[:])
plt.plot(traj[:, 2], traj[:, 3])
plt.show()

for i in range(0, 10000, 100):
	print(sum([sum([gll[d1][d2].subs(x, traj[i][2]).subs(y, traj[i][3])*traj[i][d1]*traj[i][d2] for d1 in range(2)]) for d2 in range(2)]))
