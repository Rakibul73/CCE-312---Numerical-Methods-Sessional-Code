
from math import sin

f = lambda x: 2*x**2 - 5*x + 3

a, b = map(float, input("Enter the initial interval (a b): ").split())


if f(a)*f(b) > 0:
    print("No roots exist within the given interval")
    exit()

if f(a)*f(b) == 0:
    if f(a) == 0: print('The root: %0.5f' % a)
    elif f(b) == 0: print('The root: %0.5f' % b)
    exit()

c = a
while abs(f(c)) >= 1e-6:
    c = (a*f(b) - b*f(a)) / (f(b) - f(a))
    # c = (a + b) / 2
    # yh = f(c)

    if f(a) * f(c) < 0:
        b = c
        
    elif f(a) * f(c) > 0:
        a = c

    else: break

print('The Root: %0.5f' % c)