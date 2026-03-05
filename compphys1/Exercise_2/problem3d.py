"""
Problem 3D: Interpolation
1D interpolation method comparison code
"""

import linear_interp
import spline_class

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

def interp_plot():
    """
    Creates two different figures. First one compares 1D linear interpolation to the 
    Hermite Cubic spline interpolation. Another one compares numpy's interpolation function and scipy's
    Cubic spline interpolation
    """
    # Data
    x = np.linspace(0,2*np.pi,11)
    y = np.sin(x)

    xx = np.linspace(x[0],x[-1],100)
    yy = np.zeros_like(xx)

    # 1D Linear
    for i in range(len(xx)):
        # Call interpolation function
        yy[i] = linear_interp.interp1d(xx[i],y,x)

    # Hermite Cubic Spline
    spl1d=spline_class.spline(x=x,f=y,dims=1)
    # Plotting
    fig1 = plt.figure()
    plt.plot(xx,yy,label='1D Linear')
    plt.plot(x,y,'o', label='data')

    plt.plot(xx,spl1d.eval1d(xx),'r--',label='Hermite cubic spline')
        
    plt.legend()
    plt.show()

    fig2 = plt.figure()
    # Numpy's 1D
    y_interp  = np.interp(xx,x,y)
    plt.plot(xx, y_interp, '-', label='Numpy linear interp')
    plt.plot(x, y, 'o', label='data')

    # Scipy's Cubic spline
    spl = CubicSpline(x, y)
    plt.plot(xx, spl(xx), label='Scipy Cubic spline')


    plt.legend()
    plt.show()



def main():
     interp_plot()


if __name__=="__main__":
    main()