import numpy as np
from numpy.linalg import norm
from inverse_matrix import swap_rows
from colors import bcolors
from matrix_utility import is_diagonally_dominant, DominantDiagonalFix, is_square_matrix

"""
Performs Jacobi iterations to solve the line system of equations, Ax=b, 
starting from an initial guess, ``x0``.

Terminates when the change in x is less than ``tol``, or
if ``N`` [default=200] iterations have been exceeded.

Receives 5 parameters:
    1.  a, the NxN matrix that method is being performed on.
    2.  b, vector of solution. 
    3.  X0,  the desired initial guess.
        if x is None, the initial guess will bw determined as a vector of 0's.
    4.  TOL, tolerance- the desired limitation of tolerance of solution's anomaly.
        if tolerance is None, the default value will set as 1e-16.
    5.  N, the maxim number of possible iterations to receive the most exact solution.
        if N is None, the default value will set as 200.

Returns variables:
    1.  x, the estimated solution

"""

def jacobi_iterative(A, b, X0, TOL=1e-16, N=200):
    n = len(A)
    for k in range(n):
        # Partial Pivoting: Find the pivot row with the largest absolute value in the current column
        pivot_row = k
        v_max = A[pivot_row][k]
        for i in range(k + 1, n):
            if abs(A[i][k]) > abs(v_max):
                v_max = A[i][k]
                pivot_row = i

        # if a principal diagonal element is zero,it denotes that matrix is singular,
        # and will lead to a division-by-zero later.
        if not A[pivot_row][k]:
            return k  # Matrix is singular

        # Swap the current row with the pivot row
        if pivot_row != k:
            swap_rows(A, k, pivot_row)
        # End Partial Pivoting
    if not is_diagonally_dominant(A):
        raise ValueError('Matrix is not diagonally dominant - Cant preform jacobi algorithm\n')

    print ('Matrix is  diagonally dominant - preforming jacobi algorithm\n')
    k = 1
    print( "Iteration" + "\t\t\t".join([" {:>12}".format(var) for var in ["x{}".format(i) for i in range(1, len(A) + 1)]]))
    print("-----------------------------------------------------------------------------------------------")

    while k <= N:
        x = np.zeros(n, dtype=np.double)
        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += A[i][j] * X0[j]
            x[i] = (b[i] - sigma) / A[i][i]

        print("{:<15} ".format(k) + "\t\t".join(["{:<15} ".format(val) for val in x]))

        if norm(x - X0, np.inf) < TOL:
            return tuple(x)

        k += 1
        X0 = x.copy()

    print("Maximum number of iterations exceeded")
    return tuple(x)


if __name__ == "__main__":

    A = np.array([[3, -1, 1],
                  [0, 2, -1],
                  [0, 1, -2]])

    b = np.array([4, -1, -3])

    x = np.zeros_like(b, dtype=np.double)
    solution = jacobi_iterative(A, b, x)

    print(bcolors.OKBLUE,"\nApproximate solution:", solution)