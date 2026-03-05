import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def make_matrix(x):
    """
    "Mystery matrix"
    Function to generate matrix based on the grid
    Inputs: grid x
    Output: NxN matrix
    """
    # Task 2b, explanation of mystery matrix derivation


    # This matrix approximates the first derivative df/dx on a 1D grid.
    # For interior points, we use the second-order accurate central difference:
    #
    #   f'(x_i) ≈ ( f_{i+1} − f_{i-1} ) / (2h)
    #
    # This gives coefficients:
    #   −1/(2h) at i−1
    #   +1/(2h) at i+1
    # Hence the tridiagonal structure:
    #   A[i,i−1] = −1
    #   A[i,i+1] = +1
    # and the matrix is scaled by 1/(2h).
    #
    # At the left boundary (i = 0), central difference is impossible,
    # so we use a second-order forward difference:
    #
    #   f'(x_0) ≈ ( −3f_0 + 4f_1 − f_2 ) / (2h)
    #
    # At the right boundary (i = N−1), we use a second-order backward difference:
    #
    #   f'(x_{N−1}) ≈ ( 3f_{N−1} − 4f_{N−2} + f_{N−3} ) / (2h)
    #
    # These give the boundary row coefficients:
    #   Left boundary  = [−3, 4, −1]
    #   Right boundary = [1, −4, 3]
    #
    # Therefore, the matrix is a discrete first-derivative operator:
    #   A f ≈ df/dx


    # Number of grid values
    N = len(x)
    # Difference between first and second value of the grid
    h = x[1]-x[0]
    # Creates N-1 ones
    off_diag = np.ones(N-1)
    # Form a matrix A whose mid-diagonal has value 0,
    # diagonal upper has value 1 and lower diagonal has value -1
    # Everywhere else has value 0
    # Example:
    # 0 1 0 
    #-1 0 1 
    # 0 -1 0
    A = np.zeros((N,N)) - np.diag(off_diag,-1) + np.diag(off_diag,1)
    # Changes three first values from first row
    A[0,0:3] = [-3.0,4.0,-1.0]
    # Changes three last values from the last row 
    A[-1,-3:] = [1.0,-4.0,3.0] 
    print()
    # Returns a matrix where every value has divided first by 2*h 
    return A/h/2

def main():
    # Create grid
    N = 50
    grid = np.linspace(0,np.pi,N)
    # Create x-values
    x_values = [np.sin(grid), np.cos(grid), np.exp(2*grid), grid**4]
    function_names = ["Sine","Cosine","Exponential","Fourth degree polynomial"]
    # Create matrix A
    A = make_matrix(grid)
    X = A.shape
    print(A)

    # Create 2x2 subplot figure
    fig, axes = plt.subplots(2,2, figsize=(18,6), sharex=True, sharey=False, constrained_layout=True)

    # Run over different functions and plot it to own subplot
    for ax, x, name in zip(axes.flatten(),x_values, function_names):
    
        # calculate here b=Ax as described in the problem setup
        b = np.dot(A,x)
        print()
        try:
            ax.plot(grid,b,'--')
            ax.plot(grid,x,'--')
            ax.set_title(f"x-values: {name}")
            ax.legend(["b=Ax","x"])
    
        except:
            print("  You need to first calculate b using A and x")
            print("  as described in the problem setup.")
    plt.show()

if __name__=="__main__":
    main()



