from itertools import combinations
import numpy as np
from periodic_boundary_condition.periodic_lattice import Periodic_Lattice

box_dimention = 5
number_of_particles = 3

box = np.zeros((box_dimention,box_dimention),dtype=int)
for i in range(number_of_particles):
    x_pos_temp = np.random.randint(0,box_dimention-1)
    y_pos_temp = np.random.randint(0,box_dimention-1)
    box[x_pos_temp,y_pos_temp] = 1

particle_pos_idx = np.array(list(zip(np.nonzero(box)[0],np.nonzero(box)[1])))

print(box)
print(particle_pos_idx)

particle_combination = list(combinations(particle_pos_idx, 2))
for each in particle_combination:
    distance_x = abs(each[0][0]-each[1][0])
    distance_y = abs(each[0][1]-each[1][1])
    print(each)
    print(distance_x,distance_y)
    if distance_x == 1 and distance_y == 1: print(True)
