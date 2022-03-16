folder = ["extended", "helix"]


for j in range(len(folder)):

    for i in range(1, 11):

        if i < 10:

            mkdir_file = "/home/ignacio/Leftraru/NPT.Lambda/0" + \
                str(i) + "ALA/" + folder[j] + "/TI/mkdir.sh"

            with open(mkdir_file, "w") as mkdir:
                mkdir.write(
                    "#!/usr/bin/bash\n"
                    "#\n"
                    "for i in 0.000 0.100 0.200 0.300 0.400 0.450 0.500 0.550 0.600 0.625 0.650 0.675 0.690 0.700 0.705 0.710 0.715 0.720 0.725 0.730 0.735 0.740 0.760 0.780 0.800 0.820 0.840 0.860 0.880 0.900 0.950 1.000\n"
                    "do\n"
                    "   mkdir L_\"$i\"\n"
                    "   echo L_\"$i\"\n"
                    "done\n"
                    "exit\n"
                )

        if i == 10:

            mkdir_file = "/home/ignacio/Leftraru/NPT.Lambda/10ALA/" + \
                folder[j] + "/TI/mkdir.sh"

            with open(mkdir_file, "w") as mkdir:
                mkdir.write(
                    "#!/usr/bin/bash\n"
                    "#\n"
                    "for i in 0.000 0.100 0.200 0.300 0.400 0.450 0.500 0.550 0.600 0.625 0.650 0.675 0.690 0.700 0.705 0.710 0.715 0.720 0.725 0.730 0.735 0.740 0.760 0.780 0.800 0.820 0.840 0.860 0.880 0.900 0.950 1.000\n"
                    "do\n"
                    "   mkdir L_\"$i\"\n"
                    "   echo L_\"$i\"\n"
                    "done\n"
                    "exit\n"
                )
