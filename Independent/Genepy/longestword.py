def longest_word(text):
    textlist = text.split()
    n = 0
    Lword = 0
    for i in textlist:
        if len(i) > n:
            n = len(i)
            Lword = i
    print(Lword)

longest_word("We want a SHRUBBERY")