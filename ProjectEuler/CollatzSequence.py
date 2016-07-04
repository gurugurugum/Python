def NCSeq(n):
	if n % 2 == 0:
		return n // 2
	else:
		return 3 * n +1 

def CSeq(n):
	res=[n]
	while res[-1] != 1:
		res.append(NCSeq(res[-1]))
	return res
