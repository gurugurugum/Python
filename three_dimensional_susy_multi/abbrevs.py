from three_dimensional_susy_multi.vars import *

zQ=zeta_bu.T*Q_bl
ztQt=zetat_bu.T*Qt_bl

eQ=eta_bu.T*Q_bl
etQt=etat_bu.T*Qt_bl

zzt=zeta_bu.T*zetat_bl
zguzt=[zeta_bu.T*gamma_au[i]*zetat_bl for i in range(3)]

ze=zeta_bu.T*eta_bl
ztet=zetat_bu.T*etat_bl

Q2=(Q_bu.T*Q_bl).subs(Q_bl[0]**2,0).subs(Q_bl[1]**2,0).subs(Q_bl[0]*Q_bl[1]+Q_bl[1]*Q_bl[0],0)
QguQ=[(Q_bu.T*gamma_au[i]*Q_bl).subs(Q_bl[0]**2,0).subs(Q_bl[1]**2,0).subs(Q_bl[0]*Q_bl[1]+Q_bl[1]*Q_bl[0],0) for i in range(3)]

