# execute script in the directory with the L_* folders (lambda pts)

import glob
from natsort import natsorted

i = 0
# number of total actual simulations/job (without pre_sim)
nsim = 5

# change value "nALA" to match tha data for analysis
nALA = 2

namebase = "TI_" + str(nALA) + "ALA_dummy"
topo_dir = "../../../../../topo/" + str(nALA) + "ALA_noC_54a7.top"

files = natsorted(glob.glob("L_*"))

lamb_points = []
lamb_values = []

# Add properties to the list "properties" acording to ene_ana.lib++ propertie names

properties = ["e_pp_vdw", "e_ps_vdw", "e_ss_vdw",
              "e_pp_coul", "e_ps_coul", "e_ss_coul"]

for file in files:

    names = "{:.3f}".format(float(file[2:]))
    values = float(file[2:])

    lamb_points.append(names)
    lamb_values.append(values)

# number of the simulation to analyze = cnt (above pre_sim)
    cnt = 2

    ene_ana_file = "L_" + str(names) + "/ene_ana.inp"
    ene_ana_inte_file = "L_" + str(names) + "/ene_ana_inte.inp"

# ene_ana.inp file related to free energ G.

    with open(ene_ana_file, "w") as ene:
        ene.write(
            "@fr_files ")

        while (cnt <= nsim + 1):
            jobnum = int(round(lamb_values[i] * 10000)) + cnt
            ene.write(namebase + "_" + str(jobnum) + ".trg.gz\n")
            cnt = cnt + 1

        ene.write(
            "@prop dvdl\n"
            "@topo " + topo_dir + "\n"
            "@library ../ene_ana.md++.lib\n"
            "@time 0 0.2\n")

# ene_ana_inte.inp file related to interaction components of H.

    cnt = 2

    with open(ene_ana_inte_file, "w") as inte:

        inte.write("@en_files ")
        while (cnt <= nsim + 1):

            jobnum = int(round(lamb_values[i] * 10000)) + cnt
            inte.write(namebase + "_" + str(jobnum) + ".tre.gz\n")
            cnt = cnt + 1

        inte.write("@prop ")
        for n in range(len(properties)):
            inte.write(properties[n] + " ")
        inte.write("\n")

        inte.write("@topo " + topo_dir + "\n"
                   "@library ../ene_ana.md++.lib\n"
                   "@time 0 0.2\n")

    i = i + 1

with open("runanalysis.csh", "w") as csh:

    csh.write("#!/bin/csh\n#\n"
              "module load gromos++/1.41-openmp\n"
              "module load md++/1.41-openmp\n"

              "foreach x (")

    for lam in lamb_points:

        csh.write(lam + "  ")
    csh.write(")\n\n        echo L_$x\n  cd L_$x\n")

# Comment/UnComment ene_ana files generates in the previous step If ene_ana.inp / ene_ana_inte.inp

    csh.write("ene_ana @f ene_ana.inp > ene_ana.out\n")
    csh.write("ene_ana @f ene_ana_inte.inp > ene_ana_inte.out\n")

    csh.write("        cd ..\nend\n\nexit")

print(lamb_points)
