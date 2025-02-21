import numpy as np

# Differential equation
def f(x, y):
    return -2 * x * y

# Theoretical solution
def exact_solution(x):
    return np.exp(-x**2)

# Predictor-corrector method using Adams pair
def adams_predictor_corrector(h, x0, y0, x_end):
    # Number of steps
    n = int((x_end - x0) / h)
    
    # Initialize arrays
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    
    # Initial conditions
    x[0], y[0] = x0, y0
    
    # Use Runge-Kutta 4th order to compute initial values (y1, y2, y3)
    for i in range(1, 4):
        x[i] = x[i-1] + h
        k1 = f(x[i-1], y[i-1])
        k2 = f(x[i-1] + h/2, y[i-1] + h/2 * k1)
        k3 = f(x[i-1] + h/2, y[i-1] + h/2 * k2)
        k4 = f(x[i-1] + h, y[i-1] + h * k3)
        y[i] = y[i-1] + h/6 * (k1 + 2*k2 + 2*k3 + k4)
    
    # Predictor-corrector steps
    for i in range(3, n):
        x[i+1] = x[i] + h
        
        # Predictor step
        y_pred = y[i] + h/24 * (55*f(x[i], y[i]) - 59*f(x[i-1], y[i-1]) + 37*f(x[i-2], y[i-2]) - 9*f(x[i-3], y[i-3]))
        
        # Corrector step
        y[i+1] = y[i] + h/24 * (9*f(x[i+1], y_pred) + 19*f(x[i], y[i]) - 5*f(x[i-1], y[i-1]) + f(x[i-2], y[i-2]))
    
    return x, y

# Parameters
x0, y0 = 0, 1  # Initial condition
x_end = 1.0    # End of interval
h_values = [0.001, 0.0001]  # Step sizes

# Solve for each step size
for h in h_values:
    print(f"\nStep size h = {h}")
    x, y = adams_predictor_corrector(h, x0, y0, x_end)
    
    # Compare with theoretical solution
    y_exact = exact_solution(x)
    error = np.abs(y - y_exact)
    
    # Print results
    print("x\t\ty (Numerical)\ty (Exact)\tError")
    for i in range(0, len(x), 100):  # Print every 100th step for brevity
        print(f"{x[i]:.6f}\t{y[i]:.6f}\t{y_exact[i]:.6f}\t{error[i]:.6f}")