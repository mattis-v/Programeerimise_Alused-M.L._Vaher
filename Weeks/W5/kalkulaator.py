# Tee kalkulaator (+, -, *, /)

x = float(input("x? "))
y = float(input("y? "))
op = input("operator? ")

if op == "+":
    print(x + y)
    
elif op == "-":
    print(x - y)

elif op == "*":
    print(x * y)

elif op == "/":
    print(x / y)
    
for n in ["+","-","*","/"]:
    if op == n:
        