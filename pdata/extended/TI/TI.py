Param = [[9, 804, 2421], [15, 933, 2814], [21, 895, 2706], [27, 1037, 3138], [
    33, 1451, 4386], [39, 1927, 5820], [45, 2502, 7551], [51, 3162, 9537], [57, 4014, 12099], [63, 4713, 14202]]


folder = "extended/"

original_imd = "/home/ignacio/DonElias/NPT.Lambda/10ALA/helix/TI/md.imd"
original_lib = "/home/ignacio/DonElias/NPT.Lambda/10ALA/helix/TI/mk_script.lib"

for i in range(1, 11):

    if i < 10:
        directory = "0" + str(i) + "ALA/"

    if i == 10:
        directory = "10ALA/"

    imd_file = "/home/ignacio/DonElias/NPT.Lambda/" + \
        directory + folder + "TI/TI_" + str(i) + "ALA_dummy.imd"

    lib_file = "/home/ignacio/DonElias/NPT.Lambda/" + \
        directory + folder + "TI/mk_script.lib"

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
                    "       298.15                0.1\n"
                    "       298.15                0.1\n"
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
                    "  0         0         0         0         1             1\n"
                    "# NEGR    NRE(1)    NRE(2)    ...      NRE(NEGR)\n"
                    "     2      " +
                    str(Param[i - 1][0]) + "      " +
                    str(Param[i - 1][2]) + "\nEND\n"
                )

                force_flag = True

# All flag on - write line to new file.

            elif system_flag and force_flag and multibath_flag:
                imd.write(line)

    print(str(i) + "ALA - TI_imd file complete")

    with open(original_lib, "r") as file:
        lines = file.readlines()

    with open(lib_file, "w") as lib:
        for line in lines:
            lib.write(line)

    print(str(i) + "ALA - mk_script.lib file complete")
