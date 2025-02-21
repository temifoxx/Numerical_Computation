import numpy as np

# Differential equation
def f(x, y):
    return 3 * x**2 * y

# Exact solution
def exact_solution(x):
    return np.exp(x**3)

# ==================================================
# Question 1a: 4-stage Runge-Kutta Method
# ==================================================
def runge_kutta_4th_order(h, x0, y0, n):
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    
    # Initial conditions
    x[0], y[0] = x0, y0
    
    # Runge-Kutta steps
    for i in range(n):
        x[i+1] = x[i] + h
        
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h/2, y[i] + h/2 * k1)
        k3 = f(x[i] + h/2, y[i] + h/2 * k2)
        k4 = f(x[i] + h, y[i] + h * k3)
        
        y[i+1] = y[i] + h/6 * (k1 + 2*k2 + 2*k3 + k4)
    
    return x, y

# ==================================================
# Question 1b: Predictor-Corrector Method
# ==================================================
def predictor_corrector(h, x0, y0, n, y_rk):
    x = np.zeros(n+2)
    y = np.zeros(n+2)
    
    # Initial conditions (use Runge-Kutta results for y1 and y2)
    x[0], y[0] = x0, y0
    x[1], y[1] = x0 + h, y_rk[1]
    
    # Predictor-corrector steps
    for i in range(1, n+1):
        x[i+1] = x[i] + h
        
        # Predictor step
        y_pred = y[i] + h/3 * (3*f(x[i], y[i]) - f(x[i-1], y[i-1]))
        
        # Corrector step
        y[i+1] = y[i] + h/12 * (5*f(x[i+1], y_pred) + 8*f(x[i], y[i]) - f(x[i-1], y[i-1]))
    
    return x, y

# ==================================================
# Question 1c: Compare with Theoretical Solution
# ==================================================
def compare_with_exact(x_pc, y_pc):
    # Compute exact solution and errors
    y_exact = exact_solution(x_pc)
    error_pc = np.abs(y_pc - y_exact)
    
    # Print comparison
    print("\nComparison with Theoretical Solution:")
    print("x\t\ty (PC)\t\ty (Exact)\tError (PC)")
    for i in range(len(x_pc)):
        print(f"{x_pc[i]:.2f}\t\t{y_pc[i]:.6f}\t{exact_solution(x_pc[i]):.6f}\t{error_pc[i]:.6f}")

# ==================================================
# Main Program
# ==================================================
# Parameters
x0, y0 = 0, 1  # Initial condition
h = 0.1        # Step size
n = 10         # Number of steps (to cover x = 0 to 1)

# Step 1: Compute Runge-Kutta solution (Question 1a)
x_rk, y_rk = runge_kutta_4th_order(h, x0, y0, n)

# Print Runge-Kutta results
print("Runge-Kutta 4th Order Method (Question 1a):")
print("x\t\ty (RK4)")
for i in range(len(x_rk)):
    print(f"{x_rk[i]:.2f}\t\t{y_rk[i]:.6f}")

# Step 2: Compute Predictor-Corrector solution (Question 1b)
x_pc, y_pc = predictor_corrector(h, x0, y0, n, y_rk)

# Print Predictor-Corrector results
print("\nPredictor-Corrector Method (Question 1b):")
print("x\t\ty (PC)")
for i in range(len(x_pc)):
    print(f"{x_pc[i]:.2f}\t\t{y_pc[i]:.6f}")

# Step 3: Compare with theoretical solution (Question 1c)
compare_with_exact(x_pc, y_pc)