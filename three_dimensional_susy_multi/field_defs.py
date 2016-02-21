from three_dimensional_susy_multi.vars import *

C=Function('C')(*x_mu)
chi_bl=Matrix([-I*Q_bl[i]*C for i in range(2)])

