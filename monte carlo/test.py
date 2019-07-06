import numpy as np

x = np.arange(50)
x = x.reshape((5,10))

print(x)

# print(np.roll(x,1,axis=1)) #left
# print(np.roll(x,-1,axis=1)) #right

# print(np.roll(x,1,axis=0)) #up
# print(np.roll(x,-1,axis=0)) #down

# print(np.roll(np.roll(x,1,axis=1),1,axis=0)) #left up
# print(np.roll(np.roll(x,1,axis=1),-1,axis=0)) #left down
# print(np.roll(np.roll(x,-1,axis=1),1,axis=0)) #right up
# print(np.roll(np.roll(x,-1,axis=1),-1,axis=0)) #right down