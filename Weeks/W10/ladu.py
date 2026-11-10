import csv
n = "\n"

#1
def csv_reader(fail):   
    with open(fail, encoding="UTF-8") as fi:
        contents = csv.DictReader(fi, delimiter=";")
        for line in contents:
            yield line


#2
def laoseis(fail):
    for line in csv_reader(fail):
        ladu = int(line.get("laoseis"))
        nimetus = line.get("nimetus")
        if  ladu == 0:
            yield nimetus
    

#3
def min_max(fail):
    min = float("inf")
    max = float("-inf")
    
    for line in csv_reader(fail):
        d = float(line.get("hind_km_ta"))
        
        if  d > max:
            max = d
            dmax = line
        if d < min:
            min = d
            dmin = line
           
    return dict(min=min,max=max,dmin=dmin,dmax=dmax)


#4
def laovaartus(fail):
    summa = 0.0
    for line in csv_reader(fail):
        hind = float(line.get("hind_km_ta"))
        arv = float(line.get("laoseis"))
        summa += round(hind, 2) * arv

    return round(summa, 2)


#5
def km_loend(fail, otsitav):
    summa = 0
    for line in csv_reader(fail):
        km = float(line.get("km_maar"))
        if km == otsitav:
            summa += 1
            
    return int(summa)


#6
def hind_km(fail):
    summa = 0.0
    for line in csv_reader(fail):
        alghind = float(line.get("hind_km_ta"))
        km = float(line.get("km_maar"))
        arv = float(line.get("laoseis"))
         
        hind = alghind * (1 + km / 100)
        summa += round(hind,2) * arv
        
    return(round(summa, 2))


#7
def hind_km_uus(fail):
    summa = 0.0
    for line in csv_reader(fail):
        alghind = float(line.get("hind_km_ta"))
        km = float(line.get("km_maar"))
        arv = float(line.get("laoseis"))
        
        if km == 22:
            km = 24
            
        hind = alghind * (1 + km / 100)
        summa += round(hind,2) * arv
        
    return(round(summa, 2))