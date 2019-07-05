import numpy as np
from periodic_boundary_condition.periodic_lattice import Periodic_Lattice
from matplotlib import pyplot as plt
import pickle
from functions import create_box, get_particles_pos,move_one_particle,calculate_energy

# with open('box_1/0.5.pkl','rb') as f:
#     list_of_box = np.array(pickle.load(f))

# print(len(list_of_box))
# for i in range(10):
#     print(list_of_box[i],'\n')

box = create_box(10,30)
particles_pos_idx = get_particles_pos(box)

status,box_temp,particles_pos_idx_temp = move_one_particle(box,particles_pos_idx)
while status != True:
    status,box_temp,particles_pos_idx_temp = move_one_particle(box,particles_pos_idx)

#calculate energies
e = calculate_energy(box,particles_pos_idx)
e_temp = calculate_energy(box_temp,particles_pos_idx_temp)

# check move acceptance
if e_temp <= e:
    del box
    del particles_pos_idx
    box, particles_pos_idx = box_temp,particles_pos_idx_temp
    list_of_e.append(e_temp)
    list_of_box.append(box)
else:
    p = np.exp(-1 * (e_temp-e) / T) # this shoud change later!
    accept = np.random.choice(np.arange(0,2), p=[1-p,p])

    if accept:
        del box
        del particles_pos_idx
        box, particles_pos_idx = box_temp,particles_pos_idx_temp
        list_of_e.append(e_temp)
        list_of_box.append(box)