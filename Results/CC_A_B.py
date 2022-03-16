import numpy as np


C12w = 2.634129e-06
C6w = 2.617346e-03

C12 = [0.000000e+00, 5.062500e-06, 0.000000e+00, 9.702250e-05,
       2.664624e-05, 4.937284e-06, 1.000000e-06, 1.505529e-06, 0.000000e+00]
C6 = [0.000000e+00, 2.436410e-03, 0.000000e+00, 6.068410e-03,
      9.613802e-03, 2.340624e-03, 2.261954e-03, 2.261954e-03, 0.000000e+00]

# C_i_arrys =[H1,N,h2,CA,CB,C,O1,O2,H] for 1 ALA.
# C_i_arrys (IAC codes) =[21,7,21,14,16,12,1,3,21] for 1 ALA.

C12_i = np.zeros(len(C12))
C6_i = np.zeros(len(C12))
sigma_i = np.zeros(len(C12))
epsilon_i = np.zeros(len(C12))
r_min_i = np.zeros(len(C12))

for i in range(len(C12)):

    if C12[i] != 0.000000e+00:

        C12_i[i] = np.sqrt(C12[i] * C12w)
        C6_i[i] = np.sqrt((C6[i]) * C6w)
        sigma_i[i] = (C12_i[i] / C6_i[i])**(1. / 6)
        epsilon_i[i] = (C6_i[i]**2) / (4 * C12_i[i])
        r_min_i[i] = 2**(1. / 6) * sigma_i[i]

    else:
        next

#print(r_min_i)


r_min_CC = [0, 2.00482952, 0,         2.81692053, 2.10344808, 2.00986897,
             1.54903433, 1.65834886, 0.]

print(r_min_i * 10 - r_min_CC)
