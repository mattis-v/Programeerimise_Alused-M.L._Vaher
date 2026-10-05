# Tee kalkulaator (+, -, *, /)

def summ(a,b):
    print("a + b = ")
    return a + b

def neg(a,b):
    print("a - b = ")
    return a - b

def mult(a,b):
    print("a * b = ")
    return a * b

def div(a,b):
    print("a / b = ")
    return a / b

x = float(input("x? "))
operation = input("operation? ")
y = float(input("y? "))

operator = {"+": summ, "-": neg, "*": mult, "/": div}

print(operator[operation](x,y))