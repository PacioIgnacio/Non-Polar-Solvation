#!/usr/bin/bash
#
for i in 1 2 3 4 5 6 7 8 9
do
   echo 0"$i"ALA
   cd /home/imunoz/NPT.Lambda/0"$i"ALA/helix/min
   chmod 775 em_peptide.run
   ./em_peptide.run
   echo em_peptide.run file done
   frameout @f frameout_peptide.arg
   echo frameout file complete
   mv FRAME_00001.pdb peptide_min.pdb
   echo 0"$i"ALA
done
exit