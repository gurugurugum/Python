from sympy import *
from sympy.physics.quantum import *
from sympy.physics.matrices import *

epsilonuu=[[0,1],[-1,0]]
epsilonll=[[0,-1],[1,0]]

gammaulu=[msigma(3).tolist(),(-1*msigma(1)).tolist(),(-1*msigma(2)).tolist()]

zetal=[Symbol('zeta'+str(i)) for i in range(2)]
zetau=[sum([epsilonuu[i][d]*zetal[d] for d in range(2)]) for i in range(2)]

zetatl=[Symbol('zeta'+'tilde'+str(i)) for i in range(2)]
zetatu=[sum([epsilonuu[i][d]*zetatl[d] for d in range(2)]) for i in range(2)]

Ql=[Operator('Q'+str(i)) for i in range(2)]
Qu=[sum([epsilonuu[i][d]*Ql[d] for d in range(2)]) for i in range(2)]

Qtl=[Operator('Q'+'tilde'+str(i)) for i in range(2)]
Qtu=[sum([epsilonuu[i][d]*Qtl[d] for d in range(2)]) for i in range(2)]

zQ=sum([zetau[d]*Ql[d] for d in range(2)])
ztQt=sum([zetatu[d]*Qtl[d] for d in range(2)])

zzt=sum([zetau[d]*zetatl[d] for d in range(2)])
zgztu=[sum([sum([zetau[d1]*gammaulu[i][d1][d2]*zetatl[d2] for d1 in range(2)]) for d2 in range(2)]) for i in range(3)]

