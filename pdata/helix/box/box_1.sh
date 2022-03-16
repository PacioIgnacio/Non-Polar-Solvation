#!/usr/bin/bash
#
for i in 1 2 3 4 5 6 7 8 9
do
   echo 0"$i"ALA
   cd /home/imunoz/NPT.Lambda/0"$i"ALA/helix/box
   sim_box @f sim_box_peptide.arg > sim_box_peptide.cnf
   echo sim_box_peptide.cnf file complete
done
exit