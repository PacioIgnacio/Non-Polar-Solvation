#!/usr/bin/bash
#
for i in 2 3 4 5 6 7 8 9
do
   echo 0"$i"ALA
   cd /home/imunoz/NPT.Lambda/0"$i"ALA/extended//eq
   frameout @f frameout_peptide.arg
   echo frameout file complete
done
exit