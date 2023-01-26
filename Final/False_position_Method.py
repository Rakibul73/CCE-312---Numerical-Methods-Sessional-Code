

f = lambda x: x**3 - 0.165*x**2 + 3.993*10**-4

a, b = map(float, input("Enter the initial interval (a b): ").split())


if f(a)*f(b) > 0:
    print("No roots exist within the given interval")
    exit()

if f(a)*f(b) == 0:
    if f(a) == 0: print('The root: %0.4f' % a)
    elif f(b) == 0: print('The root: %0.4f' % b)
    exit()

c = a
while abs(f(c)) >= 1e-6:
    # temp = c
    c = (a*f(b) - b*f(a)) / (f(b) - f(a))

    if f(a) * f(c) < 0:
        b = c
        
    elif f(a) * f(c) > 0:
        a = c
    
    else: break
    # pp = (abs(c - temp) / c)*100
    # print("%0.4f" % pp , "%\t", "%0.4f" %a , "\t", "%0.4f" %b, "\t", "%0.4f" %c)

print('The Root: %0.4f' % c)