def how_to_pay(amount,currency):
    lst = []
    dictlst = {}
    difference = amount
    csorted = sorted(currency, reverse=True)

    for coin in csorted:
        if difference == 0:
            break
        while difference - coin >= 0:
            lst.append(coin)
            difference -= coin

        
    for key in csorted:
        x = 0
        for coin in lst:
            if coin == key:
                x += 1
        if x != 0:
            dictlst[key] = x

    return(dictlst)


euro = [1, 2, 5, 10, 20, 50, 100, 200, 500]
x = 1112
print(how_to_pay(x,euro))