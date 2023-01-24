from math import sin, pi

f = lambda x: 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5
a = 0
b = 0.8
e = 1.640533


h = (b - a) / 3
I = (b-a) * (( f(a)    +  (3*f(h) )  + (3*f(h+h)   )     + f(b)  ) / 8.0)

# n = 3
# h = (b - a) / n


# S = (f(a) + f(b))
# for i in range(1, n, 3):                        # 1<=i<n : 1, 4, 7, n-5, n-2
#     S += 3 *(f(a + i*h) + f(a + (i+1)*h))
# for i in range(3, n, 3):                        # 3<=i<n : 3, 6, 9, n-6, n-3
#     S += 2 * f(a + i*h)
# I = 3/8 * h * S

print("Integral of the equation, I = %f" % I)

error = abs(e - I)
print("Error =", error)

print("Percent error =" , (error*100) / e , "%")