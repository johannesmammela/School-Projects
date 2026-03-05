"""
Problem 4: Bisection Method
Code computes the index of function root (single) by using bisection method
"""

import numpy as np

def index_search(f):
    """
    Function for searching the root index.
    Input :
    f : function values as an array
    Return : Nearest index of the root and the number of iterations
    """

    # Define two initial indices and initialize iter counter 
    left = 0
    right = len(f)-1
    n_iters = 0

    # Loop goes on until, incicec are consecutive indices
    while right - left > 1:
        
        # Take the middle index
        middle = (left + right)//2
        n_iters+= 1

        # If the middle index and the right index are on different signs, substitute left index to the middle index
        # Else substitute right index
        if f[middle]*f[right] <= 0:
            left = middle

        else:
            right = middle

    return left, n_iters

def test_function():
    # Function for testing


    # Generate x-values
    dim = 50
    x =np.zeros(dim)
    x[0] = 0
    x_0 = 10**(-4)
    x_max = 50
    h = np.log((x_max/(x_0)+1))/(dim-1)
    for i in range(1,dim):
        x[i]=x_0*(np.exp(i*h)-1)

    
    xp = x[3]
    f = x-xp
    i,n_iters = index_search(f)

    print(i)
    print(n_iters)

    assert abs(f[i]) < 0.1




def main():
    test_function()


if __name__=="__main__":
    main()

