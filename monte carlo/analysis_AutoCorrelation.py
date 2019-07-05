import numpy as np
from periodic_boundary_condition.periodic_lattice import Periodic_Lattice
import pickle

with open('data/box/box_{}.pkl'.format('20.0'),'rb') as f:
    box = Periodic_Lattice(np.array(pickle.load(f)))

print(box)