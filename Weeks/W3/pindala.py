# 2. Ühikuteisendaja
# Küsi pindala hektarites.
# Väljasta sama pindala ruutmeetrites (1 ha = 10000 m²)
# ja aakrites (1 ha = 2.47105 aakrit).

hpindala = int(input("Pindala hektarites? "))
rmeetrit = (int(hpindala) * 10000)
aakr = (int(hpindala) * 2.47105)

print(f"Teisendused: {rmeetrit} m2 ja {aakr} aakrit")