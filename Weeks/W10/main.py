import UuendatudLadu as module
fail = "tooted.csv"
n = "\n"

readfile = module.csv_reader(fail)
laofail = module.laoseis(fail)
minmax = module.min_max(fail)
km_ita_summa = module.laovaartus(fail)

km_22 = module.km_loend(fail, 22.0)
km_9 = module.km_loend(fail, 9.0)

a = module.hind_km(fail)
b = module.hind_km_uus(fail)


count = 0

for line in readfile:
    count += 1
print(f"Tooteid: {count}{n}")

count = 0

for line in laofail:
    count += 1
    print(line)

print(f"{n} Otsas: {count} {n}")
print(f"min: {minmax.get("min")} {n} {minmax.get("dmin")} {2*n} max: {minmax.get("max")} {n} {minmax.get("dmax")} {n}")
print(f"22%: {km_22} / 9%: {km_9} {n}")
print(f"Laoväärtus: {km_ita_summa}")
print(f"Laoväärtus vana maksuga: {a}")
print(f"Laoväärtus uue maksuga: {b}")
print(f"Nende vahe: {abs(round(a-b,2))}")