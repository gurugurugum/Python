from sympy import *
from sympy.physics.quantum import *

epsilonuu=[[0,1],[-1,0]]
epsilonll=[[0,-1],[1,0]]

zetal=[Symbol('zeta'+str(i)) for i in range(2)]
zetau=[sum([epsilonuu[i][d]*zetal[d] for d in range(2)]) for i in range(2)]

zetatl=[Symbol('zeta'+'tilde'+str(i)) for i in range(2)]
zetatu=[sum([epsilonuu[i][d]*zetatl[d] for d in range(2)]) for i in range(2)]

Ql=[Operator('Q'+str(i)) for i in range(2)]
Qu=[sum([epsilonuu[i][d]*Ql[d] for d in range(2)]) for i in range(2)]

Qtl=[Operator('Q'+'tilde'+str(i)) for i in range(2)]
Qtu=[sum([epsilonuu[i][d]*Qtl[d] for d in range(2)]) for i in range(2)]




