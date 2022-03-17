import glob
import numpy as np
import matplotlib.pyplot as plt
from natsort import natsorted

# Define n-Alanine number
nALA = 2

files = natsorted(glob.glob("L_*"))

lamb_points = []
lamb_values = []

avg_free = []
err_free = []

e_pp_vdw = []
eppvdw_err = []
e_ps_vdw = []
epsvdw_err = []
e_ss_vdw = []
essvdw_err = []
e_pp_coul = []
eppcoul_err = []
e_ps_coul = []
epscoul_err = []
e_ss_coul = []
esscoul_err = []


with open("dHdl_test.dat", "w") as f:
    # f.write("#lambda    dvdl    dvdl_err\n")
    f.write("#lambda,dvdl,dvdl_err\n")

    with open("Interaction_test.dat", "w") as g:
        g.write("#lambda,e_pp_vdw,eppvdw_err,e_ps_vdw,epsvdw_err,e_ss_vdw,essvdw_err,e_pp_coul,eppcoul_err,e_ps_coul,epscoul_err,e_ss_coul,esscoul_err\n")

        i = 0
        for file in files:

            names = "{:.3f}".format(float(file[2:]))
            values = float(file[2:])

            lamb_points.append(names)
            lamb_values.append(values)

            with open("L_" + str(names) + "/ene_ana.out", "r") as rf:
                next(rf)
                for line in rf:
                    avg_free.append(line.split()[1])
                    err_free.append(line.split()[3])

            # f.write(str(names) + "    " +
            #         avg_free[i] + "    " + err_free[i] + "\n")

            f.write(str(names) + "," +
                    avg_free[i] + "," + err_free[i] + "\n")

            with open("L_" + str(names) + "/ene_ana_inte.out", "r") as rg:
                next(rg)
                j = 1
                for line in rg:
                    if j == 1:
                        e_pp_vdw.append(line.split()[1])
                        eppvdw_err.append(line.split()[3])

                    if j == 2:
                        e_ps_vdw.append(line.split()[1])
                        epsvdw_err.append(line.split()[3])

                    if j == 3:
                        e_ss_vdw.append(line.split()[1])
                        essvdw_err.append(line.split()[3])

                    if j == 4:
                        e_pp_coul.append(line.split()[1])
                        eppcoul_err.append(line.split()[3])

                    if j == 5:
                        e_ps_coul.append(line.split()[1])
                        epscoul_err.append(line.split()[3])

                    if j == 6:
                        e_ss_coul.append(line.split()[1])
                        esscoul_err.append(line.split()[3])

                    j = j + 1

                g.write(str(names) + "," + e_pp_vdw[i] + "," +
                        eppvdw_err[i] + "," + e_ps_vdw[i] + "," + epsvdw_err[i] +
                        "," + e_ss_vdw[i] + "," + essvdw_err[i] + "," + e_pp_coul[i] +
                        "," + eppcoul_err[i] + "," + e_ps_coul[i] + "," + epscoul_err[i] + "," + e_ss_coul[i] + "," + esscoul_err[i] + "\n")

            i = i + 1


# Read data from text files generated before

data1 = np.loadtxt("Interaction_test.dat", delimiter=",")

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

data2 = np.loadtxt("dHdl_test.dat", delimiter=",")

x2 = data2[:, 0]
y2 = data2[:, 1]
y2_err_2 = data2[:, 2]

# nan values set to 0 correction when needed

y2_err = np.nan_to_num(y2_err_2)


# Free Energy calculation and error propagation


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


Integral, Error = integrate(x2, y2, y2_err)

print("Thermodynamic Results:")
print("\n")
print("Van der Waals Interactions           (\u03BB=0) [kJ/mol]")
print("1.   Peptide-Peptide = ", vdw_pp[0])
print("2.   Solvent-Solvent = ", vdw_ss[0])
print("3.   Peptide-Solvent = ", vdw_ps[0])

print("Van der Waals Interactions           (\u03BB=1) [kJ/mol]")
print("1.   Peptide-Peptide = ", vdw_pp[-1])
print("2.   Solvent-Solvent = ", vdw_ss[-1])
print("3.   Peptide-Solvent = ", vdw_ps[-1])

print("\n")

print("Coulumb Electrostatic Interaction    (\u03BB=0) [kJ/mol] ")
print("1.   Peptide-Solvent = ", coul_ps[0])
print("2.   Solvent-Solvent = ", coul_ss[0])
print("Coulumb Electrostatic Interaction    (\u03BB=1) [kJ/mol] ")
print("1.   Peptide-Solvent = ", coul_ps[-1])
print("2.   Solvent-Solvent = ", coul_ss[-1])


print("\n")
print("\u0394G Total=", Integral, "; Error=", Error)


# Data Plots

plt.style.use("seaborn")


fig1, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(
    8, 15), gridspec_kw={'height_ratios': [1.5, 1, 1]}, sharex=True)

fig2, (ax4, ax5) = plt.subplots(nrows=2, ncols=1, figsize=(
    10, 12), gridspec_kw={'height_ratios': [4, 1]}, sharex=True)


# 1ts plot

ax1.plot(x1, vdw_ps, label="Peptide-Solvent VdW")
#plt.errorbar(x, vdw_ps, yerr=vdw_ps_err, fmt=" ", barsabove=False)
ax1.plot(x1, vdw_pp, linestyle="--", label="Peptide-Peptide VdW")
ax1.plot(x1, coul_ps, linestyle="dotted",
         color="r", label="Peptide-Solvent Coul")

ax1.set_title("Peptide Energy Interactions " +
              str(nALA) + "-ALA", fontsize=15)
ax1.set_ylabel("VdW - Coulomb Interaction " + r"$[kJ/mol]$", fontsize=9)
#ax1.set_xlabel(r'$\lambda$', fontsize=15)
ax1.legend(loc="lower right")

# 2nd plot

ax2.set_title("Solvent Energy Interactions " +
              str(nALA) + "-ALA", fontsize=15)
ax2.plot(x1, vdw_ss, label="Solvent-Solvent VdW", color="black", linewidth=1)
ax2.set_ylabel("Van der Waals Interaction " +
               r"$[kJ/mol]$", fontsize=9)
#ax2.set_xlabel(r'$\lambda$', fontsize=15)
ax2.legend(loc="upper right")

# 3rd plot

ax3.plot(x1, coul_ss, label="Solvent-Solvent Coulomb", color="y")
ax3.set_ylabel("Coulomb Interaction " +
               r"$[kJ/mol]$", fontsize=9)
ax3.set_xlabel(r'$\lambda$', fontsize=15)
ax3.legend(loc="upper right")

# 4th plot

ax4.plot(x2, y2, label="\u0394G= " +
         str("{:.2f}".format(Integral)) + "  ;   Error= " + str("{:.2f}".format(Error)))
ax4.errorbar(x2, y2, y2_err, color='k', linewidth=1, marker='o',
             mfc='none', markersize=7, markeredgewidth=1)
ax4.set_title("Thermodynamic Integration " +
              str(nALA) + "-ALA", fontsize=15)
ax4.set_ylabel(
    r'$\langle\partial H/ \partial \lambda\rangle   [kJ mol^{-1}]$', fontsize=15)
#ax4.set_xlabel(r'$\lambda$', fontsize=15)
ax4.legend(loc="lower left", fontsize=15)  # handlelength=5, handleheight=3

# 5th plot

tol = 2.54
ax5.plot(x2, y2_err, color="r", linewidth=1, label="Statistical error")
ax5.set_ylabel("Error $[kJ mol^{-1}]$", fontsize=12)
ax5.set_xlabel(r'$\lambda$', fontsize=15)
ax5.hlines(y=tol, xmin=0, xmax=1, color="b", ls="--", linewidth=1)


plt.tight_layout()
plt.show()
