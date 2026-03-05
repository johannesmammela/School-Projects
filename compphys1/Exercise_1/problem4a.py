""" 
Problem 4a, Johannes Mämmelä: Functions for calculating Riemann sum,
trapezoidal rule and Simpson's rule
"""
import numpy as np
from scipy import integrate

def riemann(f,x):
    # Calculates and returns Riemann sum
    # f: Array of function values
    # x: Array of grid points 
    rie = sum(f[i] * (x[i] - x[i-1]) for i in range(1, len(x)))

    return rie

def trapezoid(f,x):
    # Calculates and returns Trapezoid rule
    # f: Array of function values
    # x: Array of grid points 
    trap = sum(0.5 * (f[i] + f[i-1]) * (x[i] - x[i-1]) for i in range(1, len(x)))
 
    return trap

def simpson(f,x):
    # Simpson's rule for nonuniform grid
    # f: Array of function values
    # x: Array of grid points 
    

    N = len(x)-1
    dx = x[1] - x[0] 
    
    # Case 1: Even number of intervals
    if N % 2 == 0:
        return integrate.simpson(f,x)

    # Case 2: odd number of intervals
    f_even = f[:-1] 

    I_even = (dx / 3) * np.sum(
        f_even[0:-2:2] + 4 * f_even[1:-1:2] + f_even[2::2]
    )

    dI = (dx / 12) * (-f[-3] + 8 * f[-2] + 5 * f[-1])

    return I_even + dI


def test_function():
    # Function for testing all the methods

    x = np.linspace(0,np.pi/2,100)
    f = np.sin(x)

    Ir = riemann(f,x)
    assert abs(Ir-1.0)<1e-2

    It = trapezoid(f,x)
    assert abs(It-1.0)<1e-2


    Is = simpson(f,x)
    assert abs(Is-1.0)<1e-2



def main():
    test_function()

main()

# AI usage:
# An AI-based tool was used to find and understand the solution for the simpson's rule
# for odd number of intervals