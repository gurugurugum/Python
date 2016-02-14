from sympy import *

xu=[Symbol('x'+str(i)) for i in range(2)]

gll=[[Function('g'+str(i)+str(j))(xu[0],xu[1]) for j in range(2)] for i in range(2)]
gll[1][0]=gll[0][1]

guu=Matrix(gll).inv().tolist()

Gammalll=[[[Rational(1,2)*(gll[i][k].diff(xu[j])+gll[i][j].diff(xu[k])-gll[j][k].diff(xu[i])) for k in range(2)] for j in range(2)] for i in range(2)]

Gammaull=[[[sum([guu[i][d]*Gammalll[d][j][k] for d in range(2)]) for k in range(2)] for j in range(2)] for i in range(2)]

Rlllu=[[[[Gammaull[l][i][k].diff(xu[j]) - Gammaull[l][j][k].diff(xu[i]) + sum([Gammaull[d][i][k]*Gammaull[l][d][j] - Gammaull[d][j][k]*Gammaull[l][d][i] for d in range(2)]) for l in range(2)] for k in range(2)] for j in range(2)] for i in range(2)]

Rll=[[sum([Rlllu[i][d][j][d] for d in range(2)]) for j in range(2)] for i in range(2)]

R=sum([sum([Rll[d2][d1]*guu[d1][d2] for d1 in range(2)]) for d2 in range(2)])


