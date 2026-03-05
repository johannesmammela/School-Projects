"""
Exercise 2: Problem 2a, N-dimensonal numerical gradient
Code for testing the numerical differential given in problem 2a. Compares numerical and analytical solution to each other
"""
import numpy as np

def num_grad(f,x,h,N):
    """
     Numerical differential
     Inputs:
     f: function to be derivated
     x: N-dimensional vector
     h: stepsize
     N: Number of dimensions
    """

    # Initialize gradient vector
    num_grad = np.zeros(N)

    # Run through every dimension
    for i in range(N):
        
        e = np.zeros(N)
        e[i] = 1.0

        # Append gradient value to gradient vector
        num_grad[i] = (1/(12*h))*(f(x-2*h*e)-8*f(x-h*e)+8*f(x+h*e)-f(x+2*h*e))
    return num_grad


def analytical_grad(x,N):
    """
     Analytical gradient
     Inputs: 
     x : N- dimensional vector
     N: Number of dimensions
    """

    x = np.asarray(x)

    # Calculate gradient values 
    grad = np.zeros_like(x)
    grad[0] = -np.sin(x[0])      
    grad[-1] = np.cos(x[-1])     
    
    if N > 2:
        grad[1:-1] = 3 * x[1:-1]**2   
        
    return grad


def calculate_derivatives(x,N):
    """
    # Function to derivative calculation. 
    # Inputs: 
    # x : N-dimensional vector
    # N : Number of dimensions
    """

    # Form function to be integrated
    def f(x):
        x = np.asarray(x)
        return np.cos(x[0])+np.sin(x[-1])+np.sum(x[1:-1]**3)
    
   # Call numerical and analytical functions
    df_numerical = num_grad(f,x,0.01,N)
    df_analytical = analytical_grad(x,N)
    
    # Print results
    print(f"x = {x}")
    print("Analytical gradient: ", df_analytical)
    print("Numerical gradient:  ", df_numerical)
    print("Difference:          ", np.linalg.norm(df_numerical - df_analytical))
    print("-" * 50)

    assert abs(np.linalg.norm(df_numerical - df_analytical)) < 0.1


def test_problem2b():
    # Test function

    # Form testing vectors
    test_vectors = [
            np.linspace(-0.5, 0.5, 3),     # N = 3
            np.linspace(-1.0, 1.0, 5),     # N = 5
            np.linspace(-1.0, 1.0, 7)]  # N = 7

    # Testing with different dimensions
    for vector in test_vectors:
        N = len(vector)
        calculate_derivatives(vector,N)
        print()
    
def main():

    test_problem2b()
   


if __name__=="__main__":
    main()