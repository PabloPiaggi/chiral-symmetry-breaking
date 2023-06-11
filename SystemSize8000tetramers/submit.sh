TEMP=$1
cp -r BASE T-${TEMP}
cd T-${TEMP}
sed -i "s/TEMP/${TEMP}/g" in.lammps
sed -i "s/TEMP/${TEMP}/g" in.restart.lammps
sed -i "s/TEMP/${TEMP}/g" job.sh
sbatch < job.sh
