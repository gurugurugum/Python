from three_dimensional_susy_multi.vars import *

zQ=(zeta_bu.T*Q_bl)[0]
ztQt=(zetat_bu.T*Qt_bl)[0]

eQ=(eta_bu.T*Q_bl)[0]
etQt=(etat_bu.T*Qt_bl)[0]

zzt=(zeta_bu.T*zetat_bl)[0]
zgzt_mu=[(zeta_bu.T*gamma_au[i]*zetat_bl)[0] for i in range(3)]

ze=(zeta_bu.T*eta_bl)[0]
zge_mu=[(zeta_bu.T*gamma_au[i]*eta_bl)[0] for i in range(3)]
zes=[ze]
zes.extend(zge_mu)

ztet=(zetat_bu.T*etat_bl)[0]
ztget_mu=[(zetat_bu.T*gamma_au[i]*etat_bl)[0] for i in range(3)]

e_z=Matrix([eta_bl[0]*zeta_bl[0],eta_bl[0]*zeta_bl[1],eta_bl[1]*zeta_bl[0],eta_bl[1]*zeta_bl[1]])
ezs=Matrix([Symbol('ez'),Symbol('egz1'),Symbol('egz2'),Symbol('egz3')])
ezMat=Matrix([[zes[i].coeff(e_z[j]) for j in range(4)] for i in range(4)])

et_z=[etat_bl[0]*zeta_bl[0],etat_bl[0]*zeta_bl[1],etat_bl[1]*zeta_bl[0],etat_bl[1]*zeta_bl[1]]
etzs=[Symbol('etz'),Symbol('etgz1'),Symbol('etgz2'),Symbol('etgz3')]

QQ=(Q_bu.T*Q_bl)[0].subs(Q_bl[0]**2,0).subs(Q_bl[1]**2,0).subs(Q_bl[0]*Q_bl[1]+Q_bl[1]*Q_bl[0],0)
QgQ_mu=[(Q_bu.T*gamma_au[i]*Q_bl)[0].subs(Q_bl[0]**2,0).subs(Q_bl[1]**2,0).subs(Q_bl[0]*Q_bl[1]+Q_bl[1]*Q_bl[0],0) for i in range(3)]

QQt=(Q_bu.T*Qt_bl)[0]
QgQt_mu=[(Q_bu.T*gamma_au[i]*Qt_bl)[0] for i in range(3)]


