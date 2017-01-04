from sympy import *

dim = 4

G = Symbol('G')
M = Symbol('M')

def set_dimension(n):
    global dim
    dim = n

xu = [Symbol('x'+str(i)) for i in range(dim)]

#gll=[[Function('g'+str(i)+str(j))(xu[0],xu[1]) for j in range(dim)] for i in range(dim)]
gll = [[Function('g'+str(i)+str(j))(*xu) for j in range(dim)] for i in range(dim)]
for i in range(dim):
    for j in range(i+1, dim):
        gll[j][i] = gll[i][j]
#gll = [[-(1-2*G*M/xu[1]),0,0,0],[0,(1-2*G*M/xu[1]),0,0],[0,0,xu[1]**2,0],[0,0,0,xu[1]**2*sin(xu[2])]]

def subsMetricSchwarz(exp):
    retVal = exp
    retVal = retVal.subs(gll[0][0],       -(1-2*G*M/xu[1]))
    retVal = retVal.subs(gll[0][1], 0)
    retVal = retVal.subs(gll[0][2], 0)
    retVal = retVal.subs(gll[0][3], 0)
#    retVal = retVal.subs(gll[1][0], 0)
    retVal = retVal.subs(gll[1][1],  (1-2*G*M/xu[1])**(-1))
    retVal = retVal.subs(gll[1][2], 0)
    retVal = retVal.subs(gll[1][3], 0)
#    retVal = retVal.subs(gll[2][0], 0)
#    retVal = retVal.subs(gll[2][1], 0)
    retVal = retVal.subs(gll[2][2],               xu[1]**2)
    retVal = retVal.subs(gll[2][3], 0)
#    retVal = retVal.subs(gll[3][0], 0)
#    retVal = retVal.subs(gll[3][1], 0)
#    retVal = retVal.subs(gll[3][2], 0)
    retVal = retVal.subs(gll[3][3], xu[1]**2*sin(xu[2])**2)
    retVal = retVal.subs(sqrtmg, xu[1]**2*sin(xu[2]))
    return retVal

def subsMetricSpherical(exp):
    retVal = exp
    retVal = retVal.subs(gll[0][0], -1)
    retVal = retVal.subs(gll[0][1], 0)
    retVal = retVal.subs(gll[0][2], 0)
    retVal = retVal.subs(gll[0][3], 0)
#    retVal = retVal.subs(gll[1][0], 0)
    retVal = retVal.subs(gll[1][1], 1)
    retVal = retVal.subs(gll[1][2], 0)
    retVal = retVal.subs(gll[1][3], 0)
#    retVal = retVal.subs(gll[2][0], 0)
#    retVal = retVal.subs(gll[2][1], 0)
    retVal = retVal.subs(gll[2][2], xu[1]**2)
    retVal = retVal.subs(gll[2][3], 0)
#    retVal = retVal.subs(gll[3][0], 0)
#    retVal = retVal.subs(gll[3][1], 0)
#    retVal = retVal.subs(gll[3][2], 0)
    retVal = retVal.subs(gll[3][3], xu[1]**2*sin(xu[2])**2)
    retVal = retVal.subs(sqrtmg, xu[1]**2*sin(xu[2]))
    return retVal

r = Function('r')(xu[1])

def subsMetricReggeWheel(exp):
    retVal = exp
    retVal = retVal.subs(gll[0][0], -(1-2*G*M/r))
    retVal = retVal.subs(gll[0][1], 0)
    retVal = retVal.subs(gll[0][2], 0)
    retVal = retVal.subs(gll[0][3], 0)
#    retVal = retVal.subs(gll[1][0], 0)
    retVal = retVal.subs(gll[1][1], (1-2*G*M/r))
    retVal = retVal.subs(gll[1][2], 0)
    retVal = retVal.subs(gll[1][3], 0)
#    retVal = retVal.subs(gll[2][0], 0)
#    retVal = retVal.subs(gll[2][1], 0)
    retVal = retVal.subs(gll[2][2], r**2)
    retVal = retVal.subs(gll[2][3], 0)
#    retVal = retVal.subs(gll[3][0], 0)
#    retVal = retVal.subs(gll[3][1], 0)
#    retVal = retVal.subs(gll[3][2], 0)
    retVal = retVal.subs(gll[3][3], r**2*sin(xu[2])**2)
    retVal = retVal.subs(sqrtmg, (r-2*G*M)*r*sin(xu[2]))
    return retVal

def subsMetricMinkow(exp):
    retVal = exp
    retVal = retVal.subs(gll[0][0], -1)
    retVal = retVal.subs(gll[0][1], 0)
    retVal = retVal.subs(gll[0][2], 0)
    retVal = retVal.subs(gll[0][3], 0)
#    retVal = retVal.subs(gll[1][0], 0)
    retVal = retVal.subs(gll[1][1], 1)
    retVal = retVal.subs(gll[1][2], 0)
    retVal = retVal.subs(gll[1][3], 0)
#    retVal = retVal.subs(gll[2][0], 0)
#    retVal = retVal.subs(gll[2][1], 0)
    retVal = retVal.subs(gll[2][2], 1)
    retVal = retVal.subs(gll[2][3], 0)
#    retVal = retVal.subs(gll[3][0], 0)
#    retVal = retVal.subs(gll[3][1], 0)
#    retVal = retVal.subs(gll[3][2], 0)
    retVal = retVal.subs(gll[3][3], 1)
    retVal = retVal.subs(sqrtmg, 1)
    return retVal

guu = Matrix(gll).inv().tolist()

g = Matrix(gll).det()

sqrtmg = Function('sqrtmg')(*xu)

def laplacian(f):
    return sum([(sqrtmg*sum([guu[j][i]*f.diff(xu[i]) for i in range(dim)])).diff(xu[j]) for j in range(dim)])/sqrtmg

Gammalll = [[[Rational(1,2)*(gll[k][i].diff(xu[j])+gll[j][i].diff(xu[k])-gll[j][k].diff(xu[i])) for k in range(dim)] for j in range(dim)] for i in range(dim)]

Gammaull = [[[sum([guu[i][d]*Gammalll[d][j][k] for d in range(dim)]) for k in range(dim)] for j in range(dim)] for i in range(dim)]

Rlllu = [[[[Gammaull[l][i][k].diff(xu[j]) - Gammaull[l][j][k].diff(xu[i]) + sum([Gammaull[d][i][k]*Gammaull[l][d][j] - Gammaull[d][j][k]*Gammaull[l][d][i] for d in range(dim)]) for l in range(dim)] for k in range(dim)] for j in range(dim)] for i in range(dim)]
#Rlllu=[[[[Out[2][l][i][k].diff(a.xu[j]) - Out[2][l][j][k].diff(a.xu[i]) + sum([Out[2][d][i][k]*Out[2][l][d][j] - Out[2][d][j][k]*Out[2][l][d][i] for d in range(dim)]) for l in range(dim)] for k in range(dim)] for j in range(dim)] for i in range(dim)]

Rll = [[sum([Rlllu[i][d][j][d] for d in range(dim)]) for j in range(dim)] for i in range(dim)]

R = sum([sum([Rll[d2][d1]*guu[d1][d2] for d1 in range(dim)]) for d2 in range(dim)])


