# Predictor-Corrector Method (Adams-Bashforth & Adams-Moulton)
def predictor_corrector(f, x0, y0, h, x_end):
    """
    Parameters:
    f      - Function f(x, y) representing dy/dx.
    x0     - Initial value of x.
    y0     - Initial value of y.
    h      - Step size.
    x_end  - Final value of x.

    """
    
    # number of steps
    n = int((x_end - x0) / h)
    
    #stores values of x0 as it increases
    x_values = [x0]
    y_values = [y0]

    # Using Euler's method to compute the following value (y1) as step size increases.
    x1 = x0 + h
    y1 = y0 + h * f(x0, y0)  

    # Store these values
    x_values.append(x1)
    y_values.append(y1)

    # Predictor-Corrector method
    for i in range(1, n): 
        x_next = x_values[i] + h 

        # Predictor step: Adams-Bashforth 2-Step
        y_pred = y_values[i] + (h / 2) * (3 * f (x_values[i], y_values[i]) - f(x_values[i-1], y_values[i-1]))

        # Corrector step: Adams-Moulton 2-Step
        y_corr = y_values[i] + (h / 12) * (5 * f(x_next, y_pred) + 8 * f(x_values[i], y_values[i]) - f(x_values[i-1], y_values[i-1]))

        # Store computed values
        x_values.append(x_next)
        y_values.append(y_corr)

    return x_values, y_values

# For dy/dx = -y
def f1(x, y):
    return -y

# For dy/dx = -x(y + y^2)
def f2(x, y):
    return -x * (y + y**2)

# Initial conditions
x0 = 0   
y0 = 1   
h = 0.001
x_end = 1

# For equation: y' = -y
x_values1, y_values1 = predictor_corrector(f1, x0, y0, h, x_end)

# For equation: y' = -x(y + y^2)
x_values2, y_values2 = predictor_corrector(f2, x0, y0, h, x_end)

# Print results for the equation: y' = -y
print("\nSolution for y' = -y using Predictor-Corrector Method")
print("=" * 50)
print(f"{'x':<10}{'y (Pred-Corr)'}")
print("-" * 50)
for i in range(0, len(x_values1), 100):  # Print every 100th step
    print(f"{x_values1[i]:<10.3f}{y_values1[i]:.6f}")
print("=" * 50)

# Print results for the equation: y' = -x(y + y^2)
print("\nSolution for y' = -x(y + y^2) using Predictor-Corrector Method")
print("=" * 50)
print(f"{'x':<10}{'y (Pred-Corr)'}")
print("-" * 50)
for i in range(0, len(x_values2), 100):  # Print every 100th step
    print(f"{x_values2[i]:<10.3f}{y_values2[i]:.6f}")
print("=" * 50)
