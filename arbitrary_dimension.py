from sympy import *

dim=4

def set_dimension(n):
	global dim
	dim =n

xu=[Symbol('x'+str(i)) for i in range(dim)]

#gll=[[Function('g'+str(i)+str(j))(xu[0],xu[1]) for j in range(dim)] for i in range(dim)]
gll=[[Function('g'+str(i)+str(j))(*xu) for j in range(dim)] for i in range(dim)]
for i in range(dim):
	for j in range(i+1,dim):
		gll[j][i]=gll[i][j]

guu=Matrix(gll).inv().tolist()

Gammalll=[[[Rational(1,2)*(gll[i][k].diff(xu[j])+gll[i][j].diff(xu[k])-gll[j][k].diff(xu[i])) for k in range(dim)] for j in range(dim)] for i in range(dim)]

Gammaull=[[[sum([guu[i][d]*Gammalll[d][j][k] for d in range(dim)]) for k in range(dim)] for j in range(dim)] for i in range(dim)]

Rlllu=[[[[Gammaull[l][i][k].diff(xu[j]) - Gammaull[l][j][k].diff(xu[i]) + sum([Gammaull[d][i][k]*Gammaull[l][d][j] - Gammaull[d][j][k]*Gammaull[l][d][i] for d in range(dim)]) for l in range(dim)] for k in range(dim)] for j in range(dim)] for i in range(dim)]
#Rlllu=[[[[Out[2][l][i][k].diff(a.xu[j]) - Out[2][l][j][k].diff(a.xu[i]) + sum([Out[2][d][i][k]*Out[2][l][d][j] - Out[2][d][j][k]*Out[2][l][d][i] for d in range(dim)]) for l in range(dim)] for k in range(dim)] for j in range(dim)] for i in range(dim)]

Rll=[[sum([Rlllu[i][d][j][d] for d in range(dim)]) for j in range(dim)] for i in range(dim)]

R=sum([sum([Rll[d2][d1]*guu[d1][d2] for d1 in range(dim)]) for d2 in range(dim)])


