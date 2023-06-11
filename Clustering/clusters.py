import numpy as np
import matplotlib.pyplot as plt
import MDAnalysis
import freud
import ase.io as aseio
import os

num_atoms_per_molecule=4
threshold=0.0
clusters_Maj=np.zeros(0,)
clusters_Min=np.zeros(0,)
base_directory="SystemSize8000tetramers/T-4.3"
base_filename=base_directory + "/dump.tetramer"
N=int(os.popen("cd " + base_directory + " ; find . -type f -name 'dump.tetramer.*' | sed 's|^\./dump.tetramer.||' | sort -n | tail -n 1").read())
print(N)
for i in range(1,N):
    filename = base_filename + "." + str(i)
    reader = MDAnalysis.coordinates.LAMMPS.DumpReader(filename)
    for frame, atoms in zip(reader,aseio.iread(filename,format='lammps-dump-text')):
        # Choose zeta > threshold
        zeta = atoms.get_array('c_zatom')[:,0]
        condition=zeta>threshold
        ts = MDAnalysis.coordinates.base.Timestep(frame.positions[condition,:].shape[0])
        ts.positions=frame.positions[condition,:]
        ts.dimensions=frame.dimensions
        cl = freud.cluster.Cluster()
        cl_props = freud.cluster.ClusterProperties()
        cl.compute(ts, neighbors={'r_max': 1.5})
        props = cl_props.compute(ts, cl.cluster_idx)
        cluster_size = cl_props.sizes / num_atoms_per_molecule
        if (np.mean(zeta)>0):
            clusters_Maj = np.append(clusters_Maj,cluster_size)
        else:
            clusters_Min = np.append(clusters_Min,cluster_size)
        # Choose zeta < -threshold
        zeta = atoms.get_array('c_zatom')[:,0]
        condition=zeta<-threshold
        ts = MDAnalysis.coordinates.base.Timestep(frame.positions[condition,:].shape[0])
        ts.positions=frame.positions[condition,:]
        ts.dimensions=frame.dimensions
        cl = freud.cluster.Cluster()
        cl_props = freud.cluster.ClusterProperties()
        cl.compute(ts, neighbors={'r_max': 1.5})
        props = cl_props.compute(ts, cl.cluster_idx)
        cluster_size = cl_props.sizes / num_atoms_per_molecule
        if (np.mean(zeta)<0):
            clusters_Maj = np.append(clusters_Maj,cluster_size)
        else:
            clusters_Min = np.append(clusters_Min,cluster_size)
np.save('clusters_maj_43_8000.npy', clusters_Maj)
np.save('clusters_min_43_8000.npy', clusters_Min)
