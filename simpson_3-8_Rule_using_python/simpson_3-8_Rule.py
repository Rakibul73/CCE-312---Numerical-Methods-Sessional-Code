from math import sin, pi

# f = lambda x: 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5
# a = 0
# b = 0.8

f = lambda x: x*sin(x)  # Equation to be integrated
a = 0                   # Lower limit
b = pi/2                # Upper limit

n = 6                   # Number of divisions must be multiple of 3
# n = 18                # More divisions give less error
h = (b - a) / n         # Width of each division

## xa = a, xb = b, x1 = a+h, x2 = a+2*h
## I = 3/8 h [{f(a)+f(b)}
##     + 3 {f(a+h) + f(a+2h) + f(a+4h) + f(a+5h) + ... + f(a+[n-2]h)
##     + f(a+[n-1]h)}     + 2 {f(a+3h) + f(a+6h) + ... + f(a+[n-3]h)}]
## I = 3/8*h*[{f(a)+f(b)} + 3*{f(a+i*h)+ f(a+(i+1)*h)} + 2*f(a+i2*h)]
## where i = 1, 4, 7 to n-2 and i2 = 3, 6, 9 to n-3

S = (f(a) + f(b))
for i in range(1, n, 3):                        # 1<=i<n : 1, 4, 7, n-5, n-2
    S += 3 *(f(a + i*h) + f(a + (i+1)*h))
for i in range(3, n, 3):                        # 3<=i<n : 3, 6, 9, n-6, n-3
    S += 2 * f(a + i*h)
I = 3/8 * h * S

print("Integral of the equation, I = %f" % I)


'''
Area under the curve is sliced into multiple of 3 strips having equal width, h
Consecutive four f(x) points can be connected with a 3rd order polynomial
The area of the first three strips, A = 3/8 h {f(x0) + 3f(x1) + 3f(x2) + f(x3)}

The sum of the areas of slices can be written as
I = 3/8 h {f(x0)+3f(x1)+3f(x2)+f(x3)} + 3/8 h {f(x3)+3f(x4)+3f(x5)+f(x6)}
            + ... + 3/8 h {f(x[n-3]) + 3f(x[n-2]) + 3f(x[n-1]) + f(xn)}

I = 3/8 h [{f(x0)+f(xn)}
            + 3{f(x1) + f(x2) + f(x4) + f(x5) + ... + f(x[n-2]) + f(x[n-1])}
            + 2{f(x3) + f(x6) + ... + f(x[n-3])}]
I = 3/8 h [{f(xa)+f(xb)}
            + 3{f(x1) + f(x2) + f(x4) + f(x5) + ... + f(x[n-2]) + f(x[n-1])}
            + 2{f(x3) + f(x6) + ... + f(x[n-3])}]

Et = exact integral - numerical integral
εt = (Et / exact integral) * 100%
εt(Simpson's 1/3 rule) < εt(Simpson's 3/8 rule) < εt(Trapezoidal rule)

'''