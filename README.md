# Critical behavior in a chiral molecular model

### Authors: Pablo M. Piaggi, Roberto Car, Frank H. Stillinger, Pablo G. Debenedetti

[![DataSpace](https://img.shields.io/badge/DataSpace-88435%2Fdsp01gt54kr255-orange)](https://doi.org/10.34770/aby7-r955)

Analysis scripts and input files to reproduce simulations of manuscript "Critical behavior in a chiral molecular model" by Piaggi, Car, Stillinger, and Debenedetti.
Output files are available at [this link](https://doi.org/10.34770/aby7-r955).

#### Description of folder contents:
* ```SystemSize<N>tetramers```: Input and output files of molecular dynamics simulations for a system with <N> molecules. Inside each folder there are subfolders ```T-<temp>``` where <temp> is the temperature. In each subfolder, the following files can be found:
  * ```in.lammps```: LAMMPS input file
  * ```in.restart.lammps```: LAMMPS input file for restarts
  * ```initialconfig.dat```: Initial configuration in LAMMPS data format
  * ```forcefield-base.dat```: Force field parameters
  * ```job.sh```: Slurm submission script
* ```Clustering```: Clustering script and results:
  * ```cluster.py```: Python script to perform clustering
* ```Analysis.ipynb```: Jupyter notebook with scripts to generate figures

Simulations were performed using the following code:
* Modified version of LAMMPS available at [this GitHub repository](https://github.com/PabloPiaggi/LAMMPS_ChiralTetramer).

The jupyter notebook and the python script were tested with the following packages:
* Python 3.8.8 [GCC 7.3.0]
* Matplotlib 3.3.4
* Numpy 1.24.2
* Scipy 1.9.1
* Freud 2.8.0
* Ase 3.20.1

Please e-mail me if you have trouble reproducing the results.
