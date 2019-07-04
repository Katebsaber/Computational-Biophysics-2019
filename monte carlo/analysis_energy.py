import numpy as np
from matplotlib import pyplot as plt
import pickle

with open('data/1.0.pkl','rb') as f:
    list_of_e = pickle.load(f)

plt.plot(list_of_e)
plt.show()