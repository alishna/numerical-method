def f(x):
    return x**3 - 4*x-9
a=0
b=1
tol=10**-3
c=0

while f(a)*f(b) >=0:
    b=b+1

while abs(b-a) >= tol:
    c=(a+b)/2
    if f(c) == 0:
        break
    elif f(c)*f(a) < 0:
        b=c
    else:
        a=c
print(c)