  # !/usr/bin/bash
#
for i in 1 2 3 4 5 6 7 8 9
do
   echo 0$iALA
   cd /home/imunoz/NPT.Lambda/0$iALA/helix/coord
   pdb2g96 @f pdb2g96_peptide.arg > pdb2g96_1ALA.cnf
   gch @f gch_peptide.arg > gch_peptide.cnf
   echo 0$iALA
doneexit