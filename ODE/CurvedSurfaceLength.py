import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
from sympy import *

xu = [Symbol('x' + str(i)) for i in range(2)]

z = sqrt(10000 - xu[0] ** 2 - xu[1] ** 2)

dxu = [Symbol('dx' + str(i)) for i in range(2)]
g = dxu[0] ** 2 + dxu[1] ** 2 + (z.diff(xu[0]) * dxu[0] + z.diff(xu[1]) * dxu[1]) ** 2
gll = [[Rational(1, 2) * g.diff(dxu[i]).diff(dxu[j]) for i in range(2)] for j in range(2)]
guu = Matrix(gll).inv().tolist()

Gammalll = [[[Rational(1,2) * (gll[i][k].diff(xu[j]) + gll[i][j].diff(xu[k]) - gll[j][k].diff(xu[i])) for k in range(2)] for j in range(2)] for i in range(2)]
Gammaull = [[[sum([guu[i][d] * Gammalll[d][j][k] for d in range(2)]) for k in range(2)] for j in range(2)] for i in range(2)]

def func(y, t):
	return [-sum([sum([Gammaull[0][i][j].subs(xu[0], y[2]).subs(xu[1], y[3]) * y[i] * y[j] for i in range(2)]) for j in range(2)]), -sum([sum([Gammaull[1][i][j].subs(xu[0], y[2]).subs(xu[1], y[3]) * y[i] * y[j] for i in range(2)]) for j in range(2)]), y[0], y[1]]

def euclidDistance3D(a, b):
	return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (z.subs(xu[0], a[0]).subs(xu[1], a[1]) - z.subs(xu[0], b[0]).subs(xu[1], b[1])) ** 2)

def firstMinimaOnTraj(goal, traj):
	beforeDistance = searchRange ** 2
	currentDistance = 0.0
	for	i in range(len(traj[:, 0])):
		currentDistance = euclidDistance3D(goal, traj[i, 2:])
		if currentDistance < beforeDistance:
			beforeDistance = currentDistance
		else:
			return [beforeDistance, i * step]
	return [-1, -1]

def unitVecOfDirection(theta):
	v0 = [math.cos(theta), math.sin(theta)]
	mag = sum([sum([gll[d1][d2].subs(xu[0], start[0]).subs(xu[1], start[1]) * v0[d1] * v0[d2] for d1 in range(2)]) for d2 in range(2)])
	return list(map(lambda n:n / math.sqrt(mag), v0))

searchRange = euclidDistance3D(start, goal) ** 2
step = 0.01
t = np.arange(0, searchRange, step)

start = [5, 0]
goal = [9, 1]
theta = math.atan2(goal[1] - start[1], goal[0] - start[0])

angleStep = 0.1
angleStepStep = 0.1
beforeDistance = searchRange ** 2
currentDistance = 0.0
result = 0.0
for i in range(int(70 / angleStep)):
	v0 = unitVecOfDirection(theta)
	y0 = v0 + start
	traj = odeint(func, y0, t)
	
	fMOT = firstMinimaOnTraj(goal, traj)
	currentDistance = fMOT[0]
	result = fMOT[1]
	if currentDistance < beforeDistance:
		beforeDistance = currentDistance
		theta += angleStep
	elif currentDistance - beforeDistance < step:
		break
	else:
		theta += -1 * angleStep
		angleStep *= angleStepStep
		theta += angleStep
print(result)

v0 = unitVecOfDirection(theta)
y0 = v0 + start
t = np.arange(0, result, step)
traj = odeint(func, y0, t)

height = [z.subs(xu[0], a).subs(xu[1], b) for a, b in zip(traj[:, 2], traj[:, 3])]
#height = list(map(lambda a, b:z.subs(xu[0], a).subs(xu[1], b), traj[:, 2], traj[:, 3]))
#height = list(map(lambda n:z.subs(xu[0], m), traj[:, 2]))
#height = list(map(lambda n:z.subs(xu[0], m), traj[:, 2]))
#height = z.subs(xu[0], traj[:, 2]).subs(xu[1], traj[:, 3])

fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.plot(traj[:, 2], traj[:, 3], height[:])
#plt.plot(traj[:, 2], traj[:, 3])
plt.show()

#for i in range(0, 10000, 100):
#	print(sum([sum([gll[d1][d2].subs(xu[0], traj[i][2]).subs(xu[1], traj[i][3]) * traj[i][d1] * traj[i][d2] for d1 in range(2)]) for d2 in range(2)]))
