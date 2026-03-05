import numpy as np
from problem4a import riemann, trapezoid, simpson

def test_riemann():
    x = np.linspace(0,1,10)
    f = np.ones_like(x)
    I1 = riemann(f,x)
    print(I1)
    assert abs(I1-1.0)<1e-6

def test_trapezoid():
    x = np.linspace(0,1,10)
    f = np.ones_like(x)
    I1 = trapezoid(f,x)
    print(I1)
    assert abs(I1-1.0)<1e-6

def test_simpson1():
    x = np.linspace(0,1,10)
    f = np.ones_like(x)
    I1 = simpson(f,x)
    print(I1)
    assert abs(I1-1.0)<1e-6


def test_simpson2():
    x = np.linspace(0,1,11)
    f = np.ones_like(x)
    I1 = simpson(f,x)
    print(I1)
    assert abs(I1-1.0)<1e-6

def test_simpson3():
    x = np.linspace(0,np.pi/2,10)
    f = np.cos(x)
    I1 = simpson(f,x)
    print(I1)
    assert abs(I1-1.0)<1e-3

def test_simpson4():
    x = np.linspace(0,np.pi/2,11)
    f = np.cos(x)
    I1 = simpson(f,x)
    print(I1)
    assert abs(I1-1.0)<1e-3

def main():
    test_riemann()
    test_trapezoid()
    test_simpson1()
    test_simpson2()
    test_simpson3()
    test_simpson4()


if __name__ == "__main__":
    main()