# https://github.com/dmNadim/Numerical-Methods/blob/main/1.%20Roots%20of%20High-Degree%20Equations/4.%20False%20Position%20or%20Regula%20Falsi%20Method.py

from math import sin

f = lambda x: x**2 - sin(x)**2 - 4*x + 1    # Function from the given equation

x1, x2 = map(float, input("Enter the initial interval (x1 x2): ").split())
# x1 = 0, 4             # The initial guesses   # x1 ≠ x2
# x2 = 1.3


if f(x1)*f(x2) > 0:     # Signs of f(x)-values are not opposite 
    print("No roots exist within the given interval")
    raise SystemExit

if f(x1)*f(x2) == 0:    # One or both initial guess is the root
    if f(x1) == 0: print('The root: %0.5f' % x1)
    if f(x2) == 0: print('The root: %0.5f' % x2)
    raise SystemExit

                        # Signs of f(x)-values are opposite
xr = x1
while abs(f(xr)) >= 1e-6:
    ## x2-x1 / f(x2)-f(x1) = x2-xr / f(x2)-0 = x1-xr / f(x1)-0
    # xr = (f(x2)*x1 - f(x1)*x2) / (f(x2) - f(x1))
    xr = x2 - (x2-x1)/(f(x2)-f(x1))*f(x2)   # False Position equation
    
    if f(x1) * f(xr) < 0:       # The root is in the 1st half
        x2 = xr
        
    elif f(x1) * f(xr) > 0:     # The root is in the 2nd half
        x1 = xr

    else: break                 # The root equals to xh

print('The Root: %0.5f' % xr)