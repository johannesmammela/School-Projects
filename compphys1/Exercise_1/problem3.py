""" 
Problem 3, Johannes Mämmelä: Code for calculating
the first and the second derivatives by using Taylor Series
"""


import numpy as np
def first_derivative(f, x, h):
    # function to calculate the first derivative
    # return: differentiated function
    df = (f(x+h)-f(x-h))/(2*h)

    return df

def second_derivative(f,x,h):
    # function to calculte the second derivative
    # return: differentiated function (second derivative)
    ddf = (f(x+h)+f(x-h)-2*f(x))/(h**2)
    return ddf


def test_first_derivative():
    # function for first derivate testing
    # return: function to be differentiated
    def f(x):
        return 2*x**2
    
    df = first_derivative(f,1,0.1)
    
    print(df)

    assert abs(df-4.0) < 0.1

def test_second_derivative():
    # function for second derivate testing
    # return: function to be differentiated

    def f(x):
        return 2*x**2
    
    ddf = second_derivative(f,1,0.1)
    print(ddf)


    assert abs(ddf-4.0) < 0.1

    

    

def main():
    # main function
    test_first_derivative()
    test_second_derivative()

    

if __name__=="__main__":
    main()







