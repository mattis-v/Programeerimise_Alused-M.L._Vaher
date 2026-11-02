def love_meet(bob, alice):
    dbob = {}
    compiled = {}

    for key in bob:
        dbob[key] = key

    for district in alice:
        fd = dbob.get(district)
        if fd != None:
            compiled[fd] = None

    return(set(compiled))

def affair_meet(bob, alice, silvester):
    dbob = {}
    dalice = {}
    compiled = {}

    for key in bob:
        dbob[key] = key
    for key in alice:
        dalice[key] = key

    for district in silvester:
        fd = dalice.get(district)
        if fd != None and dbob.get(district) == None:
            compiled[fd] = None

    return(set(compiled))


alice = ['Ⅱ', 'Ⅳ', 'Ⅱ', 'ⅩⅠⅩ', 'ⅩⅤ', 'Ⅳ', 'Ⅲ']
bob = ['Ⅳ', 'Ⅲ', 'Ⅱ', 'ⅩⅩ', 'Ⅱ', 'ⅩⅩ']
silvester = ['ⅩVⅢ', 'ⅩⅠⅩ', 'Ⅲ', 'Ⅰ', 'Ⅲ', 'ⅩVⅢ']

print(love_meet(bob, alice))
print(affair_meet(bob, alice, silvester))