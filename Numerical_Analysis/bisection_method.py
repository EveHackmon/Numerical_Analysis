import math
import numpy as np
import sympy as sp
from sympy import *
from sympy.utilities.lambdify import lambdify

def max_steps(a, b, err):
    s = int(np.floor(- np.log2(err / (b - a)) / np.log2(2) - 1))
    return s

def find_derivative(expression):
    x = sp.symbols('x')
    derivative = sp.diff(expression, x)
    print(derivative)
    return derivative

def bisection_method(f, a, b, tol):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("The scalars a and b do not bound a root")

    c, k = 0, 0
    steps = max_steps(a, b, tol)

    while abs(b - a) > tol and k < steps:
        c = a + (b - a) / 2
        if f(c) == 0:
            return c
        if f(a) == 0:
            return a
        if f(b) == 0:
            return b
        if np.sign(f(a)) == np.sign(f(c)):
            a = c
        else:
            b = c
        k += 1

    if f(c) > tol :
        raise Exception("The scalars a and b do not bound a root")
    return c

def find_all_roots(f, interval, tol):
    f1 = lambdify(x, f)
    a, b = interval
    roots = []
    interval1 = (b - a)/10
    while a <= b:
        flag = -1
        try:
            root = bisection_method(f1, a, a+interval1, tol)
            if root < a or root > b:  # Check if the root is outside the current interval
                continue

            if len(roots) == 0:
                roots.append(root)
            else:
                for i in roots:
                    if i == root:
                        flag = 0
                        break
                if flag == -1:
                    roots.append(root)
        except Exception as e:
            pass

        a += interval1
    return roots

if __name__ == '__main__':
    tol = 1e-6
    x = sp.symbols('x')

    f = (1*x**2 - 7*x + 3) / 6*x
    fTAG = sp.diff(f)

    interval = (0, 3)

    roots = find_all_roots(f, interval, tol)
    Extreme_Points = find_all_roots(fTAG, interval, tol)

    f1 = lambdify(x, f)
    for i in roots:
        try:
            x = f(i)
        except:
            roots.remove(i)

    moroots = []
    for i in Extreme_Points:
        if 0+tol >= f1(i) >= 0-tol:
            moroots.append(round(i, 5))

    for i in moroots:
        try:
            x = f(i)
        except:
            roots.remove(i)
            
    print("Intersection points from double multiplication", interval, "are:", roots)
    print("Intersection points from odd multiples are:", moroots)

