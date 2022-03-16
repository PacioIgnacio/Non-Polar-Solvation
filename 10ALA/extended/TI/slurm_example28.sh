#!/bin/bash
#!/bin/sh
#SBATCH -n 2
#SBATCH --job-name=10A_TI
#SBATCH --output=10ALA-%A_%a.out
#SBATCH --error=10ALA-%A_%a.err
#SBATCH --ntasks-per-node=2
#SBATCH --partition=intel
##SBATCH --mail-user=ignacio.siao@gmail.com
##SBATCH --mail-type=ALL
#SBATCH --array=1-1%1
#SBATCH --mem-per-cpu=2G


module load md++

export OMP_NUM_THREADS=2

INFILE=`awk "NR==$SLURM_ARRAY_TASK_ID" submit28.txt`
source $INFILE