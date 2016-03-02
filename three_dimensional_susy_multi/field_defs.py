from three_dimensional_susy_multi.vars import *
from three_dimensional_susy_multi.derivs import *

z=Symbol('z')
r=Symbol('r')

H=Function('H')(*x_mu)
A_ml=[Function('A'+str(i))(*x_mu) for i in range(3)]
V_ml=[Function('V'+str(i))(*x_mu) for i in range(3)]
C_ml=[Function('C'+str(i))(*x_mu) for i in range(3)]

def D_scalar(s):
	return [coderiv_scalar(s)[i]-I*r(A_ml[i]-Rational(1,2)*V_ml[i])*s-I*z*C_ml[i]*s for i in range(3)]

def D_contraVector(v):
	return [[coderiv_contraVector(v)[i][j]-I*r(A_ml[i]-Rational(1,2)*V_ml[i])*v[j]-I*z*C_ml[i]*v[j] for j in range(3)] for i in range(3)]

def D_coVector(v):
	return [[coderiv_coVector(v)[i][j]-I*r(A_ml[i]-Rational(1,2)*V_ml[i])*v[j]-I*z*C_ml[i]*v[j] for j in range(3)] for i in range(3)]

C=Function('C')(*x_mu)
chi_bl=Matrix([Function('chi'+str(i))(*x_mu) for i in range(2)])
chit_bl=Matrix([Function('chi'+'tilde'+str(i))(*x_mu) for i in range(2)])
M=Function('M')(*x_mu)
Mt=Function('M'+'tilde')(*x_mu)
a_ml=[Function('a'+str(i))(*x_mu) for i in range(3)]
a_mu=[sum([g_mumu[i,j]*a_ml[j] for j in range(3)]) for i in range(3)]
sigma=Function('sigma')(*x_mu)
lambda_bl=Matrix([Function('lambda'+str(i))(*x_mu) for i in range(2)])
lambdat_bl=Matrix([Function('lambda'+'tilde'+str(i))(*x_mu) for i in range(2)])
D=Function('D')(*x_mu)

#differential equations of zeta and zeta-tilde
diffz=[Rational(1,4)*I*(MatAdd(*[MatAdd(*[MatAdd(*[omega_mlalau[i][d1][d2]*LeviCivita(d1+1,d2+1,d3+1)*gamma_au[d3] for d1 in range(3)]).doit() for d2 in range(3)]).doit() for d3 in range(3)]).doit())*zeta_bl+I*(A_ml[i]-V_ml[i])*zeta_bl-Rational(1,2)*(H*gamma_ml[i]+MatAdd(*[sum([sum([epsilon_mlmlml[i][d1][d2]*g_mumu[d1,d3]*V_ml[d3] for d1 in range(3)]) for d3 in range(3)])*gamma_mu[d2] for d2 in range(3)]).doit())*zeta_bl for i in range(3)]
diffzt=[Rational(1,4)*I*(MatAdd(*[MatAdd(*[MatAdd(*[omega_mlalau[i][d1][d2]*LeviCivita(d1+1,d2+1,d3+1)*gamma_au[d3] for d1 in range(3)]).doit() for d2 in range(3)]).doit() for d3 in range(3)]).doit())*zetat_bl-I*(A_ml[i]-V_ml[i])*zetat_bl-Rational(1,2)*(H*gamma_ml[i]-MatAdd(*[sum([sum([epsilon_mlmlml[i][d1][d2]*g_mumu[d1,d3]*V_ml[d3] for d1 in range(3)]) for d3 in range(3)])*gamma_mu[d2] for d2 in range(3)]).doit())*zetat_bl for i in range(3)]

#tranformation of C
zQC=I*zeta_bu.T*chi_bl
ztQtC=-I*zetat_bu.T*chit_bl
eQC=I*eta_bu.T*chi_bl
etQtC=-I*etat_bu.T*chit_bl

#tranformation of chi
zQchi_bl=M*zeta_bl
ztQtchi_bl=((sigma+(z-r*H)*C)*eye(2)+MatAdd(*[gamma_mu[i]*(I*a_ml[i]+D_scalar(C)[i]) for i in range(3)]).doit())*zetat_bl
eQchi_bl=M*eta_bl
etQtchi_bl=((sigma+(z-r*H)*C)*eye(2)+MatAdd(*[gamma_mu[i]*(I*a_ml[i]+D_scalar(C)[i]) for i in range(3)]).doit())*etat_bl

#tranformation of chi-tilde
zQchit_bl=-((sigma-(z-r*H)*C)*eye(2)+MatAdd(*[gamma_mu[i]*(-I*a_ml[i]+D_scalar(C)[i]) for i in range(3)]).doit())*zeta_bl
ztQtchit_bl=-Mt*zetat_bl
eQchit_bl=-((sigma-(z-r*H)*C)*eye(2)+MatAdd(*[gamma_mu[i]*(-I*a_ml[i]+D_scalar(C)[i]) for i in range(3)]).doit())*eta_bl
etQtchit_bl=-Mt*etat_bl

#tranformation of M
zQM=0
#tmp=[(zetat_bu.T*gamma_mu[i]*chi_bl)[0] for i in range(3)]
#tmp2=sum([D_contraVector([(zetat_bu.T*gamma_mu[i]*chi_bl)[0] for i in range(3)])[d][d] for d in range(3)])
ztQtM=2*(zetat_bu.T*lambdat_bl)[0]-2*I*(z-(r-2)*H)*(zetat_bu.T*chi_bl)[0]+2*I*sum([D_contraVector([(zetat_bu.T*gamma_mu[i]*chi_bl)[0] for i in range(3)])[d][d] for d in range(3)])
eQM=0
etQtM=2*(etat_bu.T*lambdat_bl)[0]-2*I*(z-(r-2)*H)*(etat_bu.T*chi_bl)[0]+2*I*sum([D_contraVector([(etat_bu.T*gamma_mu[i]*chi_bl)[0] for i in range(3)])[d][d] for d in range(3)])

#tranformation of M-tilde
zQMt=2*(zeta_bu.T*lambda_bl)[0]-2*I*(z-(r+2)*H)*(zeta_bu.T*chit_bl)[0]-2*I*sum([D_contraVector([(zeta_bu.T*gamma_mu[i]*chit_bl)[0] for i in range(3)])[d][d] for d in range(3)])
ztQtM=0
eQMt=2*(eta_bu.T*lambda_bl)[0]-2*I*(z-(r+2)*H)*(eta_bu.T*chit_bl)[0]-2*I*sum([D_contraVector([(eta_bu.T*gamma_mu[i]*chit_bl)[0] for i in range(3)])[d][d] for d in range(3)])
etQtM=0

#tranformation of a_ml
zQa_ml=[-I*zeta_bu.T*gamma_mu[i]*lambdat_bl+D_scalar(zeta_bu.T*chi_bl)[i] for i in range(3)]
ztQta_ml=[I*zetat_bu.T*gamma_mu[i]*lambda_bl+D_scalar(zetat_bu.T*chit_bl)[i] for i in range(3)]
eQa_ml=[-I*eta_bu.T*gamma_mu[i]*lambdat_bl+D_scalar(eta_bu.T*chi_bl)[i] for i in range(3)]
etQta_ml=[I*etat_bu.T*gamma_mu[i]*lambda_bl+D_scalar(etat_bu.T*chit_bl)[i] for i in range(3)]

#tranformation of sigma
zQsigma=-zeta_bu.T*lambdat_bl+I*(z-r*H)*zeta_bu.T*chi_bl
ztQtsigma=-zetat_bu.T*lambda_bl+I*(z-r*H)*zetat_bu.T*chit_bl
eQsigma=-eta_bu.T*lambdat_bl+I*(z-r*H)*eta_bu.T*chi_bl
etQtsigma=-etat_bu.T*lambda_bl+I*(z-r*H)*etat_bu.T*chit_bl

#tranformation of lambda
zQlambda_bl=(I*(D+sigma*H)*eye(2)-MatAdd(*[((z-r*H)*a_mu[i]+I*sum([sum([epsilon_mumumu[i][j][k]*D_coVector(a_ml)[j][k] for j in range(3)]) for k in range(3)])+I*sum([g_mumu[i,j]*(D_scalar(sigma)[j]-V_ml[j]) for j in range(3)]))*gamma_ml[i] for i in range(3)]).doit())*zeta_bl
ztQtlambda_bl=[0,0]

#tranformation of lambda-tilde
zQlambdat_bl=[0,0]
ztQtlambdat_bl=(I*(D+sigma*H)*eye(2)-MatAdd(*[((z-r*H)*a_mu[i]-I*sum([sum([epsilon_mumumu[i][j][k]*D_coVector(a_ml)[j][k] for j in range(3)]) for k in range(3)])+I*sum([g_mumu[i,j]*(D_scalar(sigma)[j]+V_ml[j]) for j in range(3)]))*gamma_ml[i] for i in range(3)]).doit())*zetat_bl

#tranformation of D
zQD=sum([D_contraVector([(zeta_bu.T*gamma_mu[i]*lambdat_bl)[0] for i in range(3)])[d][d]-I*V_ml[d]*(zeta_bu.T*gamma_mu[d]*lambdat_bl)[0] for d in range(3)])-H*(zeta_bu.T*lambdat_bl)[0]+(z-r*H)*((zeta_bu.T*lambdat_bl)[0]-I*H*(zeta_bu.T*chi_bl)[0])+Rational(1,4)*I*r*(R-2*sum([sum([g_mumu[d1,d2]*V_ml[d1]*V_ml[d2] for d1 in range(3)]) for d2 in range(3)])-6*H**2)*(zeta_bu.T*chi_bl)[0]
ztQtD=sum([D_contraVector([(zetat_bu.T*gamma_mu[i]*lambda_bl)[0] for i in range(3)])[d][d]+I*V_ml[d]*(zetat_bu.T*gamma_mu[d]*lambda_bl)[0] for d in range(3)])-H*(zetat_bu.T*lambda_bl)[0]-(z-r*H)*((zetat_bu.T*lambda_bl)[0]+I*H*(zetat_bu.T*chit_bl)[0])+Rational(1,4)*I*r*(R-2*sum([sum([g_mumu[d1,d2]*V_ml[d1]*V_ml[d2] for d1 in range(3)]) for d2 in range(3)])-6*H**2)*(zetat_bu.T*chit_bl)[0]







































