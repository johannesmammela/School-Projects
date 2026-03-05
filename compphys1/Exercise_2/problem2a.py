"""
Exercise 2: Problem 2a, N-dimensonal numerical gradient
Code for forming coefficient matrix to determine the symmetric derivative formulas.
"""
import numpy as np


def form_matrix():
    # 1. Form 4th degree Taylor series terms f(x+h), f(x-h), f(x+2h) and f(x-2h)
    # I have formed these to the notebook and weighth of the constants are based on these
    # 2. Form sum a*f(x+h)+b*f(x-h)+c*f(x+2h)+d*f(x-2h)

    # 3. Let's form the conditional equations. Only the first differential term should stay
    #    Other terms should disappear if we want to solve first differential

    # Equations:
    # a+b+c+d = 0
    # a-b+2c-2d = 1
    # a+b+4c+4d = 0
    # a-b+8c-8d = 0

    # 4. Based on these equations we can form a coefficient matrix A

    A = np.array([[1,1,1,1],
                  [1,-1,2,-2],
                  [1,1,4,4],
                  [1,-1,8,-8]                
                  ], dtype=float)
    print("Coefficient matrix:")
    print(A)
    print()
    print("Constant values (a,b,c,d)")
    # First derivative
    b1 = [0,1,0,0]
    x1 = np.linalg.solve(A,b1)
    print("First derivative:")
    print(f"1/12*{x1*12}")
    print()
    # Second derivative
    b2 = [0,0,1,0]
    x2 = np.linalg.solve(A,b2)
    print("Second derivative:")
    print(f"1/12*{x2*12}")
    print()

    # So, expression for the second derivative:
    # f'(x) = 1/12h[-2f(x+h)-2f(x-h)+2f(x+2h)+2f(x-2h)]. Error term is O(h^3) 


    #Third derivative
    b3 = [0,0,0,1]
    x3 = np.linalg.solve(A,b3)
    print("Third derivative:")
    print(f"1/12*{x3*12}")

    # So, expression for the second derivative:
    # f'(x) = 1/12h[-2f(x+h)+2f(x-h)+f(x+2h)-f(x-2h)]. Error term is O(h^2)

def main():
    form_matrix()

if __name__=="__main__":
    main()