"""
Problem 5: Steepest Descent
Code is created for computing N-dimensional function minimum values with 3 different ways. 
By using own algorithm from problem 2b and scipy's minimize package 
"""
from problem2b import num_grad
import numpy as np
from scipy.optimize import minimize

def steepest_descent(f,x_init,a=0.5,tol=1e-4,counter_max=1000):
    """
    Steepest descent algorithm. Evaluates function minimum by using numerical gradient method from problem 2b
    - f: a function taking x as an argument
    - x_init: initial guess of optimization parameters
    - a: multiplier for the gradient (a>0)
    - tol: tolerance for the search (defaults to 1e-4)
    - counter_max: maximum number of iterations
    """
    counter = 0
    x = 1.0*x_init
    ngrad = 2*tol
    # loop coninues until teh norm of the gradient is smaller tha tolerance or the 
    # maximum number of iterations is reached
    while ngrad>tol and counter<counter_max:
        # Compute numerical gradient
        grad = num_grad(f,x,0.01,len(x))
        # Compute the norm of the gradient
        ngrad = np.sqrt(sum(grad**2))
        # Update
        dx = -(a/(ngrad+1))*grad
        x += dx
        counter += 1
    return x,counter



def test_function():
    # Function for testing the algorithm
    def f(x):
        return sum((x-2)**2)
    # Use different number of dimensions
    N_list = [5,10,15]
    for N in N_list:
        # Initial values
        x_init = np.ones(N)  
        x, counter = steepest_descent(f, x_init)
        print("Own algorithm")
        print(x)
       
        res = minimize(f,x_init)
        print("Scipy Minimize")
        print(res.x)

        assert  abs(np.linalg.norm(x - 2)) < 0.01

    


def main():

    test_function()


if __name__=="__main__":
    main()