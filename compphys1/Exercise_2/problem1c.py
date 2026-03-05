"""
Exercise 2: Problem 1c, Integration
Author: Johannes Mämmelä
Calculates Simpson's, Trapezoid's and NQuad integrals for 3D function with different step sizes
"""

from scipy import integrate
import numpy as np
import pandas as pd

def calculate_integrals(f,x,y,z):
    """
    # Function for calculating Simpson's and Trapezoid's integrals.
    # Inputs: function f as an array. Gridpoints x,y,z as arrays
    # Return: integrated values
    """
    
    # Calculate integrals: First with respect of x, then y and finally z
    trapez_x = integrate.trapezoid(f,x, axis=0)
    trapez_xy = integrate.trapezoid(trapez_x,y, axis=0)
    trapez_xyz = integrate.trapezoid(trapez_xy,z, axis=0)


    simp_x = integrate.simpson(f,x, axis=0)
    simp_xy = integrate.simpson(simp_x,y, axis=0)
    simp_xyz = integrate.simpson(simp_xy,z, axis=0)

    return trapez_xyz, simp_xyz

    
def main():

    # Let's form an array which defines the number of gridpoints and initialize lists
    N = np.linspace(2,40,10)

    trapz_list = []
    simpson_list = []
    error_list = []

    # For-loop over the number of gridpoints
    for i in N:

        # Form gridpoints
        x_c = np.linspace(-10,10,int(i))
        y_c = np.linspace(-10,10,int(i))
        z_c = np.linspace(-10,10,int(i))

        # Calculate stepsizes
        dx = x_c[1]-x_c[0]
        dy = y_c[1]-y_c[0]
        dz = z_c[1]-z_c[0]

        # Calculate error and append to the list
        err = dx*dy*dz
        error_list.append(err)

        # Form a function to be integrated
        X_c, Y_c, Z_c = np.meshgrid(x_c, y_c, z_c, indexing="ij")
        r_a = -1.1
        r_b = 1.1
        dA = ((X_c-r_a)**2)+(Y_c**2)+(Z_c**2)
        dB = ((X_c-r_b)**2)+(Y_c**2)+(Z_c**2)
        c = np.abs((1/(2*np.sqrt(3*np.pi)))*((np.exp(-dA/3))+(np.exp(-dB/3))))**2

        # Calculate integrals and append to the lists
        trapz, simpson = calculate_integrals(c,x_c,y_c,z_c)

        trapz_list.append(trapz)
        simpson_list.append(simpson)
    
    # Form DataFrames
    simpson_list, trapz_list, error_list = pd.DataFrame(simpson_list), pd.DataFrame(trapz_list), pd.DataFrame(error_list)
    integrals = pd.concat([trapz_list,simpson_list,error_list],axis=1)
    integrals.columns = ["Trapezoid","Simpson","dx*dy*dz"]

    # Form a function form for NQUAD
    def c1(x_c,y_c,z_c):
        r_a = -1.1
        r_b = 1.1
        dA = ((x_c-r_a)**2)+(y_c**2)+(z_c**2)
        dB = ((x_c-r_b)**2)+(y_c**2)+(z_c**2)

        return np.abs((1/(2*np.sqrt(3*np.pi)))*((np.exp(-dA/3))+(np.exp(-dB/3))))**2
    
    # Calculate NQUAD
    n_quad_c, error_c = integrate.nquad(c1,[[-10, 10],[-10,10],[-10,10]])

    # Print answers
    print(integrals)
    print(f"NQuad: {n_quad_c} +/- {error_c}")

if __name__=="__main__":
    main()


