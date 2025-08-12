def simpsons_one_third(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's 1/3 rule")
    
    h = (b - a) / n
    result = f(a) + f(b)
    
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            result += 2 * f(x)
        else:
            result += 4 * f(x)
    
    return (h / 3) * result

def func(x):
    return x**3 + x**2 + 1

integral = simpsons_one_third(func, 0, 1, 10)  # n must be even
print(f"Approximate integral: {integral:.6f}")
