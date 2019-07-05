import numpy as np
import pandas as pd
import pickle
from glob import glob
from matplotlib import pyplot as plt
from operator import itemgetter
from periodic_boundary_condition import periodic_lattice

# Physical config
Kb = 1

# list all saved files in directory
directory_template = 'data/'
list_of_pkl = glob(directory_template + '*.pkl')

list_of_Cv_T = []
for each_file in list_of_pkl:  
    print(each_file)  
    # open each file and convert to numpy array
    with open(each_file,'rb') as f:
        list_of_e = np.array(pickle.load(f))
        # Find Kb*T based on the name of the file
        T = float(each_file.split('\\')[1][:-4])
    
    # Itteratively calculate mean to find truncation point in order to get equilibrated states
    window_size = 10
    for i in range(len(list_of_e) - 2*window_size):
        mean_current = np.mean(list_of_e[i:i+window_size])
        mean_future = np.mean(list_of_e[i+window_size:i+2*window_size])
        # condition on series truncation
        if abs(mean_current - mean_future) <= 0.1:
            list_of_e = list_of_e[i:]
        # calculate Cv: Cv = 1/(Kb * T**2) * variance(equilibrated_states_e)
        Cv = 1/(Kb * T**2) * np.var(list_of_e)
    list_of_Cv_T.append([Cv,T])

# Sort Cv,T list based on T
list_of_Cv_T = sorted(list_of_Cv_T, key=itemgetter(1))

# Create a pandas dataframe to manage data
# df = pd.DataFrame.from_records(list_of_Cv_T,columns=['Cv','T'],index=['T'])

######### Output Options #########

# # Save results to excel
# df.to_excel("output/Cv-T.xlsx")

# # Show the plots
# list_of_Cv_T = np.array(list_of_Cv_T)
# plt.plot(list_of_Cv_T[:,1],list_of_Cv_T[:,0])
# plt.show()