from math import sin, pi

f = lambda x: 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5
a = 0
b = 0.8
e = 1.640533

n = 1 
h = (b - a) / n         

S = 0.5 * (f(a) + f(b))
print(S)
for i in range(1, n):
    S += f(a + i*h)
I = h * S

print("Integral of the equation, I = %f" % I)

error = abs(e - I)
print("Error =", error)

print("Percent error =" , (error*100) / e , "%")

