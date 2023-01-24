
from math import exp
f = lambda x: -(x**4)/2 + 4*x**3 - 10*x**2 + 8.5*x + 1

dy = lambda x: -(2*x**3) + 12*x*x - 20*x + 8.5 
x = 0                   
xn = 4                  
y = 1                   

h = 0.5                 
n = int((xn-x)/h)       


print('x \t\ty(Euler) \ty(Analytical)') 
print('%f \t%f \t%f' % (x, y, f(x)))    

for i in range(n):
    y += dy(x)*h      
    x += h              
    print('%f \t%f \t%f' % (x, y, f(x)))
