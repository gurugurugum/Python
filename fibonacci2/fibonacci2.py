import sympy
import sys
import math

def fib(n):
	expr = (((1+sympy.sqrt(5))/2)**n - ((1-sympy.sqrt(5))/2)**n)/sympy.sqrt(5)
	return sympy.simplify(expr)

convSpec = '{0:>' + str(int(math.log10(int(sys.argv[1])) + 1) - 1) + '}'
for i in range(int(sys.argv[1]), int(sys.argv[2])):
	print("%s %s" % (convSpec.format(i), fib(i)))
