from math import sin, pi

f = lambda x: 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5
a = 0
b = 0.8

# f = lambda x: x*sin(x)  # Equation to be integrated
# a = 0                   # Lower limit
# b = pi/2                # Upper limit

n = 4                   # Number of divisions must be even
# n = 18                # More divisions give less error
h = (b - a) / n         # Width of each division

## xa = a, xb = b, x1 = a+h, x2 = a+2*h
## I = 1/3 h[{f(a)+f(b)} + 4{f(a+h) + f(a+3*h)+...+f(a+[n-3]*h)+f(a+[n-1]*h)}
##                       + 2{f(a+2*h)+f(a+4*h)+...+f(a+[n-4]*h)+f(a+[n-2]*h)}]
## I = 1/3*h[{f(a)+f(b)} + 4*f(a + i*h) + 2*f(a + i2*h)]
## where i = 1, 3, 5 to n-1 and i2 = 2, 4, 6 to n-2

S = (f(a) + f(b))
for i in range(1, n, 2):
    S += 4 * f(a + i*h)
for i in range(2, n, 2):
    S += 2 * f(a + i*h)
I = 1/3 * h * S

print("Integral of the equation, I = %f" % I)


'''
Area under the curve is sliced into even number of strips having equal width, h
Consecutive three f(x) points can be connected with a 2nd order polynomial
The area of the first two strips, A = 1/3 h {f(x0) + 4f(x1) + f(x2)}

The sum of the areas of slices can be written as
I = 1/3 h{f(x0) + 4f(x1) + f(x2)} + 1/3 h{f(x2) + 4f(x3) + f(x4)} + ... + 
    1/3 h{f(x[n-4])+4f(x[n-3])+f(x[n-2]))} + 1/3 h{f(x[n-2])+4f(x[n-1])+f(xn)}

I = 1/3 h[{f(x0)+f(xn)} + 4{f(x1) + f(x3) + ... + f(x[n-3]) + f(x[n-1])}
                        + 2{f(x2) + f(x4) + ... + f(x[n-4]) + f(x[n-2])}]
I = 1/3 h[{f(xa)+f(xb)} + 4{f(x1) + f(x3) + ... + f(x[n-3]) + f(x[n-1])}
                        + 2{f(x2) + f(x4) + ... + f(x[n-4]) + f(x[n-2])}]
'''