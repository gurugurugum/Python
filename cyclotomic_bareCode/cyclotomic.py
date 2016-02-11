from sympy import *
x=Symbol('x',real=True)
def cyclotomic(m):
	f=1
	for i in range(1,m+1):
		if gcd(i,m)==1:
			f=f*(x-exp(2*pi*I/m*i))
	return f	
