from problem4a import trapezoid
from problem3 import first_derivative
import numpy as np
import matplotlib.pyplot as plt


def calculate_derivative_errors():
    # Function for calculating derivation errors.

    def f(x): 
        return np.sin(x)
    
    dx_values = np.linspace(0,0.8,398)
    der_errors = []
    for dx in dx_values: # Go through all dx-values
        num_der = first_derivative(f,0.5,dx)
        exact_der = np.cos(0.5)
        error = abs(num_der - exact_der) # Calculate error

        der_errors.append(error) # Append to list
        

    return der_errors, dx_values

def calculate_integral_errors():
    # Function for calculating integration errors.

    dx_list =[]
    int_error_list = []

    for i in range(400,1,-1):

        dx = (np.pi/2)/i # Form dx-values

        x = np.linspace(0,np.pi/2,i+1)
        f = np.cos(x)
        trap = trapezoid(f,x)
        exact_int = 1

        error = abs(trap - exact_int) # Calculate error

        # Append to lists
        dx_list.append(dx) 
        int_error_list.append(error)
       
    return int_error_list, dx_list


def my_plot(der_errors, int_errors, dx_list_der, dx_list_int):
    # Function for plotting. Plots integration and derivation errors as a function of dx.

    
    fig = plt.figure(figsize=(12,8))
   
    ax = fig.add_subplot()

    ax.plot(dx_list_der, der_errors,color="orange", linewidth=2, linestyle="--")
    ax.plot(dx_list_int, int_errors,color="blue", linewidth=2)

    ax.legend(["derivation", "integration"])

    ax.set_xlabel("dx")
    ax.set_ylabel("|exact - numeric|")

    plt.show()



def main():
    der_errors, dx_list_der = calculate_derivative_errors()
    int_errors, dx_list_int = calculate_integral_errors()
    my_plot(der_errors, int_errors, dx_list_der, dx_list_int)


main()