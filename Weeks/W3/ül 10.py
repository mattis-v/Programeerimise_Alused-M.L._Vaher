# 10. Enda valitud ülesanne
# Mõtle oma erialalt (agronoomia, keskkond, loomakasvatus jm) välja
# üks lihtne "sisend -> arvutus -> väljund" skript, mis kasutab
# ainult print() ja input(). Näiteks: söödakoguse arvutaja
# looma kaalu järgi. Nimeta muutujad kirjeldavalt.

# I = U/R ==> vool võrdub pinge jagatud takistusega

print ("I = U/R")
U = float(input("U = "))
R = float(input("R = "))
print (f"I = {U}/{R} = {U/R} A")

# float() lisatud et muuta string tüüp arv väärtuseks.