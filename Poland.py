import sys

def isOp(token):
	return (token == "+") or (token == "-") or (token == "*") or (token == "/")

def searchDoubleNum(list):
	i = 0
	while 1:
		if (not isOp(list[i])) and (not isOp(list[i+1])):
			break
		i += 1
		if i + 1 > len(list) - 1:
			return -1
	return i

def calc(op, a1, a2):
	if op == "+":
		return float(a1) + float(a2)
	elif op == "-":
		return float(a1) - float(a2)
	elif op == "*":
		return float(a1) * float(a2)
	else:
		return float(a1) / float(a2)

def calcBack(list, pos):
	if pos < 1:
		return []
	nl = list[:pos-1]
	nl.append(calc(list[pos-1], list[pos], list[pos+1]))
	if len(nl) - 2 < 0:
		return nl
	if (not isOp(nl[len(nl) - 2])):
		return calcBack(nl, len(nl) - 2)
	else:
		return nl

instr = sys.argv[1]
ins = instr.split(" ")

while len(ins) > 1:
	pos = searchDoubleNum(ins)
	if pos == -1:
		print("error!!")
		break
	frontList = calcBack(ins, pos)
	if frontList == []:
		print("error!!")
		break
	backList = ins[pos + 2:]
	ins = frontList + backList

if (pos != -1) and (frontList != []):
	print(ins[0])


