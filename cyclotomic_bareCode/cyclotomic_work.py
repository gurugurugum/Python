from sympy import *

x=Symbol('x',real=True)

def cyclotomic(m):
	f=1
	for i in range(m):
		if gcd(i,m)==1:
			f*=(x-exp(2*pi*I/m*i))
	return f

def cyclotomic_coeffs(m):
	return Poly(collect(expand_trig(expand(cyclotomic(m)).expand(complex=True)),x),x).all_coeffs()

#subs(sum([cos(pi/m*i) for i in range(1,m,2)]),+1/2)
#.subs(cos(pi/m),-sum([cos(pi/m*i) for i in range(3,m,2)])+1/2)

def subs_cos(exp,m):
	return exp.subs(cos(pi/m),-sum([cos(pi/m*i) for i in range(3,m,2)])+Rational(1,2))

def cyclotomic_expand(m):
	#f=collect(expand_trig(expand(cyclotomic(m)).expand(complex=True)),x)
	#f=collect(collect(expand(cyclotomic(m)),x).expand(complex=True),x)
	f=1
	for i in range(m):
		if gcd(i,m)==1:
			f*=(x-exp(2*pi*I/m*i))
			f=collect(expand(f),x)
	#pprint(f)
	f=collect(f.expand(complex=True),x)
	for i in range(m,2,-2):
		f=subs_cos(f,i)
	return f

def coprime_sum(m):
	n=0
	for i in range(1,m):
		if gcd(i,m)==1:
			n+=i
	return n

