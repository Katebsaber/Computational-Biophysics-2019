from sys import argv
import numpy as np
from matplotlib import pyplot as plt

def velocity_verlet(x1,x2,v1,v2,k,dt,x_eq,m):
    a_t = k * ((x2 - x1) - x_eq) / m

    x1 = 0.5 * a_t * dt**2 + v1 * dt + x1
    x2 = -0.5 * a_t * dt**2 + v2 * dt + x2

    a_next = k * ((x2 - x1) - x_eq) / m

    v1 = 0.5 * (a_t + a_next) * dt + v1
    v2 = -0.5 * (a_t + a_next) * dt + v2

    eU = 0.5 * k * ((x2 - x1) - x_eq)**2
    eT = 0.5 * (v1**2 + v2**2)
    E = eU + eT

    return x1,x2,v1,v2,E


def euler(x1,x2,v1,v2,k,dt,x_eq,m):
    a_t = k * ((x2 - x1) - x_eq) / m

    x1 = v1 * dt + x1
    x2 = v2 * dt + x2

    v1 = a_t * dt + v1
    v2 = -1 * (a_t * dt) + v2
    
    eU = 0.5 * k * ((x2 - x1) - x_eq)**2
    eT = 0.5 * (v1**2 + v2**2)
    E = eU + eT

    return x1,x2,v1,v2,E



def leap_frog(x1,x2,v1,v2,k,dt,x_eq,m):
    x1 = x1 + v1 * dt
    x2 = x2 + v2 * dt 

    a_t = k * ((x2 - x1) - x_eq) / m

    v1 = v1 + a_t * dt
    v2 = v2 - a_t * dt

    eU = 0.5 * k * ((x2 - x1) - x_eq)**2
    eT = 0.5 * (v1**2 + v2**2)
    E = eU + eT

    return x1,x2,v1,v2,E




if __name__ == '__main__':
    print('Running {} algorithm for {} itterations'.format(argv[1],argv[2]))
    global x1 
    global x2 

    global v1 
    global v2 

    x1 = 1
    x2 = 3

    v1 = 0
    v2 = 0

    k = 1
    dt=0.01
    m=1
    x_eq = 1

    if argv[1] == 'leap':    
        a_t = k * ((x2 - x1) - x_eq) / m

        v1 = v1 + a_t * dt / 2
        v2 = v2 - a_t * dt / 2

    l_e = []
    for i in range(int(argv[2])):
        if argv[1] == 'verlet':
            x1,x2,v1,v2,e = velocity_verlet(x1,x2,v1,v2,k,dt,x_eq,m)
        elif argv[1] == 'euler':
            x1,x2,v1,v2,e = euler(x1,x2,v1,v2,k,dt,x_eq,m)
        elif argv[1] == 'leap':
            x1,x2,v1,v2,e = leap_frog(x1,x2,v1,v2,k,dt,x_eq,m)
        l_e.append(e)
        print(i,x1,x2,v1,v2,e)

    plt.plot(l_e)
    plt.show()
