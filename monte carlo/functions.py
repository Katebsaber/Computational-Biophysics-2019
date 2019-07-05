from itertools import combinations
import numpy as np
from random import choice
from periodic_boundary_condition.periodic_lattice import Periodic_Lattice

def create_box(box_dimention, number_of_particles):    
    box = np.zeros((box_dimention,box_dimention),dtype=int)
    while len(np.nonzero(box)[0]) < number_of_particles:
        x_pos_temp = np.random.randint(0,box_dimention-1)
        y_pos_temp = np.random.randint(0,box_dimention-1)
        box[x_pos_temp,y_pos_temp] = 1
    return Periodic_Lattice(box)

def get_particles_pos(box):
    particles_pos_idx = np.array(list(zip(np.nonzero(box)[0],np.nonzero(box)[1])))
    return particles_pos_idx

def calculate_energy(box, particles_pos_idx):
    energy = 0
    particle_combination = list(combinations(particles_pos_idx, 2))
    for each in particle_combination:
        distance_x = abs(each[0][0]-each[1][0])
        distance_y = abs(each[0][1]-each[1][1])
        if distance_x < 2 and distance_y < 2: 
            energy += 1
    return -1 * energy


def random_move():
    moves = []
    moves.append(np.array([0,1])) #right
    moves.append(np.array([0,-1])) #left = np.array([0,-1])
    moves.append(np.array([-1,0])) #up = np.array([-1,0])
    moves.append(np.array([1,0])) #down = np.array([1,0])
    moves.append(np.array([-1,1])) #up right
    moves.append(np.array([-1,-1])) #up left
    moves.append(np.array([1,-1])) #down left
    moves.append(np.array([1,1])) #down right
    return choice(moves)
    
def check_move(box, random_particle_idx,rnd_move):
    if box[random_particle_idx[0] + rnd_move[0],
           random_particle_idx[1] + rnd_move[1]] == 0:
        return True
    else:
        return False

def move(box,random_particle_idx,rnd_move):
    # Empty the cell
    box[random_particle_idx[0],random_particle_idx[1]] = 0 
    
    # Fill the post-move cell
    box[random_particle_idx[0] + rnd_move[0],
        random_particle_idx[1] + rnd_move[1]] = 1
    
    return box
    
if __name__=='__main__':
    # UNIT AND INTEGRATION TESTING

    # Sample Temperature
    T = 0.5

    # Create the box
    box = create_box(6,5)
    # print(box)
    
    # get particle positions
    # particle_positions = get_particles_pos(box)
    # print(particle_positions)
    
    for i in range(100):
        # Check number of particles - prior to move
        print('# of Particles prior: ', len(np.nonzero(box)[0]))
        print(box)

        # Initiation state
        status = False
        while not status:
            # Choose one particle
            random_particle_idx = choice(get_particles_pos(box))
            print(random_particle_idx)

            # Choose a random move
            rnd_move = random_move()
            print(rnd_move)

            # Check if the move is possible        
            status = check_move(box,random_particle_idx,rnd_move)
            print(status)

        # Do the move 
        new_box = move(box,random_particle_idx,rnd_move)

        # Get new states
        # new_particle_positions = get_particles_pos(new_box)

        # Compare energies
        e = calculate_energy(box,get_particles_pos(box))
        new_e = calculate_energy(new_box,get_particles_pos(new_box))

        # Accept or discard new state
        if new_e <= e:
                box = new_box
        else:
            p = np.exp(-1 * (new_e-e) / T) # this shoud change later!
            accept = np.random.choice(np.arange(0,2), p=[1-p,p])

            if accept:
                box = new_box 

        # Check number of particles - posterior to move
        print('# of Particles posterior: ', len(np.nonzero(box)[0]))
        print(box)

        # Garbage collection
        del new_box
        del new_e
            
