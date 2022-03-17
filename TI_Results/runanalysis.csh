#!/bin/csh
#
module load gromos++/1.41-openmp
module load md++/1.41-openmp
foreach x (0.000  0.100  0.200  0.300  0.400  0.450  0.500  0.550  0.600  0.625  0.650  0.675  0.690  0.700  0.705  0.710  0.715  0.720  0.725  0.730  0.735  0.740  0.760  0.780  0.800  0.820  0.840  0.860  0.880  0.900  0.950  1.000  )

        echo L_$x
  cd L_$x
ene_ana @f ene_ana.inp > ene_ana.out
ene_ana @f ene_ana_inte.inp > ene_ana_inte.out
        cd ..
end

exit