# Linear solver
def my_linfit(x, y):
    N = len(x)
    b = (sum(y)-sum(x)*sum(x*y)/sum(x**2))/(N*(1+((sum(x))**2/(N*sum(x**2)))))
    a = (sum(x*y)-b*sum(x))/sum(x**2)
    return a, b

# Main
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np

    # Generate random data
    x = np.random.uniform(-2, 5, 10)
    y = np.random.uniform(0, 3, 10)


    # Fit line using custom function
    a, b = my_linfit(x, y)

    # Plot data points
    plt.plot(x, y, 'kx', label='Data')

    # Plot fitted line
    xp = np.arange(-2, 5, 0.1)
    plt.plot(xp, a * xp + b, 'r-', label=f'Fit: a={a}, b={b}')

    # Add legend and show plot
    plt.legend()
    plt.title("Linear Fit Example")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

    # Print fit parameters
    print(f"My fit: a={a} and b={b}")
