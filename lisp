import sys

input = sys.argv[1]

ri = input.replace("(", " ( ").replace(")", " ) ")
si = list(filter(lambda x: len(x) > 0, ri.split(" ")))

res = 0
lbc = 0
lbp = 0
while(si[lbp] == "("):
    lbc += 1
    lbp += 1
lbp -= 1
rbp = lbp + 1
while(si[lbp] == "("):
    lbc+=1
    lbp+=1

print(lbc)
