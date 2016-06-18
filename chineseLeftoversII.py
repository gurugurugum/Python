from functools import *
from sympy import *

## Python 2.7
def chinese_remainder(n, a):
	sum = 0
	prod = reduce(lambda a, b: a*b, n)

	for n_i, a_i in zip(n, a):
		#		p = int(prod / n_i)
		p = prod // n_i
		#		print(p)
		sum += a_i * mul_inv(p, n_i) * p
	return sum % prod


def mul_inv(a, b):
	b0 = b
	x0, x1 = 0, 1
	if b == 1: return 1
	while b > 0:
		#		q = int(a / b)
		q = a // b
		#		print(q)
		a, b = b, a%b
		x0, x1 = x1 - q * x0, x0
	#	if x1 < 0: x1 += b0
	return x1

def A(n):
	numbers = []
	primes = []
	for i in range(1,n+1):
		#		print(i,prime(i))
		numbers.append(i)
		primes.append(prime(i))
	return chinese_remainder(primes,numbers)

def Sl(n):
	rl = []
	i = 1
	Al = [A(i)]
	p = prime(i)
	while p <= n:
		#		print(i, p)
		for j in range(len(Al) - 1):
			if Al[j] % p == 0:
				rl.append((p,j+1,Al[j]))
				break
		i += 1
		p = prime(i)
		Al.append(A(i))
	return rl

def S(n):
	sum = 0
	i = 1
	Al = [A(i)]
	p = prime(i)
	while p <= n:
		for j in range(len(Al) - 1):
			if Al[j] % p == 0:
				sum += p
				break
		i += 1
		p = prime(i)
		Al.append(A(i))
	return sum

if __name__ == '__main__':
	sum = 0
	i = 1
	Al = [A(i)]
	p = prime(i)
	while p <= 300000:
		print(i, p)
		for j in range(len(Al) - 1):
			if Al[j] % p == 0:
				sum += p
				break
		i += 1
		p = prime(i)
		Al.append(A(i))
	print(sum)

#Answer:326227335
