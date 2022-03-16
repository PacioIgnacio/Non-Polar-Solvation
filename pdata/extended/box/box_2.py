import numpy as np

Param = [[9, 804, 2421], [15, 933, 2814], [21, 895, 2706], [27, 1037, 3138], [
    33, 1451, 4386], [39, 1927, 5820], [45, 2502, 7551], [51, 3162, 9537], [57, 4014, 12099], [63, 4713, 14202]]

folder = "extended/"

original_imd = "/home/ignacio/DonElias/NPT.Lambda/10ALA/helix/box/em_solvent.imd"

for i in range(1, 11):

    if i < 10:

        directory = "0" + str(i) + "ALA/"

    if i == 10:

        directory = "10ALA/"

    cnf_file = "/home/ignacio/DonElias/NPT.Lambda/" + \
        directory + folder + "box/sim_box_peptide.cnf"
    por_file = "/home/ignacio/DonElias/NPT.Lambda/" + \
        directory + folder + "/box/sim_box_peptide.por"
    rpr_file = "/home/ignacio/DonElias/NPT.Lambda/" + \
        directory + folder + "/box/sim_box_peptide.rpr"
    run_file = "/home/ignacio/DonElias/NPT.Lambda/" + \
        directory + folder + "/box/em_solvent.run"
    imd_file = "/home/ignacio/DonElias/NPT.Lambda/" + \
        directory + folder + "/box/em_solvent.imd"
    frameout_file = "/home/ignacio/DonElias/NPT.Lambda/" + \
        directory + folder + "box/frameout_peptide.arg"

    title_flag = True
    solv_flag = True
    sistem_flag = True
    force_flag = True

    with open(cnf_file, "r") as file:
        lines = file.readlines()

    with open(por_file, "w") as por:

        for line in lines:

            if line == "TITLE\n":
                title_flag = False
                por.write(line)

            elif not title_flag and line == "POSITION\n":
                por.write(
                    "solute atoms to be positionally restrained\n"
                    "END\n"
                    "POSRESSPEC\n"
                )
                title_flag = True
                next

            elif line[:10] == "    1 SOLV":
                solv_flag = False

            elif title_flag and solv_flag:
                por.write(line)

        por.write("END\n")

    print("0" + str(i) + "ALA/sim_box_peptide.por file complete")

    with open(rpr_file, "w") as rpr:

        for line in lines:

            if line == "TITLE\n":
                title_flag = False
                rpr.write(line)

            if not title_flag and line == "POSITION\n":
                rpr.write(
                    "reference positions for restraining solute atoms\n"
                    "END\n"
                    "REFPOSITION\n"
                )

                title_flag = True
                next

            elif title_flag:
                rpr.write(line)

    print("0" + str(i) + "ALA/sim_box_peptide.rpr file complete")

    with open(run_file, "w") as run:
        run.write(


            "#!/bin/sh\n"
            "GROMOS=md\n"

            "$GROMOS \\\n"
            "  @topo ../../topo/" + str(i) + "ALA_noC_54a7.top \\\n"
            "  @conf sim_box_peptide.cnf \\\n"
            "  @fin  peptide_h2o.cnf \\\n"
            "  @refpos sim_box_peptide.rpr \\\n"
            "  @posresspec sim_box_peptide.por \\\n"
            "  @input em_solvent.imd > em_solvent.omd"

        )

    print(str(i) + "ALA/em_peptide.run file complete")

    with open(original_imd, "r") as file:
        lines = file.readlines()

    with open(imd_file, "w") as imd:
        for line in lines:

            if line == "SYSTEM\n":
                sistem_flag = False

            elif not sistem_flag and line == "END\n":
                imd.write(
                    "SYSTEM\n"
                    "#      NPM      NSM\n"
                    "         1      " + str(Param[i - 1][1]) + "\nEND\n"
                )
                sistem_flag = True

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

# Todas las banderas prendidas:

            elif sistem_flag and force_flag:
                imd.write(line)

    print("0" + str(i) + "ALA em_solvent.imd file complete")

    with open(frameout_file, "w") as frame:
        frame.write(
            "@topo ../../topo/" + str(i) + "ALA_noC_54a7.top\n"
            "@pbc        r\n"
            "@outformat pdb\n"
            "@notimeblock\n"
            "@traj           peptide_h2o.cnf\n"
            "@include ALL"
        )

sh_file = "/home/ignacio/DonElias/NPT.Lambda/pdata/" + folder + "/box/box_2.sh"

with open(sh_file, "w") as box:
    box.write(
        "#!/usr/bin/bash\n"
        "#\n"
        "for i in 1 2 3 4 5 6 7 8 9\n"
        "do\n"

        "   echo 0\"$i\"ALA\n"
        "   cd /home/imunoz/NPT.Lambda/0\"$i\"ALA/" + folder + "/box\n"
        "   chmod 775 em_solvent.run\n"
        "   ./em_solvent.run\n"
        "   echo peptide_h2o.cnf file complete\n"
        "   frameout @f frameout_peptide.arg\n"
        "   echo frameout file complete\n"

        # for 10ALA folder separatly

        "cd /home/imunoz/NPT.Lambda/10ALA/" + folder + "/box\n"
        "chmod 775 em_solvent.run\n"
        "./em_solvent.run\n"
        "echo peptide_h2o.cnf file complete\n"
        "frameout @f frameout_peptide.arg\n"
        "echo frameout file complete\n"

        "done\n"

        "exit"

    )
