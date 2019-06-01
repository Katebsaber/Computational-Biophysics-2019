# 1D simulation of two masses connected by a spring
The goal of this simulation is to test stability of 3 integration algorithms against each other:

1. Euler
2. Leap frog
3. Velocity verlet

## Usage

```bash
python main_r01.py <option> <itteration>
#Options = euler, verlet, leap
#Itterations = int number
```

Examples:

```bash
python main.py euler 5000
python main.py verlet 5000
python main.py leap 5000
```



## Further references

You can find elaborate explanation on numerical analysis algorithms in following links:

> http://www2.math.umd.edu/~dlevy/classes/amsc466/lecture-notes/integration-chap.pdf
>
> http://tutorial.math.lamar.edu/Classes/DE/EulersMethod.aspx
>
> http://www.physics.udel.edu/~bnikolic/teaching/phys660/numerical_ode/node5.html   