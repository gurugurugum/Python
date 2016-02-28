from three_dimensional_susy_multi.field_defs import *

#.subs(fd.Q_bl[0]**2,0).subs(fd.Q_bl[1]**2,0).subs(fd.Q_bl[0]*fd.Q_bl[1]+fd.Q_bl[1]*fd.Q_bl[0],0)
#.subs(ab.Q_bl[0]**2,0).subs(ab.Q_bl[1]**2,0).subs(ab.Q_bl[0]*ab.Q_bl[1]+ab.Q_bl[1]*ab.Q_bl[0],0).subs(ab.Q_bl[1]*ab.Q_bl[0],-ab.Q_bl[0]*ab.Q_bl[1])

zQztQtpztQtzQC=(ztQtC.subs(chit_bl[0],zQchit_bl[0]).subs(chit_bl[1],zQchit_bl[1])+zQC.subs(chi_bl[0],ztQtchi_bl[0]).subs(chi_bl[1],ztQtchi_bl[1]))[0]

twoILiedCpzztzmrHC=2*I*(sum([(zeta_bu.T*gamma_mu[d]*zetat_bl)[0]*D_scalar(C)[d] for d in range(3)])+(zeta_bu.T*zetat_bl)[0]*(z-r*H)*C)



