def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n - 2) + fib(n - 1)

import sys

for i in range(int(sys.argv[1])):
	print fib(i)
