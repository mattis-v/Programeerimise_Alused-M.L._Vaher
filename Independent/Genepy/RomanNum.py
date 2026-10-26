def from_roman_numeral(roman_numeral):
    x = 0
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ru = list(roman_numeral)

    if len(ru) == 1:
        return d[roman_numeral]

    for n in ru:

        if x == 0:
            x = d[n]

        elif dp == d[n]:
            x += d[n]
        elif dp < d[n]:
            x -= d[n]
        elif dp > d[n]:
            x += d[n]

        dp = d[n]

    return abs(x)
print(from_roman_numeral("XXI"))