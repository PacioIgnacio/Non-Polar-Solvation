import numpy as np

Param = [[9, 804, 2421], [15, 933, 2814], [21, 895, 2706], [27, 1037, 3138], [
    33, 1451, 4386], [39, 1927, 5820], [45, 2502, 7551], [51, 3162, 9537], [57, 4014, 12099], [63, 4713, 14202]]
folder = "extended/"

cpu = 2
mem_per_cpu = "2G"

original_imd = "/home/ignacio/DonElias/NPT.Lambda/10ALA/" + \
    folder + "/eq/equilibration.imd"
original_joblist = "/home/ignacio/DonElias/NPT.Lambda/10ALA/" + \
    folder + "/eq/equilibration.jobs"
original_lib = "/home/ignacio/DonElias/NPT.Lambda/10ALA/" + \
    folder + "/eq/mk_script.lib"

for i in range(1, 11):

    if i < 10:

        directory = "0" + str(i) + "ALA/"

    if i == 10:

        directory = "10ALA/"

    mkscript_file = "/home/ignacio/DonElias/NPT.Lambda/" + \
        directory + folder + "eq/eq_mk_script.arg"
    imd_file = "/home/ignacio/DonElias/NPT.Lambda/" + \
        directory + folder + "eq/equilibration.imd"
    frameout_file = "/home/ignacio/DonElias/NPT.Lambda/" + \
        directory + folder + "eq/frameout_peptide.arg"
    joblist_file = "/home/ignacio/DonElias/NPT.Lambda/" + \
        directory + folder + "eq/equilibration.jobs"
    mklib_file = "/home/ignacio/DonElias/NPT.Lambda/" + \
        directory + folder + "eq/mk_script.lib"
    slurm_file = "/home/ignacio/DonElias/NPT.Lambda/" + \
        directory + folder + "eq/slurm_example.sh"
    submit_file = "/home/ignacio/DonElias/NPT.Lambda/" + \
        directory + folder + "eq/submit.txt"

    with open(mkscript_file, "w") as mks:
        mks.write(
            "@sys            eq_peptide\n"
            "@bin            /opt/md++1.41/bin/md\n"
            "@dir            /home/imunoz/NPT.Lambda/" + \
        directory + folder + "eq\n"
            "@files\n"
            "  topo          ../../topo/" + str(i) + "ALA_noC_54a7.top\n"
            "  input         equilibration.imd\n"
            "  coord         ../box/peptide_h2o.cnf\n"
            "  posresspec    ../box/sim_box_peptide.por\n"
            "  refpos        ../box/sim_box_peptide.rpr\n"
            "@template       mk_script.lib\n"
            "@version        md++\n"
            "@joblist        equilibration.jobs"
        )

    print(str(i) + "ALA - mk_script_file complete")

    system_flag = True
    multibath_flag = True
    force_flag = True

    with open(original_imd, "r") as file:
        lines = file.readlines()

    with open(imd_file, "w") as imd:
        for line in lines:

            if line == "SYSTEM\n":
                system_flag = False

            elif not system_flag and line == "END\n":
                imd.write(
                    "SYSTEM\n"
                    "#      NPM      NSM\n"
                    "         1      " + str(Param[i - 1][1]) + "\nEND\n"
                )
                system_flag = True

            elif line == "MULTIBATH\n":
                multibath_flag = False

            elif not multibath_flag and line == "END\n":
                imd.write(

                    "MULTIBATH\n"
                    "# ALGORITHM:\n"
                    "#      weak-coupling(0):      use weak-coupling scheme\n"
                    "#      nose-hoover(1):        use Nose Hoover scheme\n"
                    "#      nose-hoover-chains(2): use Nose Hoover chains scheme\n"
                    "# NUM: number of chains in Nose Hoover chains scheme\n"
                    "#      !! only specify NUM when needed !!\n"
                    "# NBATHS: number of temperature baths to couple to\n"
                    "#          ALGORITHM\n"
                    "                   0\n"
                    "#  NBATHS\n"
                    "         2\n"
                    "# TEMP0(1 ... NBATHS)  TAU(1 ... NBATHS)\n"
                    "       60                 0.1\n"
                    "       60                 0.1\n"
                    "#   DOFSET: number of distiguishable sets of d.o.f.\n"
                    "         2\n"
                    "# LAST(1 ... DOFSET)  COMBATH(1 ... DOFSET)  IRBATH(1 ... DOFSET)\n"
                    "      " +
                    str(Param[i - 1][0]) +
                    "                     1                     1\n"
                    "  " +
                    str(Param[i - 1][2]) +
                    "                     2                     2\nEND\n"
                )

                multibath_flag = True

            elif line == "FORCE\n":
                force_flag = False

            elif not force_flag and line == "END\n":
                imd.write(
                    "FORCE\n"
                    "# NTF(1..6): 0,1 determines terms used in force calculation\n"
                    "#             0: do not include terms\n"
                    "#             1: include terms\n"
                    "# NEGR: ABS(NEGR): number of energy groups\n"
                    "#             > 0: use energy groups\n"
                    "#             < 0: use energy and force groups\n"
                    "# NRE(1..NEGR): >= 1.0 last atom in each energy group\n"
                    "# NTF(1) NTF(2) NTF(3) NTF(4) NTF(5)        NTF(6)\n"
                    "# bonds     angles    improper  dihedral  electrostatic vdW\n"
                    "  0         1         1         1         1             1\n"
                    "# NEGR    NRE(1)    NRE(2)    ...      NRE(NEGR)\n"
                    "     2      " +
                    str(Param[i - 1][0]) + "      " +
                    str(Param[i - 1][2]) + "\nEND\n"
                )

                force_flag = True

# All flag on - write line to new file.

            elif system_flag and force_flag and multibath_flag:
                imd.write(line)

    print(str(i) + "ALA - imd_file complete")

    with open(frameout_file, "w") as frameout:
        frameout.write(
            "@topo           ../../topo/" + str(i) + "ALA_noC_54a7.top\n"
            "@pbc        r\n"
            "@outformat  pdb\n"
            "@notimeblock\n"
            "@traj      eq_peptide_5.trc.gz\n"
            "@include ALL\n"
            "@single\n"
        )

    print(str(i) + "ALA - frameout file complete")

    with open(original_joblist, "r") as file:
        lines = file.readlines()

    with open(joblist_file, "w") as job:
        for line in lines:
            job.write(line)

    with open(original_lib, "r") as file:
        lines = file.readlines()

    with open(mklib_file, "w") as lib:
        for line in lines:
            lib.write(line)

    with open(slurm_file, "w") as slurm:
        slurm.write(

            "#!/bin/bash\n"
            "#!/bin/sh\n"
            "#SBATCH -n " + str(cpu) + "\n"

            # Proyecto Alaninas

            # "#SBATCH --job-name=" + str(nALA) + "vacc" + str(i) + "\n"

            "#SBATCH --job-name=" + str(i) + "ALA_eq\n"

            "#SBATCH --output=" + str(i) + "ALA-%A_%a.out\n"
            "#SBATCH --error=" + str(i) + "ALA-%A_%a.err\n"
            "#SBATCH --ntasks-per-node=" + str(cpu) + "\n"

            #"#SBATCH --partition=slims\n"  # Leftraru
            "#SBATCH --partition=intel\n"  # DonElias

            "##SBATCH --mail-user=ignacio.siao@gmail.com\n"
            "##SBATCH --mail-type=ALL\n"
            "#SBATCH --array=1-1%1\n"
            "#SBATCH --mem-per-cpu=" + str(mem_per_cpu) + "\n"
            "\n"
            #"#module load gromosxx intel impi\n"  # Leftraru
            "\n"

            #"module load GSL/2.5\n"  # Leftraru
            #"module load FFTW/3.3.8\n"  # Leftraru
            "module load md++\n"  # DonElias
            "\n"

            "export OMP_NUM_THREADS=" + str(cpu) + "\n"
            "\n"
            "INFILE=`awk "
            '"NR==$SLURM_ARRAY_TASK_ID" '
            "submit.txt`\n"
            "source $INFILE")

    with open(submit_file, "w") as txt:
        txt.write(
            "./eq_peptide_1.run"
        )

    print(str(i) + "ALA - slurm files complete")


sh_file1 = "/home/ignacio/DonElias/NPT.Lambda/pdata/" + folder + "/eq/eq_1.sh"

with open(sh_file1, "w") as eq_1:
    eq_1.write(
        "#!/usr/bin/bash\n"
        "#\n"
        "for i in 1 2 3 4 5 6 7 8 9\n"
        "do\n"

        "   echo 0\"$i\"ALA\n"
        "   cd /home/imunoz/NPT.Lambda/0\"$i\"ALA/" + folder + "/eq\n"
        "   mk_script @f eq_mk_script.arg\n"
        "   sbatch slurm_example.sh\n"

        # "   ./eq_peptide_1.run\n"
        # "   echo eq_peptide_5.trc.gz file complete\n"
        # "   frameout @f frameout_peptide.arg\n"
        # "   echo frameout file complete\n"

        "done\n"

        "exit"

    )

sh_file2 = "/home/ignacio/DonElias/NPT.Lambda/pdata/" + folder + "/eq/eq_2.sh"

with open(sh_file2, "w") as eq_2:
    eq_2.write(
        "#!/usr/bin/bash\n"
        "#\n"
        "for i in 2 3 4 5 6 7 8 9\n"
        "do\n"

        "   echo 0\"$i\"ALA\n"
        "   cd /home/imunoz/NPT.Lambda/0\"$i\"ALA/" + folder + "/eq\n"
        "   frameout @f frameout_peptide.arg\n"
        "   echo frameout file complete\n"

        "done\n"

        "exit"
    )
