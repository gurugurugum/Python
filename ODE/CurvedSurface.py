import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
from sympy import *

xu=[Symbol('x'+str(i)) for i in range(2)]

gll=[[4*xu[0]**2 + 1, 4*xu[0]*xu[1]], [4*xu[0]*xu[1], 4*xu[1]**2 + 1]]

guu=Matrix(gll).inv().tolist()

Gammalll=[[[Rational(1,2)*(gll[i][k].diff(xu[j])+gll[i][j].diff(xu[k])-gll[j][k].diff(xu[i])) for k in range(2)] for j in range(2)] for i in range(2)]

Gammaull=[[[sum([guu[i][d]*Gammalll[d][j][k] for d in range(2)]) for k in range(2)] for j in range(2)] for i in range(2)]

def func(y, t):
	return [-sum([sum([Gammaull[0][i][j].subs(xu[0], y[2]).subs(xu[1], y[3])*y[i]*y[j] for i in range(2)]) for j in range(2)]), -sum([sum([Gammaull[1][i][j].subs(xu[0], y[2]).subs(xu[1], y[3])*y[i]*y[j] for i in range(2)]) for j in range(2)]), y[0], y[1]]

x0=[1, 0]
theta0=math.pi*1/2
v0=[math.cos(theta0), math.sin(theta0)]
mag=sum([sum([gll[d1][d2].subs(xu[0], x0[0]).subs(xu[1], x0[1])*v0[d1]*v0[d2] for d1 in range(2)]) for d2 in range(2)])
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
	print(sum([sum([gll[d1][d2].subs(xu[0], traj[i][2]).subs(xu[1], traj[i][3])*traj[i][d1]*traj[i][d2] for d1 in range(2)]) for d2 in range(2)]))
