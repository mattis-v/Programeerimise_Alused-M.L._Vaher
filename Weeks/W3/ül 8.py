# 8. Mitme sisendi vastuvõtja
# Küsi kasutajalt kolm arvu (kolm eraldi input()-i).
# Väljasta nende summa ja keskmine.

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

print(f"a = {a} ; b = {b} ; c = {c}")
print(f"a + b + c = {a + b + c}")
print(f"aritmeetiline keskmine = {round((a + b + c)/3, 2)}")