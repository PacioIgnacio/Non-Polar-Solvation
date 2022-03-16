import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['text.usetex'] = True

#---helix structures

data_1_helix = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/01ALA/helix/L01_v2/dHdl_test.dat", delimiter=",")
data_2_helix = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/02ALA/helix/L01_v2/dHdl_test.dat", delimiter=",")
data_3_helix = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/03ALA/helix/L01_v2/dHdl_test.dat", delimiter=",")
data_4_helix = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/04ALA/helix/L01_v2/dHdl_test.dat", delimiter=",")
data_5_helix = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/05ALA/helix/L01_v2/dHdl_test.dat", delimiter=",")
data_6_helix = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/06ALA/helix/L01_v2/dHdl_test.dat", delimiter=",")
data_7_helix = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/07ALA/helix/L01_v2/dHdl_test.dat", delimiter=",")
data_8_helix = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/08ALA/helix/L01_v2/dHdl_test.dat", delimiter=",")
data_9_helix = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/09ALA/helix/L01_v2/dHdl_test.dat", delimiter=",")
data_10_helix = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/10ALA/helix/L01_v2/dHdl_test.dat", delimiter=",")

#---extended structures

data_1_ext = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/01ALA/extended/L01_v1/dHdl_test.dat", delimiter=",")
data_2_ext = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/02ALA/extended/L01_v1/dHdl_test.dat", delimiter=",")
data_3_ext = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/03ALA/extended/L01_v1/dHdl_test.dat", delimiter=",")
data_4_ext = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/04ALA/extended/L01_v1/dHdl_test.dat", delimiter=",")
data_5_ext = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/05ALA/extended/L01_v1/dHdl_test.dat", delimiter=",")
data_6_ext = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/06ALA/extended/L01_v1/dHdl_test.dat", delimiter=",")
data_7_ext = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/07ALA/extended/L01_v1/dHdl_test.dat", delimiter=",")
data_8_ext = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/08ALA/extended/L01_v1/dHdl_test.dat", delimiter=",")
data_9_ext = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/09ALA/extended/L01_v1/dHdl_test.dat", delimiter=",")
data_10_ext = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/10ALA/extended/L01_v3/dHdl_test.dat", delimiter=",")


def uncAddition(A=1., B=1., sigmaA=0., sigmaB=0., a=1., b=1., sigmaAB=0.):
    f = (a * A) + (b * B)
    sigmaf = np.sqrt((a * sigmaA)**2
                     + (b * sigmaB)**2
                     + (2 * a * b * sigmaAB))
    return f, sigmaf


def integrate(x, data, errors):
    # Data: is ab nx1 array that contains n number of f values
    # while errors contains  their absolute standard deviation
    # x:    is the independent variable of the f values
    # Obviously x and f should have the same number of rows
    integralAve = 0.
    integralStd = 0.
    for i in range(1, len(data)):
        trapzPartAve, trapzPartStd = uncAddition(A=data[i - 1],
                                                 sigmaA=errors[i - 1],
                                                 a=(x[i] - x[i - 1]) / 2.0,
                                                 B=data[i],
                                                 sigmaB=errors[i],
                                                 b=(x[i] - x[i - 1]) / 2.0)
        integralAve += trapzPartAve
        integralStd += trapzPartStd

    return integralAve  # , integralStd


#--- Data plots.

fig1, axs = plt.subplots(4, 2, sharex=True, figsize=(8, 12))
fig2, axs1 = plt.subplots(4, 2, sharex=True, figsize=(8, 12))
fig3, axs2 = plt.subplots(4, 2, sharex=True, figsize=(8, 12))

axs[0, 0].plot(data_1_helix[:, 0], data_1_helix[:, 1], label="$\Delta G$= " + str("{:.2f}".format(integrate(data_1_helix[:, 0], data_1_helix[:, 1], data_1_helix[:, 2]))),
               color='k', linewidth=1, marker='o', markersize=1.5)
axs[0, 0].set(
    ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')
axs[0, 0].set_title('Thermodinamic Integration 1-ALA, Helix', fontsize=11)
axs[0, 0].legend(loc="lower left")

axs[1, 0].plot(data_2_helix[:, 0], data_2_helix[:, 1], label="$\Delta G$= " + str("{:.2f}".format(integrate(data_2_helix[:, 0], data_2_helix[:, 1], data_2_helix[:, 2]))),
               color='k', linewidth=1, marker='o', markersize=1.5)
axs[1, 0].set(
    ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')
axs[1, 0].set_title('Thermodinamic Integration 2-ALA, Helix', fontsize=11)
axs[1, 0].legend(loc="lower left")

axs[2, 0].plot(data_3_helix[:, 0], data_3_helix[:, 1], label="$\Delta G$= " + str("{:.2f}".format(integrate(data_3_helix[:, 0], data_3_helix[:, 1], data_3_helix[:, 2]))),
               color='k', linewidth=1, marker='o', markersize=1.5)
axs[2, 0].set(
    ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')
axs[2, 0].set_title('Thermodinamic Integration 3-ALA, Helix', fontsize=11)
axs[2, 0].legend(loc="lower left")

axs[3, 0].plot(data_4_helix[:, 0], data_4_helix[:, 1], label="$\Delta G$= " + str("{:.2f}".format(integrate(data_4_helix[:, 0], data_4_helix[:, 1], data_4_helix[:, 2]))),
               color='k', linewidth=1, marker='o', markersize=1.5)
axs[3, 0].set(
    ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')
axs[3, 0].set_title('Thermodinamic Integration 4-ALA, Helix', fontsize=11)
axs[3, 0].legend(loc="lower left")
axs[3, 0].set(xlabel=r'$\lambda$')

axs[0, 1].plot(data_5_helix[:, 0], data_5_helix[:, 1], label="$\Delta G$= " + str("{:.2f}".format(integrate(data_5_helix[:, 0], data_5_helix[:, 1], data_5_helix[:, 2]))),
               color='k', linewidth=1, marker='o', markersize=1.5)
#axs[0, 1].set(ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')
axs[0, 1].set_title('Thermodinamic Integration 5-ALA, Helix', fontsize=11)
axs[0, 1].legend(loc="lower left")

axs[1, 1].plot(data_6_helix[:, 0], data_6_helix[:, 1], label="$\Delta G$= " + str("{:.2f}".format(integrate(data_6_helix[:, 0], data_6_helix[:, 1], data_6_helix[:, 2]))),
               color='k', linewidth=1, marker='o', markersize=1.5)
#axs[1, 1].set(ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')
axs[1, 1].set_title('Thermodinamic Integration 6-ALA, Helix', fontsize=11)
axs[1, 1].legend(loc="lower left")

axs[2, 1].plot(data_7_helix[:, 0], data_7_helix[:, 1], label="$\Delta G$= " + str("{:.2f}".format(integrate(data_7_helix[:, 0], data_7_helix[:, 1], data_7_helix[:, 2]))),
               color='k', linewidth=1, marker='o', markersize=1.5)
#axs[2, 1].set(ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')
axs[2, 1].set_title('Thermodinamic Integration 7-ALA, Helix', fontsize=11)
axs[2, 1].legend(loc="lower left")

axs[3, 1].plot(data_8_helix[:, 0], data_8_helix[:, 1], label="$\Delta G$= " + str("{:.2f}".format(integrate(data_8_helix[:, 0], data_8_helix[:, 1], data_8_helix[:, 2]))),
               color='k', linewidth=1, marker='o', markersize=1.5)
#axs[3, 1].set(ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')
axs[3, 1].set_title('Thermodinamic Integration 8-ALA, Helix', fontsize=11)
axs[3, 1].legend(loc="lower left")
axs[3, 1].set(xlabel=r'$\lambda$')

plt.tight_layout()

#---

axs1[0, 0].plot(data_9_helix[:, 0], data_9_helix[:, 1], label="$\Delta G$= " + str("{:.2f}".format(integrate(data_9_helix[:, 0], data_9_helix[:, 1], data_9_helix[:, 2]))),
                color='k', linewidth=1, marker='o', markersize=1.5)
axs1[0, 0].set(
    ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')
axs1[0, 0].set_title('Thermodinamic Integration 9-ALA, Helix', fontsize=11)
axs1[0, 0].legend(loc="lower left")

axs1[1, 0].plot(data_10_helix[:, 0], data_10_helix[:, 1], label="$\Delta G$= " + str("{:.2f}".format(integrate(data_10_helix[:, 0], data_10_helix[:, 1], data_10_helix[:, 2]))),
                color='k', linewidth=1, marker='o', markersize=1.5)
axs1[1, 0].set(
    ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')
axs1[1, 0].set_title('Thermodinamic Integration 10-ALA, Helix', fontsize=11)
axs1[1, 0].legend(loc="lower left")

axs1[2, 0].plot(data_1_ext[:, 0], data_1_ext[:, 1], label="$\Delta G$= " + str("{:.2f}".format(integrate(data_1_ext[:, 0], data_1_ext[:, 1], data_1_ext[:, 2]))),
                color='k', linewidth=1, marker='o', markersize=1.5)
axs1[2, 0].set(
    ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')
axs1[2, 0].set_title('Thermodinamic Integration 1-ALA, Extended', fontsize=11)
axs1[2, 0].legend(loc="lower left")

axs1[3, 0].plot(data_2_ext[:, 0], data_2_ext[:, 1], label="$\Delta G$= " + str("{:.2f}".format(integrate(data_2_ext[:, 0], data_2_ext[:, 1], data_2_ext[:, 2]))),
                color='k', linewidth=1, marker='o', markersize=1.5)
axs1[3, 0].set(
    ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')
axs1[3, 0].set_title('Thermodinamic Integration 2-ALA, Extended', fontsize=11)
axs1[3, 0].legend(loc="lower left")
axs1[3, 0].set(xlabel=r'$\lambda$')

axs1[0, 1].plot(data_3_ext[:, 0], data_3_ext[:, 1], label="$\Delta G$= " + str("{:.2f}".format(integrate(data_3_ext[:, 0], data_3_ext[:, 1], data_3_ext[:, 2]))),
                color='k', linewidth=1, marker='o', markersize=1.5)
# axs1[0, 1].set(
#     ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')
axs1[0, 1].set_title('Thermodinamic Integration 3-ALA, Extended', fontsize=11)
axs1[0, 1].legend(loc="lower left")

axs1[1, 1].plot(data_4_ext[:, 0], data_4_ext[:, 1], label="$\Delta G$= " + str("{:.2f}".format(integrate(data_4_ext[:, 0], data_4_ext[:, 1], data_4_ext[:, 2]))),
                color='k', linewidth=1, marker='o', markersize=1.5)
# axs1[1, 1].set(
#     ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')
axs1[1, 1].set_title('Thermodinamic Integration 4-ALA, Extended', fontsize=11)
axs1[1, 1].legend(loc="lower left")

axs1[2, 1].plot(data_5_ext[:, 0], data_5_ext[:, 1], label="$\Delta G$= " + str("{:.2f}".format(integrate(data_5_ext[:, 0], data_5_ext[:, 1], data_5_ext[:, 2]))),
                color='k', linewidth=1, marker='o', markersize=1.5)
# axs1[0, 1].set(
#     ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')
axs1[2, 1].set_title('Thermodinamic Integration 5-ALA, Extended', fontsize=11)
axs1[2, 1].legend(loc="lower left")

axs1[3, 1].plot(data_6_ext[:, 0], data_6_ext[:, 1], label="$\Delta G$= " + str("{:.2f}".format(integrate(data_6_ext[:, 0], data_6_ext[:, 1], data_6_ext[:, 2]))),
                color='k', linewidth=1, marker='o', markersize=1.5)
# axs1[1, 1].set(
#     ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')
axs1[3, 1].set_title('Thermodinamic Integration 6-ALA, Extended', fontsize=11)
axs1[3, 1].legend(loc="lower left")
axs1[3, 1].set(xlabel=r'$\lambda$')

#---

axs2[0, 0].plot(data_7_ext[:, 0], data_7_ext[:, 1], label="$\Delta G$= " + str("{:.2f}".format(integrate(data_7_ext[:, 0], data_7_ext[:, 1], data_7_ext[:, 2]))),
                color='k', linewidth=1, marker='o', markersize=1.5)
axs2[0, 0].set(
    ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')
axs2[0, 0].set_title('Thermodinamic Integration 7-ALA, Extended', fontsize=11)
axs2[0, 0].legend(loc="lower left")

axs2[1, 0].plot(data_8_ext[:, 0], data_8_ext[:, 1], label="$\Delta G$= " + str("{:.2f}".format(integrate(data_8_ext[:, 0], data_8_ext[:, 1], data_8_ext[:, 2]))),
                color='k', linewidth=1, marker='o', markersize=1.5)
axs2[1, 0].set(
    ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')
axs2[1, 0].set_title('Thermodinamic Integration 8-ALA, Extended', fontsize=11)
axs2[1, 0].legend(loc="lower left")

axs2[2, 0].plot(data_9_ext[:, 0], data_9_ext[:, 1], label="$\Delta G$= " + str("{:.2f}".format(integrate(data_9_ext[:, 0], data_9_ext[:, 1], data_9_ext[:, 2]))),
                color='k', linewidth=1, marker='o', markersize=1.5)
axs2[2, 0].set(
    ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')
axs2[2, 0].set_title('Thermodinamic Integration 9-ALA, Extended', fontsize=11)
axs2[2, 0].legend(loc="lower left")

axs2[3, 0].plot(data_10_ext[:, 0], data_10_ext[:, 1], label="$\Delta G$= " + str("{:.2f}".format(integrate(data_10_ext[:, 0], data_10_ext[:, 1], data_10_ext[:, 2]))),
                color='k', linewidth=1, marker='o', markersize=1.5)
axs2[3, 0].set(
    ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')
axs2[3, 0].set_title('Thermodinamic Integration 10-ALA, Extended', fontsize=11)
axs2[3, 0].legend(loc="lower left")
axs2[3, 1].set(xlabel=r'$\lambda$')

fig3.delaxes(axs2[0, 1])
fig3.delaxes(axs2[1, 1])
fig3.delaxes(axs2[2, 1])
fig3.delaxes(axs2[3, 1])


plt.tight_layout()

fig1.savefig("/home/ignacio/CINV/Memoria/Figures/CH7/TI_curves_1")
fig2.savefig("/home/ignacio/CINV/Memoria/Figures/CH7/TI_curves_2")
fig3.savefig("/home/ignacio/CINV/Memoria/Figures/CH7/TI_curves_3")


plt.show()
