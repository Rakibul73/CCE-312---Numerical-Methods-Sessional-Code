# https://github.com/0xtejas/Python-Numerical-Integration-Definite

def get_values():
    try:
        global L, LimitN, Limit0, h,constant,n
        coefficient = str(input("Enter the co-efficient of the integrand F(x): "))
        Limit0 = int(input("Enter the Lower Limit: "))
        LimitN = int(input("Enter the Upper Limit: "))
        h = float(input("Enter the value of h: "))
        L = coefficient.split()
        constant = int(input("Enter Constant: "))
        n = (LimitN - Limit0)/h
    except Exception as e:
        print("Oops! Value Error Occurred.")
        print("Try Again !!\n\n")
        get_values()



table = {}

def simpson_rule():
    generate_y(n)
    if n %2 == 0:
        print("I'm Using Simpson's 1/3rd Rule")
        part1 = 0
        part2 = 0
        for keys in table:
            if keys % 2 == 0 and keys != 0 and keys != n:
                part2 += table[keys]
            elif keys % 2 != 0 and keys !=0 and keys !=n:
                part1 +=table[keys]
        Integral =  ((table[0] + table[final]) + 4*part1 + 2*part2)
        Integral = Integral * h/3
        print(Integral)
    elif n%3 == 0:
        print("I'm Using Simpson's 3/8th Rule")
        part1 = 0
        part2 = 0
        for keys in table:
            if keys % 3 == 0 and keys != 0 and keys != n:
                part2 += table[keys]
            elif keys %3 != 0 and keys !=0 and keys !=n:
                part1 +=table[keys]
        Integral = 3*h/8 * ((table[0] + table[final]) + 3*part1 + 2*part2)
        print(Integral)
        
  

def trapezoidal_rule():
    print("I'm using Trapezoidal Rule")
    generate_y(n)
    part1 = 0
    for keys in table:
        if keys!=0 and keys!=n:
            part1+=table[keys]
    Integral = h/2 * ((table[0] + table[final]) + 2*part1)
    print(Integral)
    

coefficient = []

def equation(coefficient):
    counter=len(coefficient)
    for i in coefficient:
        print("{}x^{}".format(i,counter),end=" ")
        if(int(i)>0 and counter!=1):
            print("+",end=" ")
        counter-=1
    if(not constant<0):
        print("+",end=" ")
    print(constant,end=" ")


def find_degree():
    for i in L:
        int(i)
        coefficient.append(i)
    
    equation(coefficient)

    if len(L) >= 3 and n!=1:
        simpson_rule()
    elif len(L) == 1 or len(L) == 2 or n==1:
        trapezoidal_rule() 

def generate_y(limit):
    x = Limit0
    for i in range(int(limit+1)):
        counter = len(coefficient)
        temp = 0        
        for j in coefficient:
            temp += int(j) * pow(x,counter)
            counter -= 1
        temp += constant
        x +=  h
        table[i] = temp
        global final
        final = i


    print(table)


if __name__ == "__main__":
    get_values()
    find_degree()
