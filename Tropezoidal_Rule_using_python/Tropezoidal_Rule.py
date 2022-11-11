from math import sin, pi

f = lambda x: 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5
a = 0
b = 0.8

# f = lambda x: x*sin(x)  # Equation to be integrated
# a = 0                   # Lower limit
# b = pi/2                # Upper limit

n = 1                  # Number of divisions
# n = 100               # More divisions give less error
h = (b - a) / n         # Width of each division

## xa = a, xb = b, x1 = a+h, x2 = a+2*h
## I = h {0.5[f(a)+f(b)] + f(a+h) + f(a+2*h) +...+ f(a+[n-2]*h) + f(a+[n-1]*h)}
## I = h {0.5[f(a)+f(b)] + f(a + i*h)}    where i = 1 to n-1

S = 0.5 * (f(a) + f(b))
for i in range(1, n):
    S += f(a + i*h)
I = h * S

print("Integral of the equation, I = %f" % I)


'''
Area under the curve is divided into vertical trapezoids having equal width, h
The area of the first trapezoid, A = h{f(x0)+f(x1)}/2

The sum of the areas of trapezoids can be written as
I = h/2 {f(x0) + f(x1)} + h/2 {f(x1) + f(x2)} + ...
  + h/2 {f(x[n-2])+f(x[n-1])} + h/2{f(x[n-1])+f(xn)}

I = h {1/2[f(x0)+f(xn)] + f(x1) + f(x2) + ... + f(x[n-2]) + f(x[n-1])}
I = h {1/2[f(xa)+f(xb)] + f(x1) + f(x2) + ... + f(x[n-2]) + f(x[n-1])}

'''