import numpy as np
def monte_carlo_integration(fun,xmin,xmax,Nblocks=10,Niters=100):
    # Monte Carlo Integration. As an output one gets the mean value of integrals between blocks and the standard deviation
    # Inputs:
    # fun: function to integrate
    # xmin: minimum value of x
    # xmax: maximum value of x
    # Nblocks: number of blocks (how many times block is formed)
    # Niters: number of points inside block
    block_values = np.zeros(Nblocks) # Initialize block values
    L = xmax-xmin # width of the block
    for block in range(Nblocks):
        for i in range(Niters):
            x = xmin+np.random.rand()*L # Random x-value which is bigger than xmin and smaller than xmax
            block_values[block] += fun(x) # Calculate function value at this point and sum the number to the others
        block_values[block] /= Niters # Calculate average inside one block
    I = L*np.mean(block_values) # Calculate average between blocks
    dI = L*np.std(block_values)/np.sqrt(Nblocks) # Calculate standard deviation between blocks
    return I,dI

def func(x):
    # Define the function
    return np.abs(np.cos(x))

def test_function():
    # Function for testing the simulation
    I,dI = monte_carlo_integration(func,0.,np.pi,100,100)
    
    print("Integrated value: {0:0.5f} +/- {1:0.5f}".format(I,2*dI))
    

    assert abs(I-2.0)<0.02
    assert abs(dI)<0.02


def main():
    test_function()

if __name__=="__main__":
    main()