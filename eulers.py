def backward_euler(x0, y0, xn, n, f):
    x = x0
    y = y0  
    h = (xn-x0)/n
    x_values=[x0]
    y_values=[y0]
    for i in range(n+1):
        y1 = y + h * (f(x, y))
        y = y + h * (f(x + h, y1))
        x += h
        x_values.append(x)
        y_values.append(y)
    return x_values, y_values

x_result,y_result = backward_euler(0,1,1,20,lambda x, y: (y**2 - x**2)/(y**2 + x**2))

print('x \t y')
for x,y in zip(x_result, y_result):
    print(f'{x:.2f} \t {y:.2f}')


def modified_euler(x0, y0, xn, n, f):
    x = x0
    y = y0
    h = (xn - x0) / n
    x_values = [x0]
    y_values = [y0]
    
    for i in range(n):
        # Predictor
        y1 = y + h * f(x, y)
        # Corrector
        y = y + (h / 2) * (f(x, y) + f(x + h, y1))
        x += h
        x_values.append(x)
        y_values.append(y)
        
    return x_values, y_values

x_modified, y_modified = modified_euler(0, 1, 1, 20, lambda x, y: (y**2 - x**2)/(y**2 + x**2))

print('x \t y')
for x, y in zip(x_modified, y_modified):
    print(f'{x:.2f} \t {y:.4f}')

from matplotlib import pyplot as plt
plt.plot(x_modified, y_modified, label='Modified Euler Method', color='orange')
plt.plot(x_result, y_result, label='Backward Euler Method')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
