"""
Exercise 2: Problem 1b, Integration
Calculates Simpson's, Trapezoid's and NQuad integrals for 2D function with different step sizes
"""

from scipy import integrate
import numpy as np
import pandas as pd

def calculate_integrals(f,x,y):
    """
    # Function for calculating Simpson's and Trapezoid's integrals.
    # Inputs: function f as an array. Gridpoints x and as arrays
    # Return: integrated values
    """
    
    # Calculate integrals: First with respect of x, then y
    
    trapez_x = integrate.trapezoid(f,x, axis=0)
    trapez_xy = integrate.trapezoid(trapez_x,y, axis=0)


    simp_x = integrate.simpson(f,x, axis=0)
    simp_xy = integrate.simpson(simp_x,y, axis=0)

    return trapez_xy, simp_xy

    
def main():

    # Let's form an array which defines the number of gridpoints and initialize lists
    N = np.linspace(2,40,10)

    trapz_list = []
    simpson_list = []
    error_list = []

    # For-loop over the number of gridpoints
    for i in N:
        
        # Form gridpoints
        x_b = np.linspace(0,2,int(i))
        y_b = np.linspace(-2,2,int(i))

        # Calculate stepsizes
        dx = x_b[1]-x_b[0]
        dy = x_b[1]-x_b[0]

        # Calculate error and append to the list
        err = dx*dy
        error_list.append(err)

        # Form a function to be integrated
        X_b, Y_b = np.meshgrid(x_b, y_b, indexing="ij")

        b = abs(X_b+Y_b)*np.exp(-0.5*np.sqrt((X_b**2)+(Y_b**2)))

        # Calculate integrals and append to the lists
        trapz, simpson = calculate_integrals(b,x_b,y_b)

        trapz_list.append(trapz)
        simpson_list.append(simpson)

    # Form DataFrames
    simpson_list, trapz_list, error_list = pd.DataFrame(simpson_list), pd.DataFrame(trapz_list), pd.DataFrame(error_list)
    integrals = pd.concat([trapz_list,simpson_list,error_list],axis=1)
    integrals.columns = ["Trapezoid","Simpson","dx*dy"]

    # Form a function form for QUADs

    def b1(x_b,y_b):
        return abs(x_b+y_b)*np.exp(-0.5*np.sqrt((x_b**2)+(y_b**2)))

    def quad_x(y):
        quad_x, _ = integrate.quad(lambda x: b1(x,y),0,2)
        return quad_x

    quad_xy, error = integrate.quad(quad_x,-2,2)

    nquad_xy, n_error = integrate.nquad(b1,[[0, 2],[-2,2]])

    print(integrals)
    print(f"Quad: {quad_xy} +/- {error}")
    print(f"NQuad: {nquad_xy} +/- {n_error}")
      
if __name__=="__main__":
    main()