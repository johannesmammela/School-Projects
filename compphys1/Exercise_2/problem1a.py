"""
Exercise 2: Problem 1a, Integration
Calculates Simpson's, Trapezoid's, Quad and NQuad integrals for 1D function with different step sizes
"""

from scipy import integrate
import numpy as np
import pandas as pd

def calculate_integrals(f,x):
    """
    # Function for calculating Simpson's and Trapezoid's integrals.
    # Inputs: function f as an array. Gridpoints x as arrays
    # Return: integrated values
    """
   
    trapez = integrate.trapezoid(f,x)
    simp = integrate.simpson(f,x)

    return trapez, simp



def main():

    # Let's form an array which defines the number of gridpoints and initialize lists
    N = np.linspace(2,40,10)

    f_list_trapz, f_list_simpson = [], []
    g_list_trapz, g_list_simpson = [], []
    h_list_trapz, h_list_simpson = [], []
    dr_list, dx1_list, dx2_list = [], [], []

    for i in N:

        #Form gridpoints and stepsizes
        r = np.linspace(0,20,int(i))
        dr = r[1]-r[0]
        dr_list.append(dr)

        x1 = np.linspace(0.001,1,int(i))
        dx1 = x1[1]-x1[0]
        dx1_list.append(dx1)

        x2 = np.linspace(0.001,5,int(i))
        dx2 = x2[1]-x2[0]
        dx2_list.append(dx2)

        # Form functions to be integrated

        f = (r**2)*np.exp(-2*r)
        g = np.sin(x1)/x1
        h = np.exp(np.sin(x2**3))

        # Calculate Simpson and Trapezoid 

        trapz_f, simpson_f = calculate_integrals(f,r)
        f_list_trapz.append(trapz_f)
        f_list_simpson.append(simpson_f)

        trapz_g, simpson_g = calculate_integrals(g,x1)
        g_list_trapz.append(trapz_g)
        g_list_simpson.append(simpson_g)
    
        trapz_h, simpson_h = calculate_integrals(h,x2)
        h_list_trapz.append(trapz_h)
        h_list_simpson.append(simpson_h)

    # Form DataFrames
    f_simpson_list, f_trapz_list, dr_list = pd.DataFrame(f_list_simpson), pd.DataFrame(f_list_trapz), pd.DataFrame(dr_list)
    integrals_f = pd.concat([f_trapz_list,f_simpson_list,dr_list],axis=1)
    integrals_f.columns = ["Trapezoid","Simpson","dx"]

    g_simpson_list, g_trapz_list, dx1_list = pd.DataFrame(g_list_simpson), pd.DataFrame(g_list_trapz), pd.DataFrame(dx1_list)
    integrals_g = pd.concat([g_trapz_list,g_simpson_list,dx1_list],axis=1)
    integrals_g.columns = ["Trapezoid","Simpson","dx"]

    h_simpson_list, h_trapz_list, dx2_list = pd.DataFrame(h_list_simpson), pd.DataFrame(h_list_trapz), pd.DataFrame(dx2_list)
    integrals_h = pd.concat([h_trapz_list,h_simpson_list,dx2_list],axis=1)
    integrals_h.columns = ["Trapezoid","Simpson","dx"]

    # Form function for quad and nquad
    def f1(r):
        return (r**2)*np.exp(-2*r)
    
    # Calculate integrals
    quad_f, error_f = integrate.quad(f1,0,np.inf)
    nquad_f, n_error_f = integrate.nquad(f1,[[0, np.inf]])

    def g1(x1):
        return np.sin(x1)/x1
    
    quad_g, error_g = integrate.quad(g1,0,1)
    nquad_g, n_error_g = integrate.nquad(g1,[[0, 1]])
    

    def h1(x2):
        return np.exp(np.sin(x2**3))
    
    quad_h, error_h = integrate.quad(h1,0,5)
    nquad_h, n_error_h = integrate.nquad(h1,[[0, 5]])


    #Print
    print(integrals_f)
    print(f"Quad: {quad_f} +/- {error_f}")
    print(f"NQuad: {nquad_f} +/- {n_error_f}")
    print()


    print(integrals_g)
    print(f"Quad: {quad_g} +/- {error_g}")
    print(f"NQuad: {nquad_g} +/- {n_error_g}")
    print()

    print(integrals_h)
    print(f"Quad: {quad_h} +/- {error_h}")
    print(f"NQuad: {nquad_h} +/- {n_error_h}")


if __name__=="__main__":
    main()