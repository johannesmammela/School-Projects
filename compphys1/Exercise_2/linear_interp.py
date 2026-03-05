"""
Module for simple linear interpolation

Assignment:
- Fill in the calculations for 1d, 2d and 3d linear interpolations
  using the linear basis functions l1 and l2 given below
  and defined in the lectures
"""

import numpy as np
import matplotlib.pyplot as plt

l1 = lambda t: 1.0-t
l2 = lambda t: t

def get_index(x0,x):
    # Function to find index of the interval
    # Inputs:
    # x0 : the point at which interpolation is performed
    # x : array, grid of values
    # Return : Index of the interval 
    if (x0<=x[0]):
        i = 0
    elif (x0>=x[-2]):
        i = len(x)-2
    else:
        i = np.where(x<=x0)[0][-1]
    return i

def interp1d(x0,f,x):
    # Perform 1D linear interpolation at point x0
    # Inputs:
    # f : array, function values at grid points x
    # x : array, grid of x-values

    # Return: Interpolated value

    i = get_index(x0,x)
    # Compute linear interpolation
  
    s = f[i]+(f[i+1]-f[i])*(x0-x[i])/(x[i+1]-x[i])
  
    return s

def interp2d(x0,y0,f,x,y):
    # Perform 2D bilinear interpolation at point (x0,y0)
    # Inputs:
    # x0,y0 : coordinates of the point
    # f : 2D array, function values
    # x and y : arrays,grid points in x and y directions
    # Return : Interpolated value
    i = get_index(x0,x)
    j = get_index(y0,y)

    # Compute normalized local coordinates
    tx = (x0-x[i])/(x[i+1]-x[i])
    ty = (y0-y[j])/(y[j+1]-y[j])

    # Construct row and column vectors of basis functions
    lx = np.array([[l1(tx), l2(tx)]])
    ly = np.array([[l1(ty)], [l2(ty)]])

    # Extract 2x2 submatrix of function values
    F = np.array([
        [f[i,j], f[i,j+1]],
        [f[i+1,j],f[i+1,j+1]]
    ])

    # Compute bilinear interpolation
    s = lx @ F @ ly
    s = s.item() # Convert array to scalar
    return s

def interp3d(x0,y0,z0,f,x,y,z):
    # Perform 3D trilinear interpolation at point (x0,y0)
    # Inputs:
    # x0,y0, x0 : coordinates of the point
    # f : 3D array, function values
    # x,y, z : arrays,grid points in x and y directions
    # Return : Interpolated value
    i = get_index(x0,x)
    j = get_index(y0,y)
    k = get_index(z0,z)
    
    # Compute normalized local coordinates
    tx = (x0-x[i])/(x[i+1]-x[i])
    ty = (y0-y[j])/(y[j+1]-y[j])
    tz = (z0-z[k])/(z[k+1]-z[k])

    # Construct row and column vectors of basis functions
    lx = np.array([[l1(tx), l2(tx)]])
    ly = np.array([[l1(ty)], [l2(ty)]])
    lz = np.array([[l1(tz)], [l2(tz)]])

    # Extract two 2x2 slices in z-direction 
    Ak = np.array([
        [f[i,j,k], f[i,j+1,k]],
        [f[i+1,j,k], f[i+1,j+1,k]]

    ])
    Ak_1 = np.array([
        [f[i,j,k+1], f[i,j+1,k+1]],
        [f[i+1,j,k+1], f[i+1,j+1,k+1]]

    # interpolate in y-direction
    ])
    A1 = Ak @ ly
    A2 = Ak @ ly

    # Combine slices
    A = np.hstack([A1,A2])
    s = lx @ A @ lz
    s = s.item() # Convert array to scalar
 
    return s
    
def test1d():
    """
    Test function for 1D interpolation.
    Compares interpolated values with the sine function.
    """
    
    x = np.linspace(0,np.pi,10)
    y = np.sin(x)
    xx = np.linspace(x[0],x[-1],100)
    yy = np.zeros_like(xx)
    for i in range(len(xx)):
        # Call interpolation function
        yy[i] = interp1d(xx[i],y,x)
    # Plotting
    plt.plot(xx,yy)
    plt.plot(x,y,'o')
    

def test2d():
    """
    Test function for 2D interpolation.
    Creates an original surface and compares it to the interpolated surface.
    """
    fig=plt.figure()
    ax=fig.add_subplot(121)
    xo=np.linspace(0.0,3.0,11)
    yo=np.linspace(0.0,3.0,12)
    X,Y = np.meshgrid(xo,yo,indexing="ij")
    Zorig = (X+Y)*np.exp(-1.0*(X*X+Y*Y)**2)
    ax.pcolor(X,Y,Zorig)
    ax.set_title('original')

    ax2=fig.add_subplot(122)
    x = np.linspace(0.0,3.0,51)
    y = np.linspace(0.0,3.0,51)
    X,Y = np.meshgrid(x,y,indexing="ij")
    Z = np.zeros((len(x),len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            # Call interpolation function
            Z[i,j] = interp2d(x[i],y[j],Zorig,xo,yo)
    ax2.pcolor(X,Y,Z)
    ax2.set_title('interpolated')

def test3d():
    """
    Test function for 3D interpolation.
    Compares the original 3D function slice with interpolated slices.
    """
    x=np.linspace(0.0,3.0,10)
    y=np.linspace(0.0,3.0,11)
    z=np.linspace(0.0,3.0,10)
    X,Y,Z = np.meshgrid(x,y,z,indexing="ij")
    F = (X+Y+Z)*np.exp(-1.0*(X*X+Y*Y+Z*Z))
    X,Y = np.meshgrid(x,y,indexing="ij")
    fig3d=plt.figure()
    ax=fig3d.add_subplot(121)
    ax.pcolor(X,Y,F[...,int(len(z)/2)])
    ax.set_title('original (from 3D data)')

    ax2=fig3d.add_subplot(122)
    xi=np.linspace(0.0,3.0,50)
    yi=np.linspace(0.0,3.0,50)
    zi=np.linspace(0.0,3.0,50)
    X,Y = np.meshgrid(xi,yi,indexing="ij")
    Fi=np.zeros((len(xi),len(yi),len(zi)))
    # Compute trilinear interpolation
    for i in range(len(xi)):
        for j in range(len(yi)):
            for k in range(len(zi)):
                # Call interpolation function
                Fi[i,j,k] = interp3d(xi[i],yi[j],zi[k],F,x,y,z)
    ax2.pcolor(X,Y,Fi[...,int(len(z)/2)])
    ax2.set_title('linear interp. (from 3D data)')
    

def main():
    
    try:
        test1d()
    except:
        pass
    
    try:
        test2d()
    except:
        pass

    try:
        test3d()
    except:
        pass
    
    plt.show()

"""
AI-tools were used to find right commands explain some code rows.
"""

if __name__=="__main__":
    main()
