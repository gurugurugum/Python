from sympy import *

x=Symbol('x')

def full_factor(f):
	r=roots(f,x)
	return LC(f,x)*Mul(*[(x-a)**r[a] for a in r])
