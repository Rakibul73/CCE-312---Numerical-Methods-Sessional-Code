# https://github.com/dmNadim/Numerical-Methods/blob/main/1.%20Roots%20of%20High-Degree%20Equations/3.%20Bisection%20Method.py

# def f(x):
#     return 2*x**2 - 5*x + 3   # Function from the given equation
f = lambda x: 2*x**2 - 5*x + 3

x1, x2 = map(float, input("Enter the initial interval (x1 x2): ").split())
# x1 = 0, 2         # The initial guesses
# x2 = 1.3


y1 = f(x1)
y2 = f(x2)

if y1*y2 > 0:       # Signs of y-values are not opposite 
    print("No roots exist within the given interval")
    raise SystemExit

if y1*y2 == 0:      # One or both initial guess is the root
    if y1 == 0: print('The root: %0.5f' % x1)
    if y2 == 0: print('The root: %0.5f' % x2)
    raise SystemExit

                    # Signs of y-values are opposite
xh = x1
while abs(x1-x2) >= 1.0E-6: # or abs(f(xh)) >= 1e-6:
    xh = (x1 + x2) / 2      # Bisection equation
    yh = f(xh)
    
    if y1 * yh < 0:         # The root is in the 1st half
        x2 = xh             # x1 and y1 remains same
        
    elif y1 * yh > 0:       # The root is in the 2nd half
        x1 = xh             # x2 remains same
        y1 = f(x1)          # y1 changes as x1 does

    else: break             # The root equals to xh

print('The Root: %0.5f' % xh)