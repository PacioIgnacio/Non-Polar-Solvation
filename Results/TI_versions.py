import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['text.usetex'] = True

data_1 = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/10ALA/Comandos/TI_nALA/TI_1ALA/L01_v1/dHdl.dat")
data_2 = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/10ALA/Comandos/TI_nALA/TI_1ALA/L01_v2/dHdl.dat")
data_3 = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/10ALA/Comandos/TI_nALA/TI_1ALA/L01_v3/dHdl.dat")
data_4 = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/10ALA/Comandos/TI_nALA/TI_1ALA/L01_v4/dHdl.dat")
data_5 = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/01ALA/helix/L01_v2/dHdl_test.dat", delimiter=",")

#---DATA

x1 = data_1[:, 0]
y1 = data_1[:, 1]
y1_err_2 = data_1[:, 2]
y1_err = np.nan_to_num(y1_err_2)

x2 = data_2[:, 0]
y2 = data_2[:, 1]
y2_err_2 = data_2[:, 2]
y2_err = np.nan_to_num(y2_err_2)

x3 = data_3[:, 0]
y3 = data_3[:, 1]
y3_err_2 = data_3[:, 2]
y3_err = np.nan_to_num(y3_err_2)

x4 = data_4[:, 0]
y4 = data_4[:, 1]
y4_err_2 = data_4[:, 2]
y4_err = np.nan_to_num(y4_err_2)

x5 = data_5[:, 0]
y5 = data_5[:, 1]
y5_err_2 = data_5[:, 2]
y5_err = np.nan_to_num(y5_err_2)


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

    return integralAve, integralStd

#--- Plot


fig1, axs = plt.subplots(nrows=3, ncols=2, sharex=True, figsize=(10, 9))
fig1.suptitle(
    "Thermodynamic evolition for mono-alanine helix configuration", fontsize=20)
axs[0, 0].plot(x1, y1, linewidth=1)
axs[0, 0].errorbar(x1, y1, y1_err, color='k', linewidth=1, marker='o',
                   mfc='none', markersize=5, markeredgewidth=0.5)
axs[0, 0].set_title('Thermodinamic Integration v.1', fontsize=20)
axs[0, 0].set(
    ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')

axs[1, 0].plot(x2, y2, linewidth=1)
axs[1, 0].errorbar(x2, y2, y2_err, color='k', linewidth=1, marker='o',
                   mfc='none', markersize=5, markeredgewidth=0.5)
axs[1, 0].set_title('Thermodinamic Integration v.2', fontsize=20)
axs[1, 0].set(
    ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')

axs[2, 0].plot(x3, y3, linewidth=1)
axs[2, 0].errorbar(x3, y3, y3_err, color='k', linewidth=1, marker='o',
                   mfc='none', markersize=5, markeredgewidth=0.5)
axs[2, 0].set_title('Thermodinamic Integration v.3', fontsize=20)
axs[2, 0].set(xlabel=r'$\lambda$',
              ylabel=r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$')


axs[0, 1].plot(x4, y4, linewidth=1)
axs[0, 1].errorbar(x4, y4, y4_err, color='k', linewidth=1, marker='o',
                   mfc='none', markersize=5, markeredgewidth=0.5)
axs[0, 1].set_title('Thermodinamic Integration v.4', fontsize=20)


axs[1, 1].plot(x5, y5, linewidth=1)
axs[1, 1].errorbar(x5, y5, y5_err, color='k', linewidth=1, marker='o',
                   mfc='none', markersize=5, markeredgewidth=0.5)
axs[1, 1].set_title('Thermodinamic Integration v.5', fontsize=20)
axs[1, 1].set(xlabel=r'$\lambda$')

axs[1, 1].tick_params(labelbottom=True)

fig1.delaxes(axs[2, 1])

fig1.savefig("/home/ignacio/CINV/Memoria/Figures/CH7/TI_evolution")
plt.tight_layout()
plt.show()
