from read_xsf_example import read_example_xsf_density
import numpy as np
from scipy.integrate import simpson
import matplotlib.pyplot as plt

def volume(lattice):
    """
    Compute unit cell volume
    Input: Reciprocal lattice vecctors
    """
    return abs(np.dot(lattice[0], np.cross(lattice[1], lattice[2])))
    
def number_of_electrons(lattice, grid, density):
    """
    Compute number of electrons
    
    :param lattice: lattice vectors
    :param grid: grid
    :param density: electron density matrix
    """

    # Compute Volume
    V = abs(np.dot(lattice[0], np.cross(lattice[1], lattice[2])))
    
    nx, ny, nz = grid
    # Create coordinates in different directions
    x = np.linspace(0, np.linalg.norm(lattice[0]), nx)
    y = np.linspace(0, np.linalg.norm(lattice[1]), ny)
    z = np.linspace(0, np.linalg.norm(lattice[2]), nz)
    
    # 3D Simpson-integral
    Ne_z = simpson(density, z, axis=2)
    Ne_yz = simpson(Ne_z, y, axis=1)
    Ne = simpson(Ne_yz, x, axis=0)

    # Volume per grid point
    dV = V / (nx * ny * nz)
 
    return Ne

def cartesian_to_fractional(r, lattice):
    """
    Changes coordinates from cartesian to fractional
    """
    return np.linalg.solve(lattice, r) % 1.0  

def trilinear_interpolation(frac, density):
    """
    Function to trilinear interpolation in 3D electron density grid
    Inputs:
    frac : fractal coordinates
    density : known electron densities
    """
    nx, ny, nz = density.shape

    # Change fractal coordinates to grid-coordinates
    x = frac[0] * nx
    y = frac[1] * ny
    z = frac[2] * nz

    # Search the corner of the cube and define periodical conditions
    i = int(np.floor(x)) % nx
    j = int(np.floor(y)) % ny
    k = int(np.floor(z)) % nz

    # Calculate distance inside the cube
    dx = x - i
    dy = y - j
    dz = z - k

    def idx(a, n): return a % n

    # Search eight nearest points (corners)
    c000 = density[idx(i, nx), idx(j, ny), idx(k, nz)]
    c100 = density[idx(i+1, nx), idx(j, ny), idx(k, nz)]
    c010 = density[idx(i, nx), idx(j+1, ny), idx(k, nz)]
    c001 = density[idx(i, nx), idx(j, ny), idx(k+1, nz)]
    c110 = density[idx(i+1, nx), idx(j+1, ny), idx(k, nz)]
    c101 = density[idx(i+1, nx), idx(j, ny), idx(k+1, nz)]
    c011 = density[idx(i, nx), idx(j+1, ny), idx(k+1, nz)]
    c111 = density[idx(i+1, nx), idx(j+1, ny), idx(k+1, nz)]

    # Interpolate in x-direction
    c00 = c000*(1-dx) + c100*dx
    c01 = c001*(1-dx) + c101*dx
    c10 = c010*(1-dx) + c110*dx
    c11 = c011*(1-dx) + c111*dx

    # y-direction
    c0 = c00*(1-dy) + c10*dy
    c1 = c01*(1-dy) + c11*dy

    # z-direction
    return c0*(1-dz) + c1*dz

def main():
    filename = 'dft_chargedensity2.xsf'
    # compute reprocical lattice and electron densitise
    rho, lattice, grid = read_example_xsf_density(filename)

    print('Real space lattice vectors in {}'.format(filename))
    print(lattice)
    print()
    Ne = number_of_electrons(lattice, grid, rho)

    # Must be integer
    Ne = Ne // 1

    print("Total Number of electrons:", Ne)


    # b)
    # Define line
    r0s = np.array([[-1.4466, 1.3073, 3.2115], 
                   [2.9996, 2.1733, 2.1462]
                   ])
    r1s = np.array([[1.4321, 3.1883, 1.3542],
                    [8.7516, 2.1733, 2.1462]
                    ])
    fig, axes = plt.subplots(1,2,sharey=True, figsize=(12,4))

    for ax, r0,r1 in zip(axes, r0s,r1s):
        npoints = 401

        dens_line = []
        distances = []

        for t in np.linspace(0, 1, npoints):
            # for every point at the line
            # whwn t = 0, r -> r0
            # when t = 1, r-> r1
            r = r0 + t * (r1 - r0)
            frac = cartesian_to_fractional(r, lattice)
            # Compute electron density in point r
            rho_tri = trilinear_interpolation(frac, rho)

            dens_line.append(rho_tri)
            distances.append(np.linalg.norm(r - r0))

        dens_line = np.array(dens_line)
        distances = np.array(distances)

        # Plot

        
        ax.plot(distances, dens_line)
        ax.set_xlabel("Distance along line (Å)")
        ax.set_ylabel("Electron density (Å^-3)")
        
    #plt.show()
    plt.tight_layout()
    plt.savefig("problem4b.pdf")
       
    
if __name__=="__main__":
    main()