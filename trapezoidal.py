def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    return result * h

# Example usage:
def func(x):
    return x**2  

approx_integral = trapezoidal_rule(func, 0, 1, 10)
print(f"Approximate integral: {approx_integral:.6f}")
