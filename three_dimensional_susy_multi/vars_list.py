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

etal=[Symbol('eta'+str(i)) for i in range(2)]
etau=[sum([epsilonuu[i][d]*etal[d] for d in range(2)]) for i in range(2)]

etatl=[Symbol('eta'+'tilde'+str(i)) for i in range(2)]
etatu=[sum([epsilonuu[i][d]*etatl[d] for d in range(2)]) for i in range(2)]

Ql=[Operator('Q'+str(i)) for i in range(2)]
Qu=[sum([epsilonuu[i][d]*Ql[d] for d in range(2)]) for i in range(2)]

Qtl=[Operator('Q'+'tilde'+str(i)) for i in range(2)]
Qtu=[sum([epsilonuu[i][d]*Qtl[d] for d in range(2)]) for i in range(2)]

zQ=sum([zetau[d]*Ql[d] for d in range(2)])
ztQt=sum([zetatu[d]*Qtl[d] for d in range(2)])

eQ=sum([etau[d]*Ql[d] for d in range(2)])
etQt=sum([etatu[d]*Qtl[d] for d in range(2)])

zzt=sum([zetau[d]*zetatl[d] for d in range(2)])
zguzt=[sum([sum([zetau[d1]*gammaulu[i][d1][d2]*zetatl[d2] for d1 in range(2)]) for d2 in range(2)]) for i in range(3)]

ze=sum([zetau[d]*etal[d] for d in range(2)])

Q2=sum([Qu[d]*Ql[d] for d in range(2)]).subs(Ql[0]**2,0).subs(Ql[1]**2,0)
QguQ=[sum([sum([Qu[d1]*gammaulu[i][d1][d2]*Ql[d2] for d1 in range(2)]).subs(Ql[0]**2,0).subs(Ql[1]**2,0).subs(Ql[0]*Ql[1],-Ql[1]*Ql[0]) for d2 in range(2)]) for i in range(3)]
