#!/usr/bin/bash
#
for i in 1 2 3 4 5 6 7 8 9
do
   echo 0"$i"ALA
   cd /home/imunoz/NPT.Lambda/0"$i"ALA/helix/coord
   pdb2g96 @f pdb2g96_peptide.arg > pdb2g96_"$i"ALA.cnf
   echo pdb2g96_"$i"ALA.cnf file complete
   gch @f gch_peptide.arg > gch_peptide.cnf
   echo gch_peptide.cnf file complete
   frameout @f frameout_peptide.arg
   mv FRAME_00001.pdb peptide_gch.pdb
   echo 0"$i"ALA
done
exit