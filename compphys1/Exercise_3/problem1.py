"""
Exercise 3: Problem 1, 3D integral revisited
Computes Simpson's, integral for 3D function with different step sizes and NQuad's integral for the comparison.
There is two different solutions for Simpson's integral. One uses meshgrid and another computes through for-loops
"""

from scipy.integrate import simpson, nquad
import numpy as np
import pandas as pd

def meshgrid_solution(x,y,z,N):
    """
    Computes 3D-integral by using meshgrid.
    Inputs:
    Gridpoints x, and z as arrays. 
    N : Number of gridpoints in x-direction
    """

    X, Y, Z = np.meshgrid(x, y, z, indexing="ij")
    # Form a function as an array
    f = (X+Y)**2*np.exp(-np.sqrt(X**2+Y**2+Z**2))*np.sin(Z*np.pi)

    # Compute integral first with respect of x
    simp_x = simpson(f,x, axis=0)
    # Then the solution with respect of y
    simp_xy = simpson(simp_x,y, axis=0)
    # And finally with respect of z
    simp_xyz = simpson(simp_xy,z, axis=0)
    
    # Print solution
    print(f"Meshgrid Solution, Nx={N}: {simp_xyz}")

def for_loop_solution(x,y,z,N):
    """
    For-Loop solution to compute 3D Simpon's integral. Meshgrid or higher dimensional arrays are not used.
    Gridpoints x, and z as arrays. 
    N : Number of gridpoints in x-direction
    """

    # initialize final integral value
    simp  = 0.0

    # Initialize array for results as function of z
    Iz = np.zeros(len(z))

    # Outer loop: Runs through the z-direction
    for k, z_k in enumerate(z):

        # Initialize array for results as function of y
        Iy = np.zeros(len(y))

        # Inner loop: Runs through the y-direction
        for j, y_j in enumerate(y):
            # Form a function to be integrated
            f = ((x+y_j)**2)*np.exp(-np.sqrt(x**2+y_j**2+z_k**2))*np.sin(z_k*np.pi)

            # integral over x by running through z and y values. Save the results to Iy
            Iy[j] = simpson(f,x)

        # integral over y by running through z-values
        Iz[k] = simpson(Iy,y)
    
    # Final integral over z
    simp = simpson(Iz,z)
    # Print results
    print(f"For-Loop Solution, Nx={N}: {simp}")


def test_function():
    # List of N_x values
    N_list = [8,12,16,20]

    # Compute with different step sizes
    for N in N_list:

        # Create gridpoints
        x = np.linspace(0,2,int(N))
        y = np.linspace(-2,2,2*int(N))
        z = np.linspace(-1,2,int((3/2)*N))

        
        # Simpon's integral bys using meshgrid
        meshgrid_solution(x,y,z,N)

        # Simpson's integral without using meshgrid 
        for_loop_solution(x,y,z,N)
        print()
    
    
    #Compute NQuad

    # Create a function to be integrated in a function form
    def g(x,y,z):
        return ((x+y)**2)*np.exp(-np.sqrt(x**2+y**2+z**2))*np.sin(z*np.pi)

    # Compute
    n_quad, error = nquad(g,[[0, 2],[-2,2],[-1,2]])

    # Print result
    print(f"NQuad: {n_quad} +/- {error}")


def main():
    test_function()

if __name__=="__main__":
    main()
