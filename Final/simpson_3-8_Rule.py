import sympy as sy

f = lambda x: 2000.0*sy.log(140000.0/ (140000.0  -  (2100.0*x))   ) - 9.8*x
a = 8
b = 30
# e = 1.640533

# jodi exact value e = 1.640533 deya na thake.. kintu error bair korte koy taile
x = sy.Symbol("x")
e = sy.integrate(f(x), (x, a, b))
print("Exact value = " , e)


h = (b - a) / 3
I = (b-a) * (( f(a)    +  (3*f(a + h) )  + (3*f(a + h+h)   )     + f(b)  ) / 8.0)

# n = 3
# h = (b - a) / n


# S = (f(a) + f(b))
# for i in range(1, n, 3):                       
#     S += 3 *(f(a + i*h) + f(a + (i+1)*h))
# for i in range(3, n, 3):                       
#     S += 2 * f(a + i*h)
# I = 3/8 * h * S

print("Integral of the equation, I = %f" % I)

error = abs(e - I)
print("Error =", error)

print("Percent error =" , (error*100) / e , "%")