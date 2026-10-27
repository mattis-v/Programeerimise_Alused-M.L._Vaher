from unicodedata import normalize, combining
def is_anagram(left, right):

    NL = normalize("NFD",left.lower())
    RL = normalize("NFD",right.lower())

    L = sorted(list(NL))
    R = sorted(list(RL))
    lr = []
    rr = []

    for cl in L:
        if combining(cl) != 0 or ord(cl) == 32 or ord(cl) == 45:
            lr.append(cl)
    for x in lr:
        L.remove(x)

    for cr in R:
        if combining(cr) != 0 or ord(cr) == 32 or ord(cr) == 45:
            rr.append(cr)
    for y in rr:
        R.remove(y)

    if L == R:
        return True
    elif L != R:
        return False


print(is_anagram("sortie","rôties"))

print(ord("-"))