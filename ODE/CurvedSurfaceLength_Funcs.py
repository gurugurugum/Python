import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
from sympy import *
from matplotlib import cm
import sys

xu = [Symbol('x' + str(i)) for i in range(2)]

#z = sqrt(10000 - xu[0] ** 2 - xu[1] ** 2)
z = ((xu[0] - 5) ** 2 * (xu[0] + 5) ** 2 + xu[1] ** 4) / 5 ** 4

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

def findNextLocalMinimumOnTraj(currentPosOnTraj, traj, goal):
	beforeDistance = float("inf")
	currentDistance = 0.0
	for	i in range(currentPosOnTraj, len(traj[:, 0])):
		currentDistance = euclidDistance3D(goal, traj[i, 2:])
		if currentDistance < beforeDistance:
			beforeDistance = currentDistance
		else:
			return [i - 1, beforeDistance]
	return [sys.maxsize, float("inf")]

def findNextLocalMaximumOnTraj(currentPosOnTraj, traj, goal):
	beforeDistance = -1.0
	currentDistance = 0.0
	for	i in range(currentPosOnTraj, len(traj[:, 0])):
		currentDistance = euclidDistance3D(goal, traj[i, 2:])
		#		print(currentDistance)
		if currentDistance >= beforeDistance:
			beforeDistance = currentDistance
		else:
			return [i - 1, beforeDistance]
	return [sys.maxsize, float("inf")]

def findNthLocalMinimumOnTraj(n, traj, goal):
	minimum = [0, 0]
	maximum = [0, 0]
	for i in range(n):
		minimum = findNextLocalMinimumOnTraj(maximum[0], traj, goal)
		maximum = findNextLocalMaximumOnTraj(minimum[0], traj, goal)
	return findNextLocalMinimumOnTraj(maximum[0], traj, goal)

def findAllLocalMinimaOnTraj(traj, goal):
	maximum = [0, 0]
	minimum = findNextLocalMinimumOnTraj(maximum[0], traj, goal)
	minima = [minimum]
	while minima[-1][1] < float("inf"):
		#	for i in range(5):
		print(minimum, traj[minimum[0], 2], traj[minimum[0], 3])
		maximum = findNextLocalMaximumOnTraj(minimum[0], traj, goal)
		if maximum[1] != float("inf"):
			print(maximum, traj[maximum[0], 2], traj[maximum[0], 3])
		minimum = findNextLocalMinimumOnTraj(maximum[0], traj, goal)
		minima.append(minimum)
	return minima[:-1]

def firstLocalMinimumOnTraj(goal, traj, step):
	beforeDistance = float("inf")
	currentDistance = 0.0
	for	i in range(len(traj[:, 0])):
		currentDistance = euclidDistance3D(goal, traj[i, 2:])
		if currentDistance < beforeDistance:
			beforeDistance = currentDistance
		else:
			return [beforeDistance, i * step]
	return [float("inf"), float("inf")]

def firstLocalMaximumOnTraj(goal, traj, step):
	beforeDistance = float("inf")
	currentDistance = 0.0
	pos = 0
	for	i in range(len(traj[:, 0])):
		currentDistance = euclidDistance3D(goal, traj[i, 2:])
		if currentDistance < beforeDistance:
			beforeDistance = currentDistance
		else:
			beforeDistance = currentDistance
			pos = i
			break
	for	i in range(pos + 1, len(traj[:, 0])):
		currentDistance = euclidDistance3D(goal, traj[i, 2:])
		if currentDistance >= beforeDistance:
			beforeDistance = currentDistance
		else:
			return [beforeDistance, i * step]
	return [float("inf"), float("inf")]

def secondLocalMinimumOnTraj(goal, traj, step):
	beforeDistance = float("inf")
	currentDistance = 0.0
	pos = 0
	for	i in range(len(traj[:, 0])):
		currentDistance = euclidDistance3D(goal, traj[i, 2:])
		if currentDistance < beforeDistance:
			beforeDistance = currentDistance
		else:
			beforeDistance = currentDistance
			pos = i
			break
	for	i in range(pos + 1, len(traj[:, 0])):
		currentDistance = euclidDistance3D(goal, traj[i, 2:])
		if currentDistance >= beforeDistance:
			beforeDistance = currentDistance
		else:
			beforeDistance = currentDistance
			pos = i
			break
	for	i in range(pos + 1, len(traj[:, 0])):
		currentDistance = euclidDistance3D(goal, traj[i, 2:])
		if currentDistance < beforeDistance:
			beforeDistance = currentDistance
		else:
			return [beforeDistance, i * step]
	return [float("inf"), float("inf")]

def unitVecOfDirection(theta, place):
	v0 = [math.cos(theta), math.sin(theta)]
	mag = sum([sum([gll[d1][d2].subs(xu[0], place[0]).subs(xu[1], place[1]) * v0[d1] * v0[d2] for d1 in range(2)]) for d2 in range(2)])
	return list(map(lambda n:n / math.sqrt(mag), v0))

def firstLocalMinimumOrSecondLocalMinimum(start, theta, t, goal):
	v0 = unitVecOfDirection(theta, start)
	y0 = v0 + start
	traj = odeint(func, y0, t)
	
	#	fMOT = findNthLocalMinimumOnTraj(0, traj, goal)
	#	sMOT = findNthLocalMinimumOnTraj(1, traj, goal)
	minima = findAllLocalMinimaOnTraj(traj, goal)

#	if fMOT[1] <= sMOT[1]:
#		return 0
#	else:
#		return 1
	return minima.index(min(minima, key=(lambda x: x[1])))

def positiveRotOrNegativeRot(start, theta, angleStep, t, goal, fOS):
	v0 = unitVecOfDirection(theta + angleStep, start)
	y0 = v0 + start
	trajP = odeint(func, y0, t)
	mOTP = findNthLocalMinimumOnTraj(fOS, trajP, goal)
	
	v0 = unitVecOfDirection(theta - angleStep, start)
	y0 = v0 + start
	trajN = odeint(func, y0, t)
	mOTN = findNthLocalMinimumOnTraj(fOS, trajN, goal)
	
	if mOTP[1] < mOTN[1]:
		return +1
	else:
		return -1
