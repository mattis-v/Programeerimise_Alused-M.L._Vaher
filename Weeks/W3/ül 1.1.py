# 1. Tervitaja
# Küsi kasutaja nimi ja sünniaasta ( input() funktsioon).
# Arvuta ligikaudne vanus.
# Väljasta tulemus konsooli, nt "Tere, Mari! Sa oled umbes 34 aastat vana."
# 1.1 Kontrolli vanust

nimi = input("Mis su nimi on? ")
sünniaasta = int(input("Mis on sinu sünniaasta? "))
print(f"Tere {nimi} aastast {sünniaasta}.")
vanus = (2026 - int(sünniaasta))
print(f"Te olete {vanus} aastat vana!")

def kontrollitavvanus(vanuse_kontroll):
    if 16 > vanuse_kontroll >= 14:
        print("Tattnina")
    if 18 > vanuse_kontroll >= 16:
        print("Noor")
    if 21 > vanuse_kontroll >= 18:
        print("Täisealine")
    if 24 > vanuse_kontroll >= 21:
        print("Joodik")
    if 40 > vanuse_kontroll >= 24:
        print("Sõitija")
    if vanuse_kontroll >= 40:
        print("Presidendi")
kontrollitavvanus(vanus)

    vanused = {14: "süüdiv",
               16: "KOV",
               18: "RK", "EP" "ÕLU"
               21: A-kat}