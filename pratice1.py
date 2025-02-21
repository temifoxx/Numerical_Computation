# This is the question # 

import numpy as np
from tabulate import tabulate

# Exact solution
def exact_solution(x):
    return np.exp(x**3)

# Differential equation
def f(x, y):
    return 3 * x**2 * y

# Predictor-corrector method
def predictor_corrector(h, x0, y0, n):
    # Initialize arrays
    x = np.zeros(n+3)
    y = np.zeros(n+3)
    y_pred = np.zeros(n+3)
    
    # Initial conditions
    x[0], y[0] = x0, y0
    
    # Compute y1 and y2 using the exact solution
    for i in range(1, 3):
        x[i] = x[i-1] + h
        y[i] = exact_solution(x[i])
    
    # Predictor-corrector steps
    for i in range(2, n+2):
        x[i+1] = x[i] + h
        
        # Predictor step
        y_pred[i+1] = y[i] + h/12 * (23*f(x[i], y[i]) - 16*f(x[i-1], y[i-1]) + 5*f(x[i-2], y[i-2]))
        
        # Corrector step
        y[i+1] = y[i] + h/24 * (9*f(x[i+1], y_pred[i+1]) + 19*f(x[i], y[i]) - 5*f(x[i-1], y[i-1]) + f(x[i-2], y[i-2]))
    
    return x, y

# Euler's method
def euler_method(h, x0, y0, n):
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    
    # Initial conditions
    x[0], y[0] = x0, y0
    
    # Euler steps
    for i in range(n):
        x[i+1] = x[i] + h
        y[i+1] = y[i] + h * f(x[i], y[i])
    
    return x, y

# Parameters
x0, y0 = 0, 1  # Initial condition
h = 0.1        # Step size
n = 10         # Number of steps

# Compute solutions
x_pc, y_pc = predictor_corrector(h, x0, y0, n)
x_euler, y_euler = euler_method(h, x0, y0, n)

# Exact solution at the same points
y_exact = exact_solution(x_pc)

# Compute absolute errors
error_pc = np.abs(y_pc - y_exact)
error_euler = np.abs(y_euler - exact_solution(x_euler))

# Prepare data for tabulate
pc_table = []
euler_table = []

for i in range(len(x_pc)):
    pc_table.append([x_pc[i], y_pc[i], y_exact[i], error_pc[i]])

for i in range(len(x_euler)):
    euler_table.append([x_euler[i], y_euler[i], exact_solution(x_euler[i]), error_euler[i]])

# Print results using tabulate
print("Predictor-Corrector Method:")
print(tabulate(pc_table, headers=["x", "y (PC)", "y (Exact)", "Error (PC)"], tablefmt="pretty", floatfmt=".6f"))

print("\nEuler's Method:")
print(tabulate(euler_table, headers=["x", "y (Euler)", "y (Exact)", "Error (Euler)"], tablefmt="pretty", floatfmt=".6f"))