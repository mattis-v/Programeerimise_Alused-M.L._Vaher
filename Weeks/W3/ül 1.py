# 1. Tervitaja
# Küsi kasutaja nimi ja sünniaasta ( input() funktsioon).
# Arvuta ligikaudne vanus.
# Väljasta tulemus konsooli, nt "Tere, Mari! Sa oled umbes 34 aastat vana."

nimi = input("Mis teie nimi on? ")
sünniaasta = input("Mis on sinu sünniaasta? ")
print(f"Tere {nimi}!")
vanus = (2026 - int(sünniaasta))
print(f"Te olete {vanus} aastat vana!")