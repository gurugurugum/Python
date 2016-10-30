import sys
from functools import reduce

#連続している"("の最後の"("の検索
def findLastLeftBracketOfContinuingLeftBrackets(list, startPlace):
	lbc = 0
	lbp = startPlace
	while(list[lbp] == "("):
		lbc += 1
		lbp += 1
	lbp -= 1
	return [lbc, lbp]

def findRightBracket(list, startPlace):
	lbc = 0
	rbp = startPlace
	while(list[rbp] != ")"):
		if list[rbp] == "(":
			lbc += 1
		rbp += 1
	return [lbc, rbp]

def passThroughDefun(input, startPlace):
	tmp = findLastLeftBracketOfContinuingLeftBrackets(input, startPlace)
	lbc = tmp[0] #"("の数
	lbp = tmp[1] #最後に読んだ"("の場所
	place = lbp

	if input[place + 1] == "defun":
		while lbc > 0:
			tmp = findRightBracket(input, place + 1)
			lbc += tmp[0] - 1
			place = tmp[1]

	return place

def passThroughArgDefs(input, startPlace):
	tmp = findLastLeftBracketOfContinuingLeftBrackets(input, startPlace)
	lbc = tmp[0] #"("の数
	lbp = tmp[1] #最後に読んだ"("の場所
	place = lbp
	
	if input[place + 1] == "=":
		while lbc > 0:
			tmp = findRightBracket(input, place + 1)
			lbc += tmp[0] - 1
			place = tmp[1]

	return place

def isABracket(token):
	return token == "(" or token == ")"

def isAnArithmeticOperator(token):
	return token == "+" or token == "-" or token == "*" or token == "/"

def isAComparisonOperator(token):
	return token == ">" or token == "<" or token == "==" or token == "!="

def isIf(token):
	return token == "if"

def isFloat(str):
	try:
		float(str)
		return True
	except ValueError:
		return False

def compute(list): #list is with brackets
	operator = list[1]
	operands = map((lambda x: float(x)), list[2:len(list) - 1])
	if operator == "+":
		return str(reduce((lambda x, y: x + y), operands))
	elif operator == "-":
		return str(reduce((lambda x, y: x - y), operands))
	elif operator == "*":
		return str(reduce((lambda x, y: x * y), operands))
	elif operator == "/":
		return str(reduce((lambda x, y: x / y), operands))

def getOneStatement(list):
	if isFloat(list[0]):
		return [list[0]]
	tmp = findLastLeftBracketOfContinuingLeftBrackets(list, 0)
	lbc = tmp[0] #"("の数
	lbp = tmp[1] #最後に読んだ"("の場所
	place = lbp

	while lbc > 0:
		tmp = findRightBracket(list, place + 1)
		lbc += tmp[0] - 1
		place = tmp[1]

	return list[0:place + 1]

def evalBool(bool):
	op = bool[1]
	arg1 = bool[2]
	arg2 = bool[3]
	if op == ">":
		return float(arg1) > float(arg2)
	if op == "<":
		return float(arg1) < float(arg2)
	if op == "==":
		return float(arg1) == float(arg2)
	if op == "!=":
		return float(arg1) != float(arg2)

def evaluateIfStatement(ifStatement):
	bool = getOneStatement(ifStatement[2:])
	ifTrue = getOneStatement(ifStatement[2 + len(bool):])
	ifFalse = getOneStatement(ifStatement[2 + len(bool) + len(ifTrue):])
	if evalBool(bool):
		return ifTrue
	else:
		return ifFalse

def isComputable(list):
	for i in range(2, len(list) - 1):
		if not isFloat(list[i]):
			return False
	return True

def isEvaluatable(list):
	cmped1 = list[4]
	cmped2 = list[5]
	return isFloat(cmped1) and isFloat(cmped2)

def computeComputableExpressions(list):
	computed = True
	while computed:
		computed = False
		for i in range(len(list)):
			token = list[i]
			if isAnArithmeticOperator(token):
				exp = getOneStatement(list[i - 1:])
				if isComputable(exp):
					list = list[:i - 1] + [str(compute(exp))] + list[i - 1 + len(exp):]
					computed = True
					break
				else:
					continue
			elif isIf(token):
				exp = getOneStatement(list[i - 1:])
				if isEvaluatable(exp):
					beforeIfStatement = list[:i - 1]
					ifStatement = getOneStatement(list[i - 1:])
					afterIfStatement = list[i - 1 + len(ifStatement):]
					list = beforeIfStatement + evaluateIfStatement(ifStatement) + afterIfStatement
					computed = True
					break
				else:
					continue
	return list

def getExpressionsFromHead(list, n):
	ret = []
	for i in range(n):
		headExp = getOneStatement(list)
		ret.append(headExp)
		list = list[len(headExp):]
	return ret

def replace(list, old, new):
	res = []
	for elem in list:
		if elem == old:
			res += new
		else:
			res.append(elem)
	return res

def getFuncExpSymblReplaced(argSymbols, funcExp, givenArgs):
	for i in range(len(argSymbols)):
		argSymbol = argSymbols[i]
		givenArg = givenArgs[i]
		funcExp = replace(funcExp, argSymbol, givenArg)
	return funcExp

def replaceFuncs(list):
	i = 0
	while i < len(list):
		token = list[i]
		if not isABracket(token) and not isAnArithmeticOperator(token) and not isAComparisonOperator(token) and not isIf(token) and not isFloat(token):
			funcName = token
			argSymbols = analdDefun[funcName][0]
			funcExp = analdDefun[funcName][1]
			arity = len(argSymbols)
			givenArgs = getExpressionsFromHead(list[i + 1:], arity)
			funcExpSymblReplaced = getFuncExpSymblReplaced(argSymbols, funcExp, givenArgs)
			beforeFunc = list[:i - 1]
			funcExpToReplace = getOneStatement(list[i - 1:])
			afterFunc = list[i - 1 + len(funcExpToReplace):]
			list = beforeFunc + funcExpSymblReplaced + afterFunc
			i = len(beforeFunc) + len(funcExpSymblReplaced) - 1
		i += 1
	return list

def findNextCollon(list, startPlace):
	i = startPlace
	while i < len(list):
		if list[i] == ";":
			return i
		i += 1
	return i

def findNextNewLine(list, startPlace):
	i = startPlace
	while i < len(list):
		if list[i] == "\n":
			return i
		i += 1
	return i

def deleteComments(list):
	i = 0
	while i < len(list):
		collonPlace = findNextCollon(list, i)
		newLinePlace = findNextNewLine(list, collonPlace)
		del list[collonPlace:newLinePlace + 1]
		i = collonPlace

fileName = sys.argv[1]
f = open(fileName, 'r')
input = f.read()

ri = input.replace("(", " ( ").replace(")", " ) ").replace("\n", " \n ").replace("\t", " \t ").replace(";", " ; ")
si = ri.split(" ")
deleteComments(si)
fi = list(filter(lambda x: len(x) > 0 and x != "\n" and x != "\t" , si))

res = 0 #結果

place = -1 #今読んでるとこ
rowArgDefs = [] #変数定義たち
while fi[findLastLeftBracketOfContinuingLeftBrackets(fi, place + 1)[1] + 1] == "=":
	placeBefore = place + 1
	place = passThroughArgDefs(fi, place + 1)
	rowArgDefs.append(fi[placeBefore:place])
for argDef in rowArgDefs:
	fi[place + 1:] = replace(fi[place + 1:], argDef[2], argDef[3])
rowDefuns = [] #関数定義たち
while fi[findLastLeftBracketOfContinuingLeftBrackets(fi, place + 1)[1] + 1] == "defun":
	placeBefore = place + 1
	place = passThroughDefun(fi, place + 1)
	rowDefuns.append(fi[placeBefore:place])
expToCompute = fi[place + 1:] #計算すべき式

#defunからdictを作成
analdDefun = {}
for rowDefun in rowDefuns:
	analdDefun[rowDefun[2]] = [rowDefun[4:findRightBracket(rowDefun, 4)[1]], rowDefun[findRightBracket(rowDefun, 4)[1] + 1:]]

#計算できるところを計算する
#expToCompute = computeComputableExpressions(expToCompute)

#関数を置き換える
#expToCompute = replaceFuncs(expToCompute)

while len(expToCompute) > 1:
	print("computing...")
	print(" ".join(expToCompute))
	expToCompute = computeComputableExpressions(expToCompute)
	if len(expToCompute) > 1:
		print("replacing...")
		print(" ".join(expToCompute))
		expToCompute = replaceFuncs(expToCompute)

#print(" ".join(si), place, len(si), rowDefuns, analdDefun, expToCompute)
print(" ".join(fi))
print(" ".join(expToCompute))
#print(expToCompute)
