import numpy as np

def f(x, y):
    return -2 * x * y

# 4-stage Runge-Kutta method for initial steps
def runge_kutta4(f, x0, y0, h, steps):
    x = x0
    y = y0
    results = [(x, y)]
    for _ in range(steps):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h
        results.append((x, y))
    return results

# Adams Method for Bashforth and Moulton
def adams_method(f, x0, y0, h, x_end):
    # Get first 3 values using Runge-Kutta 4th order
    initial_values = runge_kutta4(f, x0, y0, h, 3)
    
    # Extract x and y lists
    x_vals = [p[0] for p in initial_values]
    y_vals = [p[1] for p in initial_values]
    
    while x_vals[-1] + h <= x_end:
        x = x_vals[-1]
        
        # Compute f_n values
        fn = [f(x_vals[i], y_vals[i]) for i in range(len(y_vals))]

        # Predictor: Adams-Bashforth 4-step
        y_predict = y_vals[-1] + (h / 24) * (55 * fn[-1] - 59 * fn[-2] + 37 * fn[-3] - 9 * fn[-4])

        # Compute f_{n+3} using the predicted value
        f_predict = f(x + h, y_predict)

        # Corrector: Adams-Moulton 4-step
        y_correct = y_vals[-2] + (h / 24) * (9 * f_predict + 19 * fn[-1] - 5 * fn[-2] + fn[-3])

        # Update lists
        x_vals.append(x + h)
        y_vals.append(y_correct)

    return x_vals, y_vals

# Solve for h = 0.001
h1 = 0.001
x_vals_1, y_vals_1 = adams_method(f, 0, 1, h1, 1.0)

# Solve for h = 0.0001
h2 = 0.0001
x_vals_2, y_vals_2 = adams_method(f, 0, 1, h2, 1.0)

# Display results
print(f"Solution with h={h1} at x=1.0: y={y_vals_1[-1]}")
print(f"Solution with h={h2} at x=1.0: y={y_vals_2[-1]}")
