from itertools import combinations
import numpy as np
from random import choice
from periodic_boundary_condition.periodic_lattice import Periodic_Lattice

def create_box(box_dimention, number_of_particles):    
    box = np.zeros((box_dimention,box_dimention),dtype=int)
    for i in range(number_of_particles):
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

def move_one_particle(box,particles_pos_idx):
    right = np.array([0,1])
    left = np.array([0,-1])
    up = np.array([-1,0])
    down = np.array([1,0])

    # select one particle to move
    particle_idx = choice(particles_pos_idx)

    # select move
    move_id = np.random.randint(0,8)

    # move right
    if move_id == 0:    
        right_id = particle_idx + right 
        if  box[right_id[0],right_id[1]] == 0: # if true the right cell is empty
            box[particle_idx[0],particle_idx[1]] = 0
            box[right_id[0],right_id[1]] = 1
            return True, box , get_particles_pos(box)
        else:
            return False, box , get_particles_pos(box)

    # move left
    if move_id == 1:    
        left_id = particle_idx + left
        if  box[left_id[0],left_id[1]] == 0: # if true the left cell is empty
            box[particle_idx[0],particle_idx[1]] = 0
            box[left_id[0],left_id[1]] = 1
            return True, box , get_particles_pos(box)
        else:
            return False, box , get_particles_pos(box)

    # move up
    if move_id == 2:    
        upper_id = particle_idx + up
        if  box[upper_id[0],upper_id[1]] == 0: # if true the upper cell is empty
            box[particle_idx[0],particle_idx[1]] = 0
            box[upper_id[0],upper_id[1]] = 1
            return True, box , get_particles_pos(box)
        else:
            return False, box , get_particles_pos(box)

    # move down
    if move_id == 3:    
        lower_id = particle_idx + down 
        if  box[lower_id[0],lower_id[1]] == 0: # if true the lower cell is empty
            box[particle_idx[0],particle_idx[1]] = 0
            box[lower_id[0],lower_id[1]] = 1
            return True, box , get_particles_pos(box)
        else:
            return False, box , get_particles_pos(box)

    # move right up
    if move_id == 4:    
        right_up_id = particle_idx + right + up 
        if  box[right_up_id[0],right_up_id[1]] == 0: # if true the right up cell is empty
            box[particle_idx[0],particle_idx[1]] = 0
            box[right_up_id[0],right_up_id[1]] = 1
            return True, box , get_particles_pos(box)
        else:
            return False, box , get_particles_pos(box)

    # move right down
    if move_id == 5:    
        right_down_id = particle_idx + right + down 
        if  box[right_down_id[0],right_down_id[1]] == 0: # if true the right down cell is empty
            box[particle_idx[0],particle_idx[1]] = 0
            box[right_down_id[0],right_down_id[1]] = 1
            return True, box , get_particles_pos(box)
        else:
            return False, box , get_particles_pos(box)

    # move left up
    if move_id == 6:    
        left_up_id = particle_idx + left + up 
        if  box[left_up_id[0],left_up_id[1]] == 0: # if true the left up cell is empty
            box[particle_idx[0],particle_idx[1]] = 0
            box[left_up_id[0],left_up_id[1]] = 1
            return True, box , get_particles_pos(box)
        else:
            return False, box , get_particles_pos(box)

    # move left down
    if move_id == 7:    
        left_down_id = particle_idx + left + down 
        if  box[left_down_id[0],left_down_id[1]] == 0: # if true the left down cell is empty
            box[particle_idx[0],particle_idx[1]] = 0
            box[left_down_id[0],left_down_id[1]] = 1
            return True, box , get_particles_pos(box)
        else:
            return False, box , get_particles_pos(box)
