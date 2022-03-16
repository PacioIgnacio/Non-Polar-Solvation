#!/usr/bin/bash
#
for i in 1 2 3 4 5 6 7 8 9
do
   echo 0"$i"ALA
   cd /home/imunoz/NPT.Lambda/0"$i"ALA/extended//box
   chmod 775 em_solvent.run
   ./em_solvent.run
   echo peptide_h2o.cnf file complete
   frameout @f frameout_peptide.arg
   echo frameout file complete
cd /home/imunoz/NPT.Lambda/10ALA/extended//box
chmod 775 em_solvent.run
./em_solvent.run
echo peptide_h2o.cnf file complete
frameout @f frameout_peptide.arg
echo frameout file complete
done
exit