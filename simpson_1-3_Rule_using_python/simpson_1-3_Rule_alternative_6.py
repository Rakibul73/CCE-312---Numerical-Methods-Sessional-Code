def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5

a= input ("the lower limit, upper limit, subinterval number:  ")
b= input ("the lower limit, upper limit, subinterval number:  ")
n= input ("the lower limit, upper limit, subinterval number:  ")
h= float (b-a)/n
sum = f(a)+f(b) 
d=4

for k in range(1,n-1):
    x= a+k*h
    sum= sum+ d*f(x)
    d= 6-d

sum= h/3*sum
print ("value of the integral= ", sum)