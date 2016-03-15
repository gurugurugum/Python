import sys
sys.path.append('/Users/kazuma/Documents/Python')

from three_dimensional_susy_multi.field_defs import *

#.subs(fd.Q_bl[0]**2,0).subs(fd.Q_bl[1]**2,0).subs(fd.Q_bl[0]*fd.Q_bl[1]+fd.Q_bl[1]*fd.Q_bl[0],0)
#.subs(ab.Q_bl[0]**2,0).subs(ab.Q_bl[1]**2,0).subs(ab.Q_bl[0]*ab.Q_bl[1]+ab.Q_bl[1]*ab.Q_bl[0],0).subs(ab.Q_bl[1]*ab.Q_bl[0],-ab.Q_bl[0]*ab.Q_bl[1])

def subsDiffZ(exp):
	retVal = exp
	retVal = retVal.subs(zeta_bl[0].diff(x_mu[0]),diffz[0][0])
	retVal = retVal.subs(zeta_bl[1].diff(x_mu[0]),diffz[0][1])
	retVal = retVal.subs(zeta_bl[0].diff(x_mu[1]),diffz[1][0])
	retVal = retVal.subs(zeta_bl[1].diff(x_mu[1]),diffz[1][1])
	retVal = retVal.subs(zeta_bl[0].diff(x_mu[2]),diffz[2][0])
	retVal = retVal.subs(zeta_bl[1].diff(x_mu[2]),diffz[2][1])
	return retVal

def subsDiffZt(exp):
	retVal = exp
	retVal = retVal.subs(zetat_bl[0].diff(x_mu[0]),diffzt[0][0])
	retVal = retVal.subs(zetat_bl[1].diff(x_mu[0]),diffzt[0][1])
	retVal = retVal.subs(zetat_bl[0].diff(x_mu[1]),diffzt[1][0])
	retVal = retVal.subs(zetat_bl[1].diff(x_mu[1]),diffzt[1][1])
	retVal = retVal.subs(zetat_bl[0].diff(x_mu[2]),diffzt[2][0])
	retVal = retVal.subs(zetat_bl[1].diff(x_mu[2]),diffzt[2][1])
	return retVal

#--- C ---
#zQztQtpztQtzQC=ztQtC.subs(chit_bl[0],zQchit_bl[0]).subs(chit_bl[1],zQchit_bl[1])+zQC.subs(chi_bl[0],ztQtchi_bl[0]).subs(chi_bl[1],ztQtchi_bl[1])
#
#twoILiedCpzztzmrHC=2*I*(sum([(zeta_bu.T*gamma_mu[d]*zetat_bl)[0]*D_scalar(C)[d] for d in range(3)])+(zeta_bu.T*zetat_bl)[0]*(z-r*H)*C)
#
#zeroOfC=simplify(zQztQtpztQtzQC - twoILiedCpzztzmrHC)


#--- chi ---
zQztQtpztQtzQchi=Matrix([subsDiffZ( ztQtchi_bl[i].subs(sigma,zQsigma).subs(C,zQC).subs(a_ml[0],zQa_ml[0]).subs(a_ml[1],zQa_ml[1]).subs(a_ml[2],zQa_ml[2]).doit() ) + zQchi_bl[i].subs(M,ztQtM) for i in range(2)])

twoILiedchipzztzmrHchi=2*I*(Liederiv_spinor_low([(zeta_bu.T*gamma_mu[i]*zetat_bl)[0] for i in range(3)],chi_bl)+sum([(zeta_bu.T*gamma_mu[d]*zetat_bl)[0]*(-I*r*(A_ml[d]-Rational(1,2)*V_ml[d])-I*z*C_ml[d]) for d in range(3)])*chi_bl+(zeta_bu.T*zetat_bl)[0]*(z-r*H)*chi_bl)

zeroOfchi=(zQztQtpztQtzQchi - twoILiedchipzztzmrHchi).applyfunc(simplify)


#--- chi-tilde ---
#zQztQtpztQtzQchit=Matrix([ztQtchit_bl[i].subs(Mt,zQMt) + subsDiffZt( zQchit_bl[i].subs(sigma,ztQtsigma).subs(C,ztQtC).subs(a_ml[0],ztQta_ml[0]).subs(a_ml[1],ztQta_ml[1]).subs(a_ml[2],ztQta_ml[2]) ) for i in range(2)])

#twoILiedchitpzztzmrHchit=2*I*(Liederiv_spinor_low([(zeta_bu.T*gamma_mu[i]*zetat_bl)[0] for i in range(3)],chit_bl)+sum([(zeta_bu.T*gamma_mu[d]*zetat_bl)[0]*(-I*r*(A_ml[d]-Rational(1,2)*V_ml[d])-I*z*C_ml[d]) for d in range(3)])*chit_bl+(zeta_bu.T*zetat_bl)[0]*(z-r*H)*chit_bl)


#--- M ---
#zQztQtpztQtzQM=subsDiffZ(subsDiffZt(ztQtM.subs(lambdat_bl[0],zQlambdat_bl[0]).subs(lambdat_bl[1],zQlambdat_bl[1]).subs(chi_bl[0],zQchi_bl[0]).subs(chi_bl[1],zQchi_bl[1])+zQM))
#
#twoILiedMpzztzmrHM=2*I*(sum([(zeta_bu.T*gamma_mu[d]*zetat_bl)[0]*D_scalar(M)[d] for d in range(3)])+(zeta_bu.T*zetat_bl)[0]*(z-r*H)*M)
#
#zeroOfM=simplify(zQztQtpztQtzQM - twoILiedMpzztzmrHM)


#--- M-tilde ---
#zQztQtpztQtzQMt=subsDiffZ(subsDiffZt(ztQtMt+zQMt.subs(lambda_bl[0],zQlambda_bl[0]).subs(lambda_bl[1],zQlambda_bl[1]).subs(chit_bl[0],zQchit_bl[0]).subs(chit_bl[1],zQchit_bl[1])))

#twoILiedMtpzztzmrHMt=2*I*(sum([(zeta_bu.T*gamma_mu[d]*zetat_bl)[0]*D_scalar(Mt)[d] for d in range(3)])+(zeta_bu.T*zetat_bl)[0]*(z-r*H)*Mt)


#--- a_ml ---
#zQztQtpztQtzQa_ml=[subsDiffZ(subsDiffZt( ztQta_ml[i].subs(lambda_bl[0],zQlambda_bl[0]).subs(lambda_bl[1],zQlambda_bl[1]).subs(chit_bl[0],zQchit_bl[0]).subs(chit_bl[1],zQchit_bl[1])+zQa_ml[i].subs(lambdat_bl[0],ztQtlambdat_bl[0]).subs(lambdat_bl[1],ztQtlambdat_bl[1]).subs(chi_bl[0],ztQtchi_bl[0]).subs(chi_bl[1],ztQtchi_bl[1]) )) for i in range(3)]

#twoILieda_mlpzztzmrHa_ml=[2*I*(Liederiv_coVector([(zeta_bu.T*gamma_mu[d]*zetat_bl)[i] for i in range(3)],a_ml)[j]+sum([(zeta_bu.T*gamma_mu[d]*zetat_bl)[0]*(-I*r*(A_ml[d]-Rational(1,2)*V_ml[d])-I*z*C_ml[d]) for d in range(3)])*a_ml[j]+(zeta_bu.T*zetat_bl)[0]*(z-r*H)*a_ml[j]) for j in range(3)]


#--- sigma ---
#zQztQtpztQtzQsigma=(ztQtsigma.subs(lambda_bl[0],zQlambda_bl[0]).subs(lambda_bl[1],zQlambda_bl[1]).subs(chit_bl[0],zQchit_bl[0]).subs(chit_bl[1],zQchit_bl[1])+zQsigma.subs(lambdat_bl[0],ztQtlambdat_bl[0]).subs(lambdat_bl[1],ztQtlambdat_bl[1]).subs(chi_bl[0],ztQtchi_bl[0]).subs(chi_bl[1],ztQtchi_bl[1]))[0]

#twoILiedsigmapzztzmrHsigma=2*I*(sum([(zeta_bu.T*gamma_mu[d]*zetat_bl)[0]*D_scalar(sigma)[d] for d in range(3)])+(zeta_bu.T*zetat_bl)[0]*(z-r*H)*sigma)


#--- lambda ---
#zQztQtpztQtzQlambda=Matrix([ztQtlambda_bl[i] + subsDiffZt( zQlambda_bl[i].subs(D,ztQtD).subs(sigma,ztQtsigma).subs(a_ml[0],ztQta_ml[0]).subs(a_ml[1],ztQta_ml[1]).subs(a_ml[2],ztQta_ml[2]) ) for i in range(2)])

#twoILiedlambdapzztzmrHlambda=2*I*(Liederiv_spinor_low([(zeta_bu.T*gamma_mu[i]*zetat_bl)[0] for i in range(3)],lambda_bl)+sum([(zeta_bu.T*gamma_mu[d]*zetat_bl)[0]*(-I*r*(A_ml[d]-Rational(1,2)*V_ml[d])-I*z*C_ml[d]) for d in range(3)])*lambda_bl+(zeta_bu.T*zetat_bl)[0]*(z-r*H)*lambda_bl)


#--- lambda-tilde ---
#zQztQtpztQtzQlambdat=Matrix([subsDiffZ( ztQtlambdat_bl[i].subs(D,zQD).subs(sigma,zQsigma).subs(a_ml[0],zQa_ml[0]).subs(a_ml[1],zQa_ml[1]).subs(a_ml[2],zQa_ml[2]) ) + zQlambdat_bl[i] for i in range(2)])

#twoILiedlambdatpzztzmrHlambdat=2*I*(Liederiv_spinor_low([(zeta_bu.T*gamma_mu[i]*zetat_bl)[0] for i in range(3)],lambdat_bl)+sum([(zeta_bu.T*gamma_mu[d]*zetat_bl)[0]*(-I*r*(A_ml[d]-Rational(1,2)*V_ml[d])-I*z*C_ml[d]) for d in range(3)])*lambdat_bl+(zeta_bu.T*zetat_bl)[0]*(z-r*H)*lambdat_bl)


#--- D ---
#zQztQtpztQtzQD=(ztQtD.subs(lambda_bl[0],zQlambda_bl[0]).subs(lambda_bl[1],zQlambda_bl[1]).subs(chit_bl[0],zQchit_bl[0]).subs(chit_bl[1],zQchit_bl[1])+zQD.subs(lambdat_bl[0],ztQtlambdat_bl[0]).subs(lambdat_bl[1],ztQtlambdat_bl[1]).subs(chi_bl[0],ztQtchi_bl[0]).subs(chi_bl[1],ztQtchi_bl[1]))
#zQztQtpztQtzQD=subsDiffZ(zQztQtpztQtzQD)
#zQztQtpztQtzQD=subsDiffZt(zQztQtpztQtzQD)

#twoILiedDpzztzmrHD=2*I*(sum([(zeta_bu.T*gamma_mu[d]*zetat_bl)[0]*D_scalar(D)[d] for d in range(3)])+(zeta_bu.T*zetat_bl)[0]*(z-r*H)*D)

#zeroOfD=simplify(zQztQtpztQtzQD - twoILiedDpzztzmrHD)


#.subs(zeta_bl[0].diff(x_mu[0]),diffz[0][0]).subs(zeta_bl[1].diff(x_mu[0]),diffz[0][1]).subs(zeta_bl[0].diff(x_mu[1]),diffz[1][0]).subs(zeta_bl[1].diff(x_mu[1]),diffz[1][1]).subs(zeta_bl[0].diff(x_mu[2]),diffz[2][0]).subs(zeta_bl[1].diff(x_mu[2]),diffz[2][1]).subs(zetat_bl[0].diff(x_mu[0]),diffzt[0][0]).subs(zetat_bl[1].diff(x_mu[0]),diffzt[0][1]).subs(zetat_bl[0].diff(x_mu[1]),diffzt[1][0]).subs(zetat_bl[1].diff(x_mu[1]),diffzt[1][1]).subs(zetat_bl[0].diff(x_mu[2]),diffzt[2][0]).subs(zetat_bl[1].diff(x_mu[2]),diffzt[2][1])
#zQztQtpztQtzQD=subsDiffZt(subsDiffZ(ztQtD.subs(lambda_bl[0],zQlambda_bl[0]).subs(lambda_bl[1],zQlambda_bl[1]).subs(chit_bl[0],zQchit_bl[0]).subs(chit_bl[1],zQchit_bl[1])+zQD.subs(lambdat_bl[0],ztQtlambdat_bl[0]).subs(lambdat_bl[1],ztQtlambdat_bl[1]).subs(chi_bl[0],ztQtchi_bl[0]).subs(chi_bl[1],ztQtchi_bl[1])))


if __name__ == "__main__":
	print("result:",end="")
	print(zeroOfchi)







