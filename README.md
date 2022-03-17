
# Non-Polar-Solvation

This repository is the suplementary material for the work titled:  
### "Non-polar solvation free energy calculations of 20 Alanine-peptides using Molecular Dynamics simulation and Thermodynamic Integration methods with GROMOS simulation software."

In this work, Molecular Dynamics technique (explicit model) was perform using GROMOS simulation software to calculate the van der Waals free energy of 
cavity-formation of 20 alanine peptides divided in extended and helix configurations, ranging from 1 to 10, and compare the numerical results with two 
impliciti solvent models: the standard model based on the molecular surface of the solute (SASA), and a new methodology which has a closer physical 
meaning modeling the solute as an uncharged capacitor.


### Notes: ### 

- **GROMOS** is an acronym of the **GROningen MOlecular Simulation** computer program. It’s a software package used for computer simulations of molecular 
systems like proteins, inorganic and organic chemical compounds, DNA, etc, writen in **C++**, available in this [link](http://www.gromos.net/). 
- All the motivation, theorical background, and methods are carefully explained in the project report. You can find the LaTeX file [here](https://github.com/PacioIgnacio/Non-Polar-Solvation/tree/master/Info).

## Workflow ##  

I strongly recommend to follow this structure when you work with GROMOS. It's a step by step method to develop molecular dynamics simulation 

  1. /topo  : create topology for each system.
  2. /coord : create coordinates for each atom.
  3. /min   : realax the system structure.
  4. /box   : solvate the structure in a box full of solvent molecules.
  5. /eq    : for each atom, increase velocities progressively.
  6. /md    : run **Molecular Dynamics Simulation**
  7. /TI    : run **Termodynamic Integration**

This repository is organized as follows: 
- Each diractory is enumerated with the number of *Alanine* residues of this particular system. (e.g. /5ALA = *Penta-Alanine*)
- The second level is corresponding on the configuration of the system (/Helix or /Extended)
- The third level is where all the steps described in the **Workflow** are organized.  

As you can see, GROMOS works with *text files* as an imput/output to its functions. This is why you can find python code to automatize the procces of edit 
and create each one of those files. They are also organized by step in the directory [/pdata](https://github.com/PacioIgnacio/Non-Polar-Solvation/tree/master/pdata) and follows the same structure. 

The results of the molecular simulations are available in the [/Results](https://github.com/PacioIgnacio/Non-Polar-Solvation/tree/master/Results) section and any code developed for the trajectory analisys and the Thermodynamics Integration is also available in the [/TI_results](https://github.com/PacioIgnacio/Non-Polar-Solvation/tree/master/TI_Results) directory. 

Feel free to use! 
