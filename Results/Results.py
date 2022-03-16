import numpy as np
import matplotlib.pyplot as plt
import csv
plt.rcParams['text.usetex'] = True


def sasa_model(a):  # SASA value in [\ams2]

    b = -4  # [kcal/mol]
    gamma = 0.025  # [kcal/mol ang2]

 #  DG = gamma * (4.184 / 10e-2) * a + b * (4.184)
    DG = gamma * a + b

    return DG


def G_final(a):
    G_non_polar = a * -1  # [kJ/mol] to [kcal/mol]

    return G_non_polar  # [kcal/mol]


#--- Results.csv

data = np.loadtxt("/home/ignacio/CINV/Memoria/Results.csv",
                  skiprows=1, delimiter=",")

x = data[:, 0]
G_ext = data[:, 1] / 4.184
G_ext_err = data[:, 2]
sasa_ext = data[:, 3]
G_helix = data[:, 4] / 4.184
G_helix_err = data[:, 5]
sasa_helix = data[:, 6]
dG_cav_ext = data[:, 7]
dG_disp_ext = data[:, 8]
sasa_ext_CC = data[:, 9]
dG_cav_helix = data[:, 10]
dG_disp_helix = data[:, 11]
sasa_helix_CC = data[:, 12]

dG_i_ext = dG_cav_ext + dG_disp_ext
dG_i_helix = dG_cav_helix + dG_disp_helix

dG_sasa_ext = sasa_model(sasa_ext_CC) + dG_disp_ext
dG_sasa_helix = sasa_model(sasa_helix_CC) + dG_disp_helix

data_1 = np.loadtxt('/home/ignacio/CINV/Memoria/CC_m_helix',
                    skiprows=1, delimiter=",")
dG_CC_helix = data_1[:, 1]

data_2 = np.loadtxt('/home/ignacio/CINV/Memoria/CC_m_extended',
                    skiprows=1, delimiter=",")

dG_CC_ext = data_2[:, 1]

# --- Statistical Mesures

#--- RMSD


def rmsd(a, b):
    ext_sum_i = 0

    for i in range(10):

        ext_i = (a[i] - b[i])**2
        ext_sum_i = ext_sum_i + ext_i

    rmsd = np.sqrt(ext_sum_i / len(a))

    return (rmsd)


def rmsd_total(a, b, c, d):
    ext_sum_i = 0
    helix_sum_i = 0

    for i in range(10):

        ext_i = (a[i] - b[i])**2
        ext_sum_i = ext_sum_i + ext_i

        helix_i = (c[i] - d[i])**2
        helix_sum_i = helix_sum_i + helix_i

    rmsd = np.sqrt((ext_sum_i + helix_sum_i) / (len(a) * 2))

    return rmsd
#--- R2


def R2(a, b):
    correlation_matrix = np.corrcoef(a, b)
    correlation_xy = correlation_matrix[0, 1]
    r_squared = correlation_xy**2

    return r_squared

#--- Pearson coef.


def pearson_coef(a, b):
    pearson_coef = np.corrcoef(a, b)

    return pearson_coef


print('Implicit Extended RMSD  = %1.3f ' % rmsd(G_ext, dG_CC_ext))
print('Implicit Extended R2 = %1.3f ' % R2(G_ext, dG_CC_ext))
print('Implicit Extended Pearson = %1.3f' %
      pearson_coef(G_ext, dG_CC_ext)[0, 1] + '\n')

print('Implicit Helix RMSD  = %1.3f ' % rmsd(G_helix, dG_CC_helix))
print('Implicit Helix R2 = %1.3f ' % R2(G_helix, dG_CC_helix))
print('Implicit Helix Pearson = %1.3f' %
      pearson_coef(G_helix, dG_CC_helix)[0, 1] + '\n')

print('SASA Extended RMSD  = %1.3f ' % rmsd(G_ext, dG_sasa_ext))
print('SASA Extended R2 = %1.3f ' % R2(G_ext, dG_sasa_ext))
print('SASA Extended Pearson = %1.3f' %
      pearson_coef(G_ext, dG_sasa_ext)[0, 1] + '\n')

print('SASA Helix RMSD  = %1.3f ' % rmsd(G_helix, dG_sasa_helix))
print('SASA Helix R2 = %1.3f ' % R2(G_helix, dG_sasa_helix))
print('SASA Helix Pearson = %1.3f' %
      pearson_coef(G_ext, dG_sasa_helix)[0, 1] + '\n')

print('Implicit RMSD total = %1.3f' %
      rmsd_total(G_ext, dG_CC_ext, G_helix, dG_CC_helix))
print('SASA RMSD total = %1.3f' % rmsd_total(
    G_ext, dG_sasa_ext, G_helix, dG_sasa_helix) + '\n')

print('Improve = %1.2f ' % (rmsd_total(G_ext, dG_sasa_ext, G_helix, dG_sasa_helix) - rmsd_total(G_ext,
                                                                                                dG_i_ext, G_helix, dG_i_helix) / np.max(rmsd_total(G_ext, dG_sasa_ext, G_helix, dG_sasa_helix))) + '%')

#--- Data plots

fig1, ax1 = plt.subplots(figsize=(8, 6))
fig2, ax2 = plt.subplots(figsize=(8, 6))
fig3, ax3 = plt.subplots(figsize=(8, 6))
fig4, (ax4_1, ax4_2) = plt.subplots(1, 2, figsize=(8, 6), sharey=True)
fig5, (ax5_1, ax5_2) = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

ax1.set_title(
    "Gibbs Free Energy -$\Delta G_{non-polar}$ / Alanine", fontsize=18)
ax1.plot(x, G_helix, color='k', marker=".", label="Helix", linewidth=1)
ax1.plot(x, G_ext, color='red', marker="v", label="Extended", linewidth=1)
ax1.set_ylabel("-$\Delta G_{non-polar}$  " + r"$[kJ mol^{-1}]$", fontsize=18)
ax1.set_xlabel("n-ALA", fontsize=18)

#---


ax2.set_title(
    "Gibbs Free Energy $\Delta G_{non-polar}$ / Alanine HELIX", fontsize=18)
ax2.plot(x, G_final(G_helix), marker=".", label="Explicit", linewidth=1)
ax2.plot(x, dG_sasa_helix, marker="v",
         label="SASA Implicit Model", linewidth=1)
# ax2.plot(x, sasa_model(sasa_helix * 100) + dG_disp_helix, marker="^",
#          label="SASA GROMOS Model", linewidth=1)
ax2.plot(x, dG_disp_helix + dG_cav_helix, marker="d",
         label="Implicit Model", linewidth=1)
ax2.set_ylabel("$\Delta G_{non-polar}$  " + r"$[kcal / mol]$", fontsize=18)
ax2.set_xlabel("n-ALA", fontsize=18)

ax3.set_title(
    "Gibbs Free Energy $\Delta G_{non-polar}$ / Alanine EXTENDED", fontsize=18)
ax3.plot(x, G_final(G_ext), marker=".", label="Explicit", linewidth=1)
ax3.plot(x, dG_sasa_ext, marker="^",
         label="SASA Model", linewidth=1)
# ax3.plot(x, sasa_model(sasa_ext * 100) + dG_disp_ext, marker="^",
#          label="SASA GROMOS Model", linewidth=1)
ax3.plot(x, dG_disp_ext + dG_cav_ext, marker="d",
         label="Implicit Model", linewidth=1)
ax3.set_ylabel("$\Delta G_{non-polar}$  " + r"$[kcal / mol]$", fontsize=18)
ax3.set_xlabel("n-ALA", fontsize=18)

fig4.suptitle('SASA factor generated with GROMOS and msms', fontsize=18)

ax4_1.set_title('Extended SASA factor', fontsize=16)
ax4_1.plot(x, sasa_ext * 100, marker='s', label='GROMOS SASA Extended')
ax4_1.plot(x, sasa_ext_CC, marker='o', label='Implicit SASA Extended')
ax4_1.set_xlabel("n-ALA", fontsize=18)
ax4_1.set_ylabel('SASA [$\AA^{2}]$', fontsize=18)

ax4_2.set_title('Helix SASA factor', fontsize=16)
ax4_2.plot(x, sasa_helix * 100, marker='^', label='GROMOS SASA Helix')
ax4_2.plot(x, sasa_helix_CC, marker='v', label='Implicit SASA Helix')
ax4_2.set_xlabel("n-ALA", fontsize=18)

ax5_1.set_title(
    "Gibbs Free Energy $\Delta G_{non-polar}$ / Alanine extended", fontsize=18)
ax5_1.plot(x, G_final(G_ext), marker="o", label="Explicit", linewidth=1)
ax5_1.plot(x, dG_CC_ext, marker="s", label="Implicit Model", linewidth=1)
ax5_1.plot(x, dG_sasa_ext, marker="v",
           label="SASA Implicit Model", linewidth=1)
ax5_1.set_xlabel("n-ALA", fontsize=18)
ax5_1.set_ylabel("$\Delta G_{non-polar}$  " + r"$[kcal / mol]$", fontsize=18)

ax5_2.set_title(
    "Gibbs Free Energy $\Delta G_{non-polar}$ / Alanine helix", fontsize=18)
ax5_2.plot(x, G_final(G_helix), marker="o", label="Explicit", linewidth=1)
ax5_2.plot(x, dG_CC_helix, marker="s", label="Implicit Model", linewidth=1)
ax5_2.plot(x, dG_sasa_helix, marker="v",
           label="SASA Implicit Model", linewidth=1)
ax5_2.set_xlabel("n-ALA", fontsize=18)


ax1.grid()
ax2.grid()
ax3.grid()
ax4_1.grid()
ax4_2.grid()
ax5_1.grid()
ax5_2.grid()

fig4.tight_layout()
fig5.tight_layout()

ax1.legend(loc="upper right")
ax2.legend(loc="upper left")
ax3.legend(loc="upper left")
ax4_1.legend(loc="upper left")
ax4_2.legend(loc="upper left")
ax5_1.legend(loc="upper left")
ax5_2.legend(loc="upper left")

fig1.savefig("/home/ignacio/CINV/Memoria/Figures/CH6/results_1.png")
fig2.savefig("/home/ignacio/CINV/Memoria/Figures/CH6/comparison_helix.png")
fig3.savefig("/home/ignacio/CINV/Memoria/Figures/CH6/comparison_extended.png")
fig4.savefig("/home/ignacio/CINV/Memoria/Figures/CH6/SASA_factor.png")
fig5.savefig("/home/ignacio/CINV/Memoria/Figures/CH6/New_CC.png")

plt.show()
