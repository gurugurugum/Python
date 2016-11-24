import numpy as np
import functools
import matplotlib.pyplot as plt

def inner_prod(dx, v1, v2):
	return np.sum(np.conjugate(v1)*v2*dx)

def norm(dx, v):
	return np.sqrt(inner_prod(dx, v, v))

def normalize(dx, v):
	return v/norm(dx, v)

def normalize_vs(dx, vs):
	return np.array(list(map(lambda v:normalize(dx, v), vs)))

def solveSchroedinger(L, N, V):
	x, dx = np.linspace(-L/2, L/2, N), L / N
	K = np.eye(N, N)
	K_sub = np.vstack((K[1:], np.array([0] * N)))
	K = dx**-2 * (2 * K - K_sub - K_sub.T)
	Vl = np.array(list(map(V,np.linspace(-L/2, L/2, N))))
	Vm = np.diag(Vl)
	H = (K / 2 + Vm)
	w, v = np.linalg.eigh(H)
	return x, dx, w, normalize_vs(dx, v.T), Vl

def getCoeffs(dx, vs, T):
	return np.array(list(map(lambda v:inner_prod(dx, v, T), vs)))

def fOfT(f0, L, N, V, t):
	x, dx, w, vs, Vl = solveSchroedinger(L, N, V)
	return functools.reduce(lambda x,y:x+y, ((getCoeffs(dx, vs, f0)*(lambda x:np.e**(-1j*x*t))(w))*(vs.T)).T)

class System:
	def __init__(self, L, N, V):
		self.L = L
		self.N = N
		self.x, self.dx = np.linspace(-self.L/2, self.L/2, self.N), self.L / self.N
		self.VL = np.array(list(map(V,self.x)))
		K = np.eye(self.N, self.N)
		K_sub = np.vstack((K[1:], np.array([0] * self.N)))
		K = self.dx**-2 * (2 * K - K_sub - K_sub.T)
		VM = np.diag(self.VL)
		H = (K / 2 + VM)
		self.w, self.vs = np.linalg.eigh(H)
		self.vs = normalize_vs(self.dx, self.vs.T)

	def setWF0ByFunc(self, f):
		self.wF0L = np.array(list(map(f,self.x)))
		self.wF0L = normalize(self.dx, self.wF0L)
		self.coeffs = getCoeffs(self.dx, self.vs, self.wF0L)

	def setWF0ByList(self, l):
		self.wF0L = l
		self.wF0L = normalize(self.dx, self.wF0L)
		self.coeffs = getCoeffs(self.dx, self.vs, self.wF0L)

	def setBoundary(self, l, u):
		xl = self.x > l
		xu = self.x < u
		self.xlu = xl*xu

	def plotPotential(self, l, u):
		xl = self.x > l
		xu = self.x < u
		xlu = xl*xu
		plt.plot(self.x[xlu], self.VL[xlu], label="potential")
		plt.legend(loc='upper left')

	def plotPotential(self):
		plt.plot(self.x[self.xlu], self.VL[self.xlu], label="potential")
		plt.legend(loc='upper left')

	def getWFOf(self, t):
		return functools.reduce(lambda x,y:x+y, ((self.coeffs*(lambda x:np.e**(-1j*x*t))(self.w))*(self.vs.T)).T)

	def plotWFOf(self, t):
		plt.plot(self.x[self.xlu], np.absolute(self.getWFOf(t))[self.xlu], label="t="+str(t))
		plt.legend(loc='upper left')




