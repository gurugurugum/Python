def term(n):
	retVal = 0
	for i in range(n,n**2 + 1):
		retVal += i**3
	return retVal

for i in range(1,100):
	print term(i)
