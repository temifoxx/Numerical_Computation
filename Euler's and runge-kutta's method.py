def f(x, y):
    return x + y  

# Euler's Method
def euler_method(f, x0, y0, h, n):
    x = x0
    y = y0
    results = [(x0, y0)]

    for _ in range(n):
        y_new = y + h * f(x, y)
        x_new = x + h
        results.append((x_new, y_new))
        x, y = x_new, y_new

    return results

# Runge-Kutta 4th Order Method
def runge_kutta_method(f, x0, y0, h, n):
    x = x0
    y = y0
    results = [(x0, y0)]

    for _ in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)

        y_new = y + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
        x_new = x + h
        results.append((x_new, y_new))
        x, y = x_new, y_new

    return results

# Parameters
x0 = 0     
y0 = 1     
h = 0.1    
n = 10     

# Compute solutions
euler_results = euler_method(f, x0, y0, h, n)
rk4_results = runge_kutta_method(f, x0, y0, h, n)

# Print tabulated results
print("\nComparison of Euler's Method and Runge-Kutta 4th Order Method")
print("=" * 55)
print(f"{'x':<10}{'Euler y':<15}{'Runge-Kutta y'}")
print("-" * 55)

for i in range(len(euler_results)):
    x_val = euler_results[i][0]
    y_euler = euler_results[i][1]
    y_rk4 = rk4_results[i][1]
    print(f"{x_val:<10.2f}{y_euler:<15.6f}{y_rk4:.6f}")

print("=" * 55)
