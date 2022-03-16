folder = "helix"

def cnf2por_rpr(cnf_file):

    title_flag = True
    solv_flag = True

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


for i in range(1, 11):

    if i < 10:

        cnf_file = "/home/ignacio/DonElias/NPT.Lambda/0" + \
            str(i) + "ALA/" + folder + "/md/md_peptide_10.cnf"

        por_file = "/home/ignacio/DonElias/NPT.Lambda/0" + \
            str(i) + "ALA/" + folder + "/md/md_peptide_10.por"

        rpr_file = "/home/ignacio/DonElias/NPT.Lambda/0" + \
            str(i) + "ALA/" + folder + "/md/md_peptide_10.rpr"

        cnf2por_rpr(cnf_file)

    if i == 10:

        cnf_file = "/home/ignacio/DonElias/NPT.Lambda/10ALA/" + \
            folder + "/md/md_peptide_10.cnf"

        por_file = "/home/ignacio/DonElias/NPT.Lambda/10ALA/" + \
            folder + "/md/md_peptide_10.por"

        rpr_file = "/home/ignacio/DonElias/NPT.Lambda/10ALA/" + \
            folder + "/md/md_peptide_10.rpr"

        cnf2por_rpr(cnf_file)
