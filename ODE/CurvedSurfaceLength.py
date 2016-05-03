import sys
sys.path.append('/Users/kazuma/Documents/Python')
from ODE.CurvedSurfaceLength_Funcs import *

start = [5, 0]
goal = [0, 5]
theta = math.atan2(goal[1] - start[1], goal[0] - start[0])

searchRange = euclidDistance3D(start, goal) ** 2
step = 0.01
t = np.arange(0, searchRange, step)

angleStep = 0.1
angleStepStep = 0.1
beforeDistance = searchRange ** 2
currentDistance = 0.0
result = 0.0
fOS = firstMinimaOrSecondMinima(start, theta, t, goal)
angleStep = angleStep * positiveRotOrNegativeRot(start, theta, angleStep, t, goal, fOS)
#for i in range(10000):
while 1:
	v0 = unitVecOfDirection(theta, start)
	y0 = v0 + start
	traj = odeint(func, y0, t)
	
	mOT = findNthMinimaOnTraj(fOS, traj, goal)
	distanceFromStart = mOT[0] * step
	result = distanceFromStart
	currentDistance = mOT[1]
	print(currentDistance)
#	print(firstMinimaOnTraj(goal, traj)[0])
#	print(secondMinimaOnTraj(goal, traj)[0])
	if currentDistance < beforeDistance:
		beforeDistance = currentDistance
		theta += angleStep
	elif currentDistance < beforeDistance + step:
		break
	else:
		beforeDistance = currentDistance
		angleStep = -1 * angleStep * angleStepStep
		theta += angleStep
print(result)

v0 = unitVecOfDirection(theta, start)
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
plt.hold(True)

x_surf=np.arange(-5, 5, 0.01)                # generate a mesh
y_surf=np.arange(-5, 5, 0.01)
x_surf, y_surf = np.meshgrid(x_surf, y_surf)
z_surf = x_surf ** 2 + y_surf ** 2             # ex. function, which depends on x and y
ax.plot_surface(x_surf, y_surf, z_surf, cmap=cm.hot);    # plot a 3d surface plot

ax.plot(traj[:, 2], traj[:, 3], height[:])
#plt.plot(traj[:, 2], traj[:, 3])
plt.show()

#for i in range(0, 10000, 100):
#	print(sum([sum([gll[d1][d2].subs(xu[0], traj[i][2]).subs(xu[1], traj[i][3]) * traj[i][d1] * traj[i][d2] for d1 in range(2)]) for d2 in range(2)]))
