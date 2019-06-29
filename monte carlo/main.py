from functions import create_box, get_particles_pos,move_one_particle,calculate_energy
from matplotlib import pyplot as plt
import numpy as np
import time

box_dimention = 10
number_of_particles = 30

assert number_of_particles < box_dimention**2

for j in range(1,41):
    T = 0.5 * j
        
    box = create_box(box_dimention,number_of_particles)
    particles_pos_idx = get_particles_pos(box)

    start = time.time()
    list_of_e = []
    for i in range(10000):
        if (i%100) == 0: print(i) # print itteration number every 100 steps
        
        e_temp = 0 # zero out temp energy
        
        # do the move
        status,box_temp,particles_pos_idx_temp = move_one_particle(box,particles_pos_idx)
        while status != True:
            status,box_temp,particles_pos_idx_temp = move_one_particle(box,particles_pos_idx)
        
        #calculate energies
        e = calculate_energy(box,particles_pos_idx)
        e_temp = calculate_energy(box_temp,particles_pos_idx_temp)

        # check move acceptance
        if e_temp <= e:
            box, particles_pos_idx = box_temp,particles_pos_idx_temp
            list_of_e.append(e_temp)
        else:
            p = np.exp(-1 * (e_temp-e) / T) # this shoud change later!
            accept = np.random.choice(np.arange(0,2), p=[1-p,p])

            if accept:
                box, particles_pos_idx = box_temp,particles_pos_idx_temp
                list_of_e.append(e_temp)

    end = time.time()
    print('elapsed time: ', end - start)

    plt.plot(list_of_e)
    plt.show()