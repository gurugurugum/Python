from sympy import *
from sympy.physics.quantum import Operator
from sympy.physics.matrices import Matrix, msigma
from sympy.functions.special.tensor_functions import LeviCivita

x_mu=Matrix([Symbol('x'+str(i)) for i in range(3)])

epsilon_bubu=Matrix([[0,1],[-1,0]])
epsilon_blbl=Matrix([[0,-1],[1,0]])

gamma_au=[msigma(3),-1*msigma(1),-1*msigma(2)]
gamma_al=gamma_au

e_mlau=Matrix([[Function('e'+str(i)+str(j))(*x_mu) for i in range(3)] for j in range(3)])
#e_almu=Matrix([[Function('ei'+str(i)+str(j))(*x_mu) for i in range(3)] for j in range(3)])
e_almu=e_mlau.inv().applyfunc(simplify)

epsilon_auauau=[[[LeviCivita(i,j,k) for k in range(3)] for j in range(3)] for i in range(3)]
epsilon_alalal=epsilon_auauau
epsilon_mumumu=[[[sum([sum([sum([e_almu[d1,i]*e_almu[d2,j]*e_almu[d3,k]*epsilon_auauau[d1][d2][d3] for d3 in range(3)]) for d2 in range(3)]) for d1 in range(3)]) for k in range(3)] for j in range(3)] for i in range(3)]
epsilon_mlmlml=[[[sum([sum([sum([e_mlau[i,d1]*e_mlau[j,d2]*e_mlau[k,d3]*epsilon_alalal[d1][d2][d3] for d3 in range(3)]) for d2 in range(3)]) for d1 in range(3)]) for k in range(3)] for j in range(3)] for i in range(3)]

gamma_mu=[MatAdd(*[e_almu[d,i]*gamma_au[d] for d in range(3)]).doit() for i in range(3)]
gamma_ml=[MatAdd(*[e_mlau[i,d]*gamma_al[d] for d in range(3)]).doit() for i in range(3)]

#g_mlml=(e_mlau*e_mlau.T).applyfunc(simplify)
g_mlml=(e_mlau*e_mlau.T)
#g_mumu=(e_almu.T*e_almu).applyfunc(simplify)
g_mumu=(e_almu.T*e_almu)

Chris_mumlml=[[[sum([Rational(1,2)*g_mumu[i,d]*(g_mlml[d,k].diff(x_mu[j]) + g_mlml[d,j].diff(x_mu[k]) - g_mlml[j,k].diff(x_mu[d])) for d in range(3)]) for k in range(3)] for j in range(3)] for i in range(3)]

omega_mlalau=[[[sum([e_mlau[d,k]*e_almu[j,d].diff(x_mu[i]) for d in range(3)]) + sum([sum([e_mlau[d1,k]*Chris_mumlml[d1][i][d2]*e_almu[j,d2] for d2 in range(3)]) for d1 in range(3)]) for k in range(3)] for j in range(3)] for i in range(3)]

R_mlmlalau=[[[[omega_mlalau[j][k][l].diff(x_mu[i])-omega_mlalau[i][k][l].diff(x_mu[j])+sum([omega_mlalau[j][k][d]*omega_mlalau[i][d][l]-omega_mlalau[i][k][d]*omega_mlalau[j][d][l] for d in range(3)]) for l in range(3)] for k in range(3)] for j in range(3)] for i in range(3)]
R_mlml=[[sum([sum([R_mlmlalau[i][d1][j][d2]*e_almu[d2,d1] for d1 in range(3)]) for d2 in range(3)]) for j in range(3)] for i in range(3)]
R=sum([sum([g_mumu[d1,d2]*R_mlml[d1][d2] for d1 in range(3)]) for d2 in range(3)])

zeta_bl=Matrix([Function('zeta'+str(i))(*x_mu) for i in range(2)])
zeta_bu=epsilon_bubu*zeta_bl

zetat_bl=Matrix([Function('zeta'+'tilde'+str(i))(*x_mu) for i in range(2)])
zetat_bu=epsilon_bubu*zetat_bl

eta_bl=Matrix([Function('eta'+str(i))(*x_mu) for i in range(2)])
eta_bu=epsilon_bubu*eta_bl

etat_bl=Matrix([Function('eta'+'tilde'+str(i))(*x_mu) for i in range(2)])
etat_bu=epsilon_bubu*etat_bl

#Q_bl=Matrix([Operator('Q'+str(i)) for i in range(2)])
#Q_bu=epsilon_bubu*Q_bl

#Qt_bl=Matrix([Operator('Q'+'tilde'+str(i)) for i in range(2)])
#Qt_bu=epsilon_bubu*Qt_bl

