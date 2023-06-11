#!/bin/bash
#SBATCH --job-name="L-T-TEMP"
#SBATCH --nodes=2                # node count
#SBATCH --ntasks=56              # total number of tasks across all nodes
#SBATCH --ntasks-per-node=28     # total number of tasks per node
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --time=24:00:00

module purge
module load intel/2021.1.2
module load intel-mpi/intel/2021.1.1
module load anaconda3/2021.5
module load fftw/intel-2021.1/intel-mpi/3.3.9

############################################################################
# Variables definition
############################################################################
EXE=/scratch/gpfs/ppiaggi/Simulations/ChiralTetramer/Lammps/lammps-1Feb14/src/lmp_mpi
cycles=3
############################################################################


############################################################################
# Run
############################################################################
if [ -e runno ] ; then
   #########################################################################
   # Restart runs
   #########################################################################
   nn=`tail -n 1 runno | awk '{print $1}'`
   srun $EXE -in in.restart.lammps
   #########################################################################
else
   #########################################################################
   # First run
   #########################################################################
   nn=1
   srun $EXE -in in.lammps
   #########################################################################
fi
############################################################################

############################################################################
# Prepare next run
############################################################################
# Back up
############################################################################
cp log.lammps log.lammps.${nn}
cp dump.tetramer dump.tetramer.${nn}
last_restart=$(ls -1v tetramer.restart.* | tail -n 1)
echo ${last_restart}
cp ${last_restart} tetramer.restart 
############################################################################

############################################################################
# Check number of cycles
############################################################################
mm=$((nn+1))
echo ${mm} > runno
#cheking number of cycles
if [ ${nn} -ge ${cycles} ]; then
  exit
fi
############################################################################

############################################################################
# Resubmitting again
############################################################################
sbatch < job.sh
############################################################################

date
