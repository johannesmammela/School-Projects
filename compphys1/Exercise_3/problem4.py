"""
Problem 4: 2D Interpolation
Description under the "visualize" function
"""

import numpy as np
import matplotlib.pyplot as plt
from spline_class import spline

def visualize(xexp,yexp,Fexp,y_ref):
    """
    Computes 2d spline interpolation and presents the visualization.
    Plot 1x2 subplot, where the subfigure on left presents the original experimental data and
    subfigure on the right presents the interpolated values and reference data.
    Inputs:
    xexp : x-grid
    yexp : y-grid
    Fexp : experimental data
    y_ref : reference data
    """
    X,Y = np.meshgrid(xexp,yexp,indexing="ij")

    # Create path data
    x_path = np.linspace(0,1.81,100)
    y_path = (1/3)*x_path**3
    
    # Spline interpolation
    spl2d = spline(x=xexp,y=yexp,f=Fexp, dims=2)
    Z = np.array([spl2d.eval2d(xexp, yexp) for xexp, yexp in zip(x_path, y_path)])


    # Create figure
    fig, axes = plt.subplots(1,2, figsize=(10,6), sharex=True, sharey=False, constrained_layout=True)

    # Plot interpolated and reference data on the right
    axes[1].plot(x_path,Z,color='red',linestyle='dotted',label='spline',linewidth=4)
    axes[1].plot(x_path,y_ref,'-',label='reference',linewidth=2)
    axes[1].set_title('2d spline interpolation')
    axes[1].legend()
    
 
    # Plot experimental data and path on the left
    axes[0].contourf(X,Y,Fexp)
    axes[0].scatter(X,Y,color="red")
    axes[0].plot(x_path,y_path,'k--', linewidth=4)
    
    plt.show()



def main():

    # Load data
    xexp = np.loadtxt("x_grid.txt")
    yexp = np.loadtxt("y_grid.txt")
    Fexp = np.loadtxt("exp_data.txt")

    y_ref = np.loadtxt("ref_interpolated.txt")
    Fexp = Fexp.reshape([len(xexp),len(yexp)])

    # Visualize
    visualize(xexp,yexp,Fexp,y_ref)

if __name__=="__main__":
    main()
