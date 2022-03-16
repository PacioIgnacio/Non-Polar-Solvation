for i in range(1, 10):

    arg_file = "/home/ignacio/DonElias/NPT.Lambda/0" + \
        str(i) + "ALA/helix/box/sim_box_peptide.arg"

    with open(arg_file, "w") as pep:
        pep.write(
            "@topo    ../../topo/" + str(i) + "ALA_noC_54a7.top\n"
            "  # We use a cubic box (r = rectangular)\n"
            "@pbc     r\n"
            "  # coordinates of the solute.\n"
            "@pos  ../min/peptide_min.cnf\n"
            "  # coordinates of the box containing SPC water molecules.\n"
            "@solvent spc.cnf\n"
            "  # the minimum solute-wall distance\n"
            "@minwall   0.8\n"
            "  # the minimum solute-solvent distance\n"
            "@thresh  0.23\n"
            "  # used if one uses trucated octahedron pbc\n"
            "@rotate\n")

        print(str(i)+"ALA - sim_box_peptide.arg file copmplete")


sh_file = "/home/ignacio/DonElias/NPT.Lambda/pdata/box/box_1.sh"

with open(sh_file, "w") as box:
    box.write(
        "#!/usr/bin/bash\n"
        "#\n"
        "for i in 1 2 3 4 5 6 7 8 9\n"
        "do\n"

        "   echo 0\"$i\"ALA\n"
        "   cd /home/imunoz/NPT.Lambda/0\"$i\"ALA/helix/box\n"

        "   sim_box @f sim_box_peptide.arg > sim_box_peptide.cnf\n"
        "   echo sim_box_peptide.cnf file complete\n"
        "done\n"

        "exit"

    )
