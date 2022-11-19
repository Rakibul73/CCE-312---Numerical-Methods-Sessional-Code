
from math import sin

f = lambda x: x**2 - sin(x)**2 - 4*x + 1 

x1, x2 = map(float, input("Enter the initial interval (x1 x2): ").split())


if f(x1)*f(x2) > 0:
    print("No roots exist within the given interval")
    raise SystemExit

if f(x1)*f(x2) == 0:
    if f(x1) == 0: print('The root: %0.5f' % x1)
    if f(x2) == 0: print('The root: %0.5f' % x2)
    raise SystemExit

xr = x1
while abs(f(xr)) >= 1e-6:
    xr = x2 - (x2-x1)/(f(x2)-f(x1))*f(x2)
    
    if f(x1) * f(xr) < 0:
        x2 = xr
        
    elif f(x1) * f(xr) > 0:
        x1 = xr

    else: break

print('The Root: %0.5f' % xr)