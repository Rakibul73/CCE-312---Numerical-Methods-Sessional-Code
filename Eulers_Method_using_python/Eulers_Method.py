# https://github.com/dmNadim/Numerical-Methods/blob/main/6.%20Ordinary%20Differential%20Equations/1.%20Euler's%20Method.py

from math import exp
f = lambda x: exp(x**2/2)   # Analytical Solution

dy = lambda x, y: x*y   # Equation to be solved, y' = xy
x = 0                   # Lower limit, [0
xn = 2                  # Upper limit, 2]
y = 1                   # Initial condition, y(0) = 1

h = 0.5                 # Width of each division, step size
# h = 0.1               # Smaller step size gives less error
n = int((xn-x)/h)       # Number of divisions of the domain


print('x \t\ty(Euler) \ty(Analytical)') # Header of Output
print('%f \t%f \t%f' % (x, y, f(x)))    # Initial x and y

for i in range(n):
    y += dy(x,y)*h      # y for next step, y(x+h) = y(x) + y'(x)h
    x += h              # x for next step, x = x + h
    print('%f \t%f \t%f' % (x, y, f(x)))


"""
Taylor's series can be written as
y(x+h) = y(x) + y'(x)h + y''(x)/2! h^2 + y'''(x)/3! h^3 + ...

Approximate solution of Euler's method is obtained by
trancating the series at the first derivative term
y(x+h) = y(x) + y'(x)h

The initial condition is the value of y(x) at initial domain x

Find the numerical solution of the following differential equation
over the domain [0,2]: y' = xy,       y(0) = 1

Analytical Solution: y = e^(x^2/2)

"""