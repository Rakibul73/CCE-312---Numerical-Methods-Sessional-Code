
f = lambda x: 2*x**2 - 5*x + 3

x1, x2 = map(float, input("Enter the initial interval (x1 x2): ").split())


y1 = f(x1)
y2 = f(x2)

if y1*y2 > 0:
    print("No roots exist within the given interval")
    raise SystemExit

if y1*y2 == 0:
    if y1 == 0: print('The root: %0.5f' % x1)
    if y2 == 0: print('The root: %0.5f' % x2)
    raise SystemExit


xh = x1
while abs(x1-x2) >= 1.0E-6:
    xh = (x1 + x2) / 2
    yh = f(xh)
    
    if y1 * yh < 0:
        x2 = xh
        
    elif y1 * yh > 0:
        x1 = xh
        y1 = f(x1)

    else: break

print('The Root: %0.5f' % xh)