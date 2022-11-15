from math import sin, pi

f = lambda x: 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5
a = 0
b = 0.8
e = 1.640533

n = 4
h = (b - a) / n


S = (f(a) + f(b))
for i in range(1, n, 2):
    S += 4 * f(a + i*h)
for i in range(2, n, 2):
    S += 2 * f(a + i*h)
I = 1/3 * h * S

print("Integral of the equation, I = %f" % I)

error = abs(e - I)
print("Error =", error)

print("Percent error =" , (error*100) / e , "%")