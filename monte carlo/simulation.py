from functions import create_box, get_particles_pos,calculate_energy, random_move, check_move, move, calc_e
from matplotlib import pyplot as plt
import numpy as np
import time
import pickle
from random import choice

box_dimention = 20
number_of_particles = 150 

# Check if the box is able to contain this number of particles
assert number_of_particles < box_dimention**2

for j in range(1,41):
    T = 0.5 * j

    # Create the box
    box = create_box(box_dimention,number_of_particles)

    start = time.time()
    list_of_e = []
    list_of_box = []
    for i in range(200000):
        # Check number of particles - prior to move
        # print('# of Particles prior: ', len(np.nonzero(box)[0]))
        # print(box)

        # Initiation state
        status = False
        while not status:
            # Choose one particle
            random_particle_idx = choice(get_particles_pos(box))
            # print(random_particle_idx)

            # Choose a random move
            rnd_move = random_move()
            # print(rnd_move)

            # Check if the move is possible        
            status = check_move(box,random_particle_idx,rnd_move)
            # print(status)

        # Do the move 
        new_box = move(box,random_particle_idx,rnd_move)

        # Compare energies
        # e = calculate_energy(box)
        # new_e = calculate_energy(new_box)
        e = calc_e(box)
        new_e = calc_e(new_box)

        # Accept or discard new state
        if new_e < e:
                box = new_box
        else:
            p = 0.008 * T #np.exp(-1 * (new_e-e)/ T**2)  
            # print('p=',p)
            accept = np.random.choice(np.arange(0,2), p=[1-p,p])

            if accept:
                box = new_box


        # Check number of particles - posterior to move
        # print('# of Particles posterior: ', len(np.nonzero(box)[0]))
        # print(box)

        # Garbage collection
        del new_box
        del new_e

        # Log every 1000 steps
        if (i%1000) == 0: 
            print(i)

        if (i%(10)) == 0: 
            # save energies
            list_of_e.append(e)

        if (i%10000) == 0: 
            with open('data/e/{}.pkl'.format(str(T)),'wb') as f:
                pickle.dump(list_of_e,f)

            # save box
            with open('data/box/{}.pkl'.format(str(T)),'wb') as f:
                pickle.dump(box,f)

            plt.plot(list_of_e)
            plt.savefig('data/e/{}.png'.format(str(T)))
            # plt.show()
            plt.clf()

    end = time.time()
    print('elapsed time: ', end - start)

    

