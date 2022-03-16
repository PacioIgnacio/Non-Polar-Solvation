#!/usr/bin/bash
#
for i in 1 2 3 4 5 6 7 8 9
do
   echo 0"$i"ALA
   cd /home/imunoz/NPT.Lambda/0"$i"ALA/extended//eq
   mk_script @f eq_mk_script.arg
   sbatch slurm_example.sh
done
exit