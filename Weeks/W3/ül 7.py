# 7. Kommentaaride harjutus
# Kirjuta lühike (5-realine) skript, mis arvutab ristküliku
# ümbermõõdu ja pindala. Lisa iga muutuja juurde üks lühike
# selgitab kommentaar (nt # muutuja dimensioon on sentimeetrites).

# Ristküliku küljed a ja b ning nende korrutis.
a = int(input("Külg a sentimeetrites? "))
b = int(input("Teine külg b sentimeetrites? "))

print(f"Ristkülikul on küljed pikkustega {a} ja {b}.")
print(f"Teades seda, saame arvutada selle pindala valemiga: a * b = {a} * {b} = {a*b}")