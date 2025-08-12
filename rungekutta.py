def runge_kutta_4(f, x0, y0, x_end, h):
    xs, ys = [x0], [y0]
    x, y = x0, y0
    while x < x_end:
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        x += h
        xs.append(x)
        ys.append(y)
    return xs, ys

def dydx(x, y):
    return x + y

x_vals, y_vals = runge_kutta_4(dydx, 0, 1, 2, 0.1)
for x, y in zip(x_vals, y_vals):
    print(f"x={x:.2f}, y={y:.4f}")
