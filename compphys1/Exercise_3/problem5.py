"""
Problem 5: Electric Field
Code to calculate the electric field caused by charged rod
at any point in space.
Function E_total_1 computes the net field in a case wherw lambda is constant
and E_total_2 handles the non-constant lambda cases.
Code also plots the charge distribution and computes net charge 
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson


def dE(x,r_p,lamb):
    """
    Computes differential electrical charge.
    Input:
    x : point on the rod
    r_p : point where charge is computed
    lamb : lambda
    Output:
    Differential
    """
    # Compute diffence between r and rod point x
    r_vec = r_p-np.array([x, 0.0,0.0])

    # Normalize
    r_norm = np.linalg.norm(r_vec)

    # Avoid dividing by 0
    if r_norm ==0:
        return np.array([0.0,0.0,0.0])
    return lamb*r_vec / (r_norm**3) 



def E_total_1(r_p, x_list):
    """
    Compute Net Charge at certain point with constant lambda
    Inputs:
    r_p : point coordinates
    x_list : charged 1D rod
    Output:
    Net charge as an array
    """
    #Lambda
    
    lamb = 1
    print()
    # Compute differential electrical field
    
    # For constant lambda

    dE_x = np.array([dE(x,r_p,lamb)[0] for x in x_list])
    dE_y = np.array([dE(x,r_p,lamb)[1] for x in x_list])
    dE_z = np.array([dE(x,r_p,lamb)[2] for x in x_list])

    # Compute simpson's integrall in different directions
    E_x = simpson(dE_x, x_list)
    E_y = simpson(dE_y, x_list)
    E_z = simpson(dE_z, x_list)

    return np.array([E_x, E_y, E_z])

def E_total_2(r_p, x_list,lamb_list):
    """
    Compute Net Charge at certain point with non-constant lambda
    Inputs:
    r_p : point coordinates
    x_list : charged 1D rod
    x0 : Initial charge rod value
    L : Defines the length of the rod
    Output:
    Net charge as an array

    """

    # Compute differentials in different directions
    dE_x = np.array([
        dE(x, r_p, lamb_val)[0]
        for x, lamb_val in zip(x_list, lamb_list)
    ])

    dE_y = np.array([
        dE(x, r_p, lamb_val)[1]
        for x, lamb_val in zip(x_list, lamb_list)
    ])

    dE_z = np.array([
        dE(x, r_p, lamb_val)[2]
        for x, lamb_val in zip(x_list, lamb_list)
    ])

    # Compute Net Electric Field
    E_x = simpson(dE_x, x_list)
    E_y = simpson(dE_y, x_list)
    E_z = simpson(dE_z, x_list)

    return np.array([E_x, E_y, E_z])



def main():
    # Form 1D -rod
    L = 2
    x_list = np.linspace(-L/2,L/2,1000)
    x0 = -L/2

    d = 1
    # define point where there charge is calculated
    r_p = np.array([L/2+d,0.0,0.0])

    # Compute Net electric field
    E_num = E_total_1(r_p, x_list)
    print("Numerical E:", E_num)

    lam = 1.0
    E_analytical = lam * (1/d - 1/(d+L))
    print("Analytical E_x:", E_analytical)
    
    # TASK 2: Non Constant Lambda

    #Lambda
    def lamb(x):
        return np.sin(4*np.pi*(x - x0)/L)**2 * np.exp(-(x - x0))

    # Take a list 
    lamb_list = lamb(x_list)

    # Create grid
    x = np.linspace(-2, 2, 40)
    y_neg = np.linspace(-1, -0.1, 20)
    y_pos = np.linspace(0.1, 1, 20)

    y = np.concatenate((y_neg, y_pos))

    X, Y = np.meshgrid(x, y)

    # Initialize Electric field vectors
    Ex = np.zeros_like(X)
    Ey = np.zeros_like(Y)

    # Compute over grid
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            r_p = np.array([X[i,j], Y[i,j], 0])
            # Compute Electric field
            E = E_total_2(r_p, x_list,lamb_list)
            Ex[i,j] = E[0]
            Ey[i,j] = E[1]
    

    # Plot figure
    plt.figure(figsize=(6,6))
    plt.quiver(X, Y, Ex, Ey, scale=75)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Electric field of the rod in xy-plane with non-constant lambda")
    


    # Task 3 : Charge distribution

    # Plot a charge distribution
    plt.figure()
    plt.plot(x_list,lamb_list,'b-')
    plt.title("Charge distribution along the rod")
    plt.show()

    # Net Charge bu using simpson

    Q = simpson(lamb_list, x_list)
    print(f"Net Charge: {Q}")



if __name__=="__main__":
    main()