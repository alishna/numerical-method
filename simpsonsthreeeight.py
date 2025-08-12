import numpy as np

def func(x):
    return (1/(1+x))

n = 12

a = 0
b = 1
x = np.linspace(a, b, n+1)
y = np.zeros(n+1)
for i in range(n+1):
    y[i] = func(x[i])

I1 = y[0] + y[n]
I2 = 0
I3 = 0

for i in range (1,n-1,3):
    I3=I3+y[i]+y[i+1]
for i in range(3,n-2,3):
    I2=I2+y[i]

h=(b-a)/n
I = (3 * h / 8) * (I1 + 2 * I2 + 3* I3)
print("The value is:", I)