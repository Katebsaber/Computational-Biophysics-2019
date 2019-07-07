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

for j in range(20,40):
    T = 0.5 + 0.05 * j

    # Create the box
    box = create_box(box_dimention,number_of_particles)

    start = time.time()
    list_of_e = []
    list_of_box = []
    for i in range(300000):
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
        if new_e <= e:
                box = new_box
        elif new_e>e:
            p = np.exp(-1*(new_e-e)/ T)  
            rnd_n = np.random.rand(1)[0]
            # print('delta E = ', new_e-e)
            # print('formula(T={}) = '.format(T), p)
            # print('random number = ',rnd_n)
            if rnd_n <= p:
                accept = True
            else:
                accept = False

            if accept:
                box = new_box


        # Check number of particles - posterior to move
        # print('# of Particles posterior: ', len(np.nonzero(box)[0]))
        # print(box)

        # Log every 1000 steps
        if (i%1000) == 0: 
            print(i)

        if (i%(500)) == 0: 
            # save energies
            list_of_e.append(e)

        if (i%10000) == 0: 
            with open('data/e/{}.pkl'.format(str(T)),'wb') as f:
                pickle.dump(list_of_e,f)

            # save box
            with open('data/box/{}.pkl'.format(str(T)),'wb') as f:
                pickle.dump(box,f)

            plt.plot(list_of_e)
            plt.savefig('data/e/plot/{}.png'.format(str(T)))
            # plt.show()
            plt.clf()

        # Garbage collection
        del new_box
        del new_e

    end = time.time()
    print('elapsed time: ', end - start)

    

