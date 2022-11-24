
from math import exp
f = lambda x: exp(x**2/2)   

dy = lambda x, y: x*y   
x = 0                   
xn = 2                  
y = 1                   

h = 0.5                 
n = int((xn-x)/h)       


print('x \t\ty(Euler) \ty(Analytical)') 
print('%f \t%f \t%f' % (x, y, f(x)))    

for i in range(n):
    y += dy(x,y)*h      
    x += h              
    print('%f \t%f \t%f' % (x, y, f(x)))
