Param = [[9, 291, 882], [15, 405, 1230], [21, 541, 1644], [27, 612, 1863], [
    33, 601, 1836], [39, 784, 2391], [45, 952, 2901], [51, 1027, 3132], [57, 1323, 4026]]

folder = "extended"

original_imd = "/home/ignacio/DonElias/NPT.Lambda/10ALA/helix/min/em_peptide.imd"


for i in range(1, 10):

    run_file = "/home/ignacio/DonElias/NPT.Lambda/0" + \
        str(i) + "ALA/" + folder + "/min/em_peptide.run"
    imd_file = "/home/ignacio/DonElias/NPT.Lambda/0" + \
        str(i) + "ALA/" + folder + "/min/em_peptide.imd"
    frameout_file = "/home/ignacio/DonElias/NPT.Lambda/0" + \
        str(i) + "ALA/" + folder + "/min/frameout_peptide.arg"

    with open(frameout_file, "w") as frame:
        frame.write(
            "@topo ../../topo/" + str(i) + "ALA_noC_54a7.top\n"
            "@pbc        v\n"
            "@outformat pdb\n"
            "@notimeblock\n"
            "@traj           peptide_min.cnf\n"
        )

    print(str(i) + "ALA frameout file complete")

    with open(run_file, "w") as run:
        run.write(

            "#!/bin/sh\n"
            "GROMOS=md\n"

            "$GROMOS \\\n"
            "  @topo ../../topo/" + str(i) + "ALA_noC_54a7.top \\\n"
            "  @conf ../coord/gch_peptide.cnf \\\n"
            "  @fin  peptide_min.cnf \\\n"
            "  @input em_peptide.imd > em_peptide.omd"
        )

    print(str(i) + "ALA em_peptide.run file complete")

    with open(original_imd, "r") as file:
        lines = file.readlines()

    force_flag = True

    with open(imd_file, "w") as imd:

        for line in lines:

            if line == "FORCE\n":
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
                    "     1      " + str(Param[i - 1][0]) + "\nEND\n"
                )
                force_flag = True

# Todas las banderas prendidas:

            elif force_flag:
                imd.write(line)

    print(str(i) + "ALA em_peptide.imd file complete")


sh_file = "/home/ignacio/DonElias/NPT.Lambda/pdata/" + folder + "/min/min.sh"

with open(sh_file, "w") as min:
    min.write("#!/usr/bin/bash\n"

              "#\n"
              "for i in 1 2 3 4 5 6 7 8 9\n"
              "do\n"
              "   echo 0\"$i\"ALA\n"
              "   cd /home/imunoz/NPT.Lambda/0\"$i\"ALA/" + folder + "/min\n"
              "   chmod 775 em_peptide.run\n"
              "   ./em_peptide.run\n"
              "   echo em_peptide.run file done\n"
              "   frameout @f frameout_peptide.arg\n"
              "   echo frameout file complete\n"
              "   mv FRAME_00001.pdb peptide_min.pdb\n"
              "   echo 0\"$i\"ALA\n"
              "done\n"
              "exit"

              )
