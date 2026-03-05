"""
Computational physics 1

1. Add code to function 'largest_eig'
- use the power method to obtain the largest eigenvalue and the 
  corresponding eigenvector of the provided matrix

2. Compare the results with scipy's eigs
- this is provided, but you should use that to validating your 
  power method implementation
- they should yield the same, if not, then something is still wrong!!

3. Add code to function 'eigen_solver'
- obtain neigs number of largest eigenvalues and corresponding
  eigenvectors
- compare against scipy's results, which should match yours

Notice: 
  - np.dot(A,x), A.dot(x), A @ x could be helpful for performing 
    matrix operations with sparse matrices
  - numpy's toarray function might prove useful, and in general
    you could manage without it
  - for vv^T like product you might want to use np.outer(v,v)
"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as sp
import scipy.sparse.linalg as sla
from scipy.integrate import simpson


def largest_eig(A,tol=1e-12,maxiters=100_000):
    """
    Code to calculate the largest eigenvalue and its corresponding vector.
    Inputs:
    A : matrix
    tol : tolerance
    maxiters: maximum number of iterations
    Outputs:
    eig : largest eigenvalue
    evec : corresponding vector
    """
    N = A.shape[0]
    eig = 0.0
    # Create random starting vector
    evec = np.ones(N)+abs(np.random.rand(N))
    # Normalize
    evec = evec / np.linalg.norm(evec)

    for _ in range(maxiters):
        # Multiply matrix by vector
        evec_new = A @ evec

        # Normalize new vector
        evec_new = evec_new / np.linalg.norm(evec_new)

         # Check convergence
        if np.linalg.norm(evec_new - evec) < tol:
            break
        # Substitute
        evec = evec_new

        # Estimate eigenvalue
        eig = (evec.T @ A @ evec) / (evec.T @ evec)

    return eig, evec

def eigen_solver(Ain,neigs=5,tol=1e-12):
    """
    Code to calculate the N largest eigenvalues and corresponding vectors of these.
    Inputs:
    A : matrix
    tol : tolerance
    neigs: number of eigenvalues to find
    Outputs:
    eig : largest eigenvalue
    evec : corresponding vector
    """

    # Matrix to array
    Amod = Ain.toarray()*1.0

    # Initialize to list
    eigs = []
    evecs = []
    
    # N rounds
    for _ in range(neigs):
        # Find largest eigenvalue
        eig, vec = largest_eig(Amod)

        # Append
        eigs.append(eig)
        evecs.append(vec)

        # Substact the eigenvector from matrix
        Amod = Amod - eig * np.outer(vec, vec)

    return np.array(eigs), np.array(evecs)

def make_matrix(grid):
    """
    Function to form a matrix.
    Input : grid
    Output : matrix
    """
    grid_size = grid.shape[0]
    dx = grid[1]-grid[0]
    dx2 = dx*dx
    
    H0 = sp.diags(
        [
            -0.5 / dx2 * np.ones(grid_size - 1),
            1.0 / dx2 * np.ones(grid_size) - 1.0/(abs(grid)+2.5),
            -0.5 / dx2 * np.ones(grid_size - 1)
        ],
        [-1, 0, 1])

    return H0
    
def main():
    
    x = np.linspace(-5,5,101)
    H0 = make_matrix(x)
    
    eigs, evecs = sla.eigsh(H0, k=1, which='LA')
    
    eig_val,eig_vec = largest_eig(H0)
    
    print('largest_eig estimate: ', eig_val)
    print('scipy eigsh estimate: ', eigs)
    
    psi0 = evecs[:,0]
    norm_const = np.sqrt(simpson(abs(psi0)**2,x=x))
    psi0 = psi0/norm_const

    psi0_ = eig_vec*1.0
    norm_const = np.sqrt(simpson(abs(psi0_)**2,x=x))
    psi0_ = psi0_/norm_const

    plt.plot(x,abs(psi0)**2,label='scipy eig. vector squared')
    plt.plot(x,abs(psi0_)**2,'r--',label='largest_eig vector squared')
    plt.legend(loc=0)
    
    if abs(eig_val-eigs)<1e-6 and np.amax(abs(abs(psi0)**2-abs(psi0_)**2))<1e-2:
        print("Working fine")
    else:
        print("\nNOT yet working as expected!\n")

    plt.show()

    N = 5

    eigs, evecs = eigen_solver(H0,N)

    print(f'{N} largest_eig estimates: ', eigs)

    eigs_sci, evecs_sci = sla.eigsh(H0, k=N, which='LA')

    reversed_eigs = np.flip(eigs_sci)

    print(f'{N} largest scipy eigsh estimates: ', reversed_eigs)



if __name__=="__main__":
    main()
