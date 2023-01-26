import sympy as sy

f = lambda x: 2000.0*sy.log(140000.0/ (140000.0  -  (2100.0*x))   ) - 9.8*x
a = 8
b = 30
# e = 1.640533

# jodi exact value e = 1.640533 deya na thake.. kintu error bair korte koy taile
x = sy.Symbol("x")
e = sy.integrate(f(x), (x, a, b))
print(e)

n = 2
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

