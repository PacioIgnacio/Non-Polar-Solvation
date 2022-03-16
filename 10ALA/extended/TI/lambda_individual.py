import glob
from natsort import natsorted

files = natsorted(glob.glob("L_*"))

lamb_points = []
lamb_values = []

nALA = 10
namebase = "TI_" + str(nALA) + "ALA_dummy"
# namebase = "TI_scp_dummy"

# parámetros slurm
cpu = 2
mem_per_cpu = "2G"

# Parámetro simulación, ## dt=500000 1[ns]
n_sim = 5  # Seleciconar número par
t_sim = 7500000
t_sim_pre = 100000

# Rutas directorios

bin_path = "/opt/md++1.41/bin/md"  # DonElias
#bin_path = "/home/cinv/md++1.41/bin/md"  # Leftraru
dir_path = "/home/jgarate/work/gromos/NPT.Lambda/10ALA/extended/TI"

#---

i = 1

for file in files:

    names = "{:.3f}".format(float(file[2:]))
    values = float(file[2:])

    lamb_points.append(names)
    lamb_values.append(values)

    g = open("slurm_example" + str(i) + ".sh", "w")
    h = open("submit" + str(i) + ".txt", "w")
    f = open("TI_joblist" + str(i) + ".dat", "w")
    p = open("TI_mk_script" + str(i) + ".arg", "w")

    for k in range(n_sim + 1):

        if k == 0:

            h.write("L_" + str(lamb_points[i - 1]) + "/" + namebase +
                     "_" + str(int(round(lamb_values[i - 1] * 10000)) + k + 1) + ".run\n")




    # for k in range(n_sim + 1):

    #     h.write("L_" + str(lamb_points[i - 1]) + "/" + namebase +
    #             "_" + str(int(round(lamb_values[i - 1] * 10000)) + k + 1) + ".run\n")

# SLURM FILE

    g.write("#!/bin/bash\n"
            "#!/bin/sh\n"
            "#SBATCH -n " + str(cpu) + "\n"

            # Proyecto Alaninas

            # "#SBATCH --job-name=" + str(nALA) + "vacc" + str(i) + "\n"

            "#SBATCH --job-name=" + str(nALA) + "A_TI\n"

            "#SBATCH --output=" + str(nALA) + "ALA-%A_%a.out\n"
            "#SBATCH --error=" + str(nALA) + "ALA-%A_%a.err\n"
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
            "submit" + str(i) + ".txt`\n"
            "source $INFILE")

# GROMOS FILES

# Single simulation/job after pre_sim

    # f.write("TITLE\n"
    #         "Script atomatizado con Python\n"
    #         "END\n"
    #         "JOBSCRIPTS\n"
    #         "job_id NSTLIM  RLAM    subdir   run_after\n")

    # f.write(str(int(round(lamb_values[i - 1] * 10000)) + 1) + "      " + str(t_sim_pre) + "    " +
    #         str(lamb_points[i - 1]) + "    " + "L_" + str(lamb_points[i - 1]) + "    0\n")

    # for k in range(n_sim - 1):

    #     f.write(str(int(round(lamb_values[i - 1] * 10000)) + (k + 2)) + "    " + str(t_sim) +
    #             "    " + str(lamb_points[i - 1]) + "    " + "L_" + str(lamb_points[i - 1]) + "    " +
    #             str(int(round(lamb_values[i - 1] * 10000)) + (k + 1)) + "\n")

    # f.write("END")


# n_sim divisions for the same simulation/job

    f.write("TITLE\n"
            "Script atomatizado con Python\n"
            "END\n"
            "JOBSCRIPTS\n"
            "job_id NSTLIM  RLAM    subdir   run_after\n")

    for k in range(n_sim + 1):

        if k == 0:
            f.write(str(int(round(lamb_values[i - 1] * 10000)) + 1) + "      " + str(t_sim_pre) + "    " +
                    str(lamb_points[i - 1]) + "    " + "L_" + str(lamb_points[i - 1]) + "    0\n")

        else:
            f.write(str(int(round(lamb_values[i - 1] * 10000)) + k + 1) + "      " + str(int(t_sim / n_sim)) + "    " +
                    str(lamb_points[i - 1]) + "    " + "L_" + str(lamb_points[i - 1]) + "    " + str(int(round(lamb_values[i - 1] * 10000)) + k) + "\n")

    f.write("END")

    p.write("@sys       " + namebase + "\n"
            "@bin       " + bin_path + "\n"
            "@version         md++\n"
            "@dir       " + dir_path + "\n"
            "@files\n "
            "  topo          ../../topo/" +
            str(nALA) + "ALA_noC_54a7.top\n"
            "  pttopo        ../../../../ptps/" + str(nALA) + "ALA_dummy.ptp\n"
            "  input         TI_" + str(nALA) + "ALA_dummy.imd\n"
            "  coord         ../md/md_peptide_10.cnf\n"
            "  posresspec    ../md/md_peptide_10.por\n"
            "  refpos        ../md/md_peptide_10.rpr\n"
            "@template       mk_script.lib\n"
            "@joblist        TI_joblist" + str(i) + ".dat")

    i = i + 1


with open("mk_script.sh", "w") as mks:
    mks.write(
        "#! /usr/bin/bash\n"  # Leftraru
        "#\n"
#        "module load GSL/2.5\n"
#        "module load FFTW/3.3.8\n"
        "for x in ")

    for i in range(len(lamb_points)):
        mks.write(str(i + 1) + " ")

    mks.write("\n"
              " do\n"

              " mk_script @f TI_mk_script$x.arg\n"
              "done")

with open("run_slurm.sh", "w") as run:
    run.write(
        "#! /usr/bin/bash\n"  # Leftraru
        "#\n"
        "for x in ")

    for i in range(len(lamb_points)):
        run.write(str(i + 1) + " ")

    run.write("\n"
              " do\n"
              " sbatch slurm_example$x.sh\n"
              "done")


print("Lambda Points =", len(lamb_points))
