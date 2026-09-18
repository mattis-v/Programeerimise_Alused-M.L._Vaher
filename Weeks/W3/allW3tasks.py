"""
Nädal 1 — Käivitumine

Enne tegemist: paigalda uv, Thonny, Git ja loo GitHub-konto.
Iga ülesanne lõpeta oma git-hoidlas eraldi commitiga.
Muutujanimed peavad olema muutuja sisu kirjeldavad (sh tsükliloendurid).
"""


# 0. Git-harjutus
# Tee endale GitHub-konto
# Klooni projekt enda arvutisse




# 1. Tervitaja
# Küsi kasutaja nimi ja sünniaasta ( input() funktsioon).
# Arvuta ligikaudne vanus.
# Väljasta tulemus konsooli, nt "Tere, Mari! Sa oled umbes 34 aastat vana."

nimi = input("Mis teie nimi on? ")
sünniaasta = input("Mis on sinu sünniaasta? ")
print(f"Tere {nimi}!")
vanus = (2026 - int(sünniaasta))
print(f"Te olete {vanus} aastat vana!")


# 2. Ühikuteisendaja
# Küsi pindala hektarites.
# Väljasta sama pindala ruutmeetrites (1 ha = 10000 m²)
# ja aakrites (1 ha = 2.47105 aakrit).

hpindala = int(input("Pindala hektarites? "))
rmeetrit = (int(hpindala) * 10000)
aakr = (int(hpindala) * 2.47105)

print(f"Teisendused: {rmeetrit} m2 ja {aakr} aakrit")


# 3. Visiitkaart
# Küsi nimi, eriala ja lemmiktoit.
# Väljasta need korralikult vormindatuna (nt raamiga tärnidest),
# kasutades mitut print()-lauset. Eesmärk on print'i tunnetada, mitte loogikat.

nimi = input("Teie nimi? ")
eriala = input("Teie eriala? ")
Ltoit = input("Teie lemmiktoit? ")

print("\n", f"Teie nimi on {nimi}, töötate {eriala} erialal ja teie lemmik toiduks on {Ltoit}.")


# 4. Nimetamise harjutus
# On antud skript, kus kõik muutujad on halvasti nimetatud.
# Nimeta muutujad ümber nii, et kood on ilma kommentaarideta arusaadav.
# Väljund ei tohi muutuda.

# a = 180
# b = 75
# c = a - (b + 100)

#print("Kehamassiindeks lähedal:", c)

pikkus = 180
kaal = 75
KMI = pikkus - (kaal + 100)

print("Kehamassiindeks lähedal:", KMI)


# 5. Käsu järjekord
# Loo kolm eraldi skripti (või kolm plokki), mis erinevad AINULT
# ridade järjekorra poolest ja väljastavad iga kord erineva tulemuse:
#
# x = 5
# print(x)
# x = x + 1
#
# Muuda ridade järjekorda kolmel eri moel ja kirjuta iga variandi kohta
# kommentaarina, mida see prindib.


# 6. Muuda skripti
# All olev skript töötab. Muuda seda nii, et see küsib kasutajalt
# ka perekonnanime ja lisab selle tervitusse.
#nimi = "Mari"
#print("Tere, " + nimi + "!")

Nees = input("Teie eesnimi? ")
Npere = input("Teie perekonnanimi? ")

print(f"Tere, {Nees} {Npere}!")


# 7. Kommentaaride harjutus
# Kirjuta lühike (5-realine) skript, mis arvutab ristküliku
# ümbermõõdu ja pindala. Lisa iga muutuja juurde üks lühike
# selgitab kommentaar (nt # muutuja dimensioon on sentimeetrites).

# Ristküliku küljed a ja b ning nende korrutis.
a = int(input("Külg a sentimeetrites? "))
b = int(input("Teine külg b sentimeetrites? "))

print(f"Ristkülikul on küljed pikkustega {a} ja {b}.")
print(f"Teades seda, saame arvutada selle pindala valemiga: a * b = {a} * {b} = {a*b}")


# 8. Mitme sisendi vastuvõtja
# Küsi kasutajalt kolm arvu (kolm eraldi input()-i).
# Väljasta nende summa ja keskmine.

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

print(f"a = {a} ; b = {b} ; c = {c}")
print(f"a + b + c = {a + b + c}")
print(f"aritmeetiline keskmine = {round((a + b + c)/3, 2)}")


# 9. Git-harjutus
# See ei ole Python, vaid käsurea harjutus:
# Loo uus fail nadal1_git.txt, kirjuta sinna üks lause selle kohta,
# mis vahe on lähtekoodil ja täitmisel. Tee: git add, git commit, git push.
# Kirjuta siia kommentaarina oma commiti sõnum.


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