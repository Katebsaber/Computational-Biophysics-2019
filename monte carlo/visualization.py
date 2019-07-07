import matplotlib.pyplot as plt
import numpy as np
import pickle
from glob import glob

directory_template = 'data/box/'
list_of_pkl = glob(directory_template + '*.pkl')

for each_box in list_of_pkl:    
    with open(each_box,'rb') as f:
        box = np.array(pickle.load(f))
    # Find T based on the name of the file
    T = float(each_box.split('\\')[-1][:-4])

    plt.imshow(box, cmap='hot', interpolation='nearest')
    plt.savefig('data/box/plot/{}.png'.format(str(T)))
    # plt.show()
    plt.clf()