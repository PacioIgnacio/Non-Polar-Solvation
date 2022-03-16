folder = "extended"

original_lib = "/home/ignacio/DonElias/NPT.Lambda/01ALA/helix/coord/pdb2g96.lib"

# Script running in /coord folder to generate pdb2g96_nALA.cnf and gch_nALA_cnf

for i in range(1, 10):

    pdb_file = "/home/ignacio/DonElias/NPT.Lambda/0" + \
        str(i) + "ALA/" + folder + "/coord/pdb2g96_peptide.arg"
    gch_file = "/home/ignacio/DonElias/NPT.Lambda/0" + \
        str(i) + "ALA/" + folder + "/coord/gch_peptide.arg"
    frameout_file = "/home/ignacio/DonElias/NPT.Lambda/0" + \
        str(i) + "ALA/" + folder + "/coord/frameout_peptide.arg"
    lib_file = "/home/ignacio/DonElias/NPT.Lambda/0" + \
        str(i) + "ALA/" + folder + "/coord/pdb2g96.lib"

    with open(pdb_file, "w") as pdb:
        pdb.write(
            "@topo ../../topo/" + str(i) + "ALA_noC_54a7.top\n"
            "@pdb  0" + str(i) + "Anoh.pdb\n"
            "@lib  pdb2g96.lib"
        )

#

    with open(gch_file, "w") as gch:
        gch.write(
            "@topo ../../topo/" + str(i) + "ALA_C_54a7.top\n"
            "# the coordinates from which you want to generate the hydrogens.\n"
            "@pos pdb2g96_" + str(i) + "ALA.cnf\n"
            "# All hydrogens within a bond length tolerance of 0.1% are kept - the others are generated\n"
            "@tol   0.1"
        )

    with open(frameout_file, "w") as frame:
        frame.write(
            "@topo ../../topo/" + str(i) + "ALA_C_54a7.top\n"
            "@pbc        v\n"
            "@outformat pdb\n"
            "@notimeblock\n"
            "@traj           gch_peptide.cnf\n"


        )

    with open(original_lib, "r") as file:
        lines = file.readlines()

    with open(lib_file, "w") as lib:
        for line in lines:
            lib.write(line)

sh_file = "/home/ignacio/DonElias/NPT.Lambda/pdata/" + folder + "/coord/coord.sh"

with open(sh_file, "w") as coord:
    coord.write("#!/usr/bin/bash\n"
                "#\n"
                "for i in 1 2 3 4 5 6 7 8 9\n"
                "do\n"
                "   echo 0\"$i\"ALA\n"
                "   cd /home/imunoz/NPT.Lambda/0\"$i\"ALA/" + folder + "/coord\n"
                "   pdb2g96 @f pdb2g96_peptide.arg > pdb2g96_\"$i\"ALA.cnf\n"
                "   echo pdb2g96_\"$i\"ALA.cnf file complete\n"
                "   gch @f gch_peptide.arg > gch_peptide.cnf\n"
                "   echo gch_peptide.cnf file complete\n"
                "   frameout @f frameout_peptide.arg\n"
                "   mv FRAME_00001.pdb peptide_gch.pdb\n"
                "   echo 0\"$i\"ALA\n"
                "done\n"
                "exit"
                )
# coord.sh script is required to run in console with bash comand -- bash coord.sh
# It will run all pdb2g96 and gch file in each nALA/.../coord/ folders.
