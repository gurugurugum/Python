from three_dimensional_susy_multi.vars import *

def coderiv_scalar(s):
	return [s.diff(x_mu[m]) for m in range(3)]

def coderiv_spinor_low(s):
	#oeg=[Matrix([[sum([sum([sum([omega_mlalau[i][d1][d2]*LeviCivita(d1+1,d2+1,d3+1)*gamma_au[d3][j,k] for d1 in range(3)]) for d2 in range(3)]) for d3 in range(3)]) for k in range(2)] for j in range(2)]) for i in range(3)]
	oeg=[MatAdd(*[MatAdd(*[MatAdd(*[omega_mlalau[i][d1][d2]*LeviCivita(d1+1,d2+1,d3+1)*gamma_au[d3] for d1 in range(3)]).doit() for d2 in range(3)]).doit() for d3 in range(3)]).doit() for i in range(3)]
	#oegMat=list(map(lambda n:Matrix(n),oeg))
	return [Matrix([s[b].diff(x_mu[m])-Rational(1,4)*I*(oeg[m]*s)[b] for b in range(2)]) for m in range(3)]

def coderiv_contraVector(v):
	return [Matrix([v[n].diff(x_mu[m])+sum([Chris_mumlml[n][m][d]*v[d] for d in range(3)]) for n in range(3)]) for m in range(3)]

def coderiv_coVector(v):
	return [Matrix([v[n].diff(x_mu[m])-sum([Chris_mumlml[d][m][n]*v[d] for d in range(3)]) for n in range(3)]) for m in range(3)]

#def coderiv_tensor(t,indType):

def Liederiv_spinor_low(conV,s):
	spinor_coderiv_part=MatAdd(*[conV[d]*coderiv_spinor_low(s)[d] for d in range(3)]).doit()
	vector_coderiv_part=MatAdd(*[MatAdd(*[MatAdd(*[sum([coderiv_contraVector(conV)[m][d]*g_mlml[d,n] for d in range(3)])*epsilon_mumumu[m][n][r]*gamma_ml[r] for r in range(3)]).doit() for n in range(3)]).doit() for m in range(3)]).doit()*s
	return spinor_coderiv_part+Rational(1,4)*I*vector_coderiv_part

