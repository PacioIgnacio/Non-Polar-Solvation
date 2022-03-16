import glob
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True

#--- Data

data1 = np.loadtxt(
    "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/05ALA/extended/L01_v1/Interaction_test.dat", delimiter=",")

x1 = data1[:, 0]
vdw_pp = data1[:, 1]
vdw_pp_err = data1[:, 2]
vdw_ps = data1[:, 3]
vdw_ps_err = data1[:, 4]
vdw_ss = data1[:, 5]
vdw_ss_err = data1[:, 6]
coul_pp = data1[:, 7]
coul_pp_err = data1[:, 8]
coul_ps = data1[:, 9]
coul_ps_err = data1[:, 10]
coul_ss = data1[:, 11]
coul_ss_err = data1[:, 12]

#--- Plots


fig1, (ax1) = plt.subplots(1, 1)
fig2, (ax2) = plt.subplots(1, 1)
fig3, (ax3) = plt.subplots(1, 1)

# 1st plot

ax1.plot(x1, vdw_ps, color='k', label="Peptide-Solvent VdW", linewidth=1)
#plt.errorbar(x, vdw_ps, yerr=vdw_ps_err, fmt=" ", barsabove=False)
ax1.plot(x1, vdw_pp, linestyle="--", color='red',
         label="Peptide-Peptide VdW", linewidth=1)
ax1.plot(x1, coul_ps, linestyle="--", color='blue',
         label="Peptide-Solvent Coul", linewidth=1)

ax1.set_title(
    "Peptide Energy Interactions: Penta-Alanine extended", fontsize=18)
ax1.set_ylabel("VdW - Coulomb Interaction " + r"$[kJ/mol]$", fontsize=18)
ax1.set_xlabel(r'$\lambda$', fontsize=15)
ax1.legend(loc="lower right")

# 2nd plot

ax2.set_title(
    "Solvent-Solvent van der Waals Interactions", fontsize=18)
ax2.plot(x1, vdw_ss, label="Solvent-Solvent VdW", color="black", linewidth=1)
ax2.set_ylabel("Van der Waals Interaction " +
               r"$[kJ/mol]$", fontsize=18)
ax2.set_xlabel(r'$\lambda$', fontsize=15)
ax2.legend(loc="lower left")

# 3rd plot
ax3.set_title(
    "Solvent-Solvent Coulomb Interactions", fontsize=18)
ax3.plot(x1, coul_ss, label="Solvent-Solvent Coulomb", color="y")
ax3.set_ylabel("Coulomb Interaction " +
               r"$[kJ/mol]$", fontsize=18)
ax3.set_xlabel(r'$\lambda$', fontsize=15)
ax3.legend(loc="upper right")

plt.tight_layout()

fig1.savefig("/home/ignacio/CINV/Memoria/Figures/CH6/Interactions.png")
fig2.savefig(
    "/home/ignacio/CINV/Memoria/Figures/CH6/Solvent_vdw_Interactions.png")
fig3.savefig(
    "/home/ignacio/CINV/Memoria/Figures/CH6/Solvent_coul_Interactions.png")

plt.show()
