from colors import bcolors

def lagrange_interpolation(x_data, y_data, x):
    """
    Lagrange Interpolation

    Parameters:
    x_data (list): List of x-values for data points.
    y_data (list): List of y-values for data points.
    x (float): The x-value where you want to evaluate the interpolated polynomial.

    Returns:
    float: The interpolated y-value at the given x.
    """
    n = len(x_data)
    result = 0.0

    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term
    return result

if __name__ == '__main__':
    x_data = [1.2, 1.3, 1.4, 1.5, 1.6]
    y_data = [1.5095, 1.6984, 1.9043, 2.1293, 2.3756]
    x1_interpolate = 1.47  # The x-value where you want to interpolate
    x2_interpolate = 1.67

    print(" Date: 08/04/2024\n"
          " Group: Daniel Houri , 209445071 \n"
          "        Yakov Shtefan , 208060111 \n"
          "        Vladislav Rabinovich , 323602383 \n"
          " Git: https://github.com/EveHackmon/Numerical_Analysis.git \n"
          " Name: Eve Hackmon , 209295914 \n"
          " Input:\n")
    print("x_data", x_data)
    print("y_data", y_data)
    y1_interpolate = round(lagrange_interpolation(x_data, y_data, x1_interpolate), 1)
    print(bcolors.OKBLUE, "Interpolated value at x =", x1_interpolate, "is y =", y1_interpolate, bcolors.ENDC)
    y2_interpolate = round(lagrange_interpolation(x_data, y_data, x2_interpolate), 1)
    print(bcolors.OKBLUE, "Interpolated value at x =", x2_interpolate, "is y =", y2_interpolate, bcolors.ENDC)