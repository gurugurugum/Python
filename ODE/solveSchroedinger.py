import numpy as np
import functools

def inner_prod(dx, v1, v2):
	return np.sum(v1*v2*dx)

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

def getCoeffs(dx, T, vs):
	return np.array(list(map(lambda v:inner_prod(dx, T, v), vs)))

def fOfT(f0, L, N, V, t):
	x, dx, w, vs, Vl = solveSchroedinger(L, N, V)
	return functools.reduce(lambda x,y:x+y, ((getCoeffs(dx, f0, vs)*(lambda x:np.e**(-1j*x*t))(w))*(vs.T)).T)
