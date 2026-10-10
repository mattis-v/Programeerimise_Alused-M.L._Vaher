from string import ascii_lowercase as x
lst = list(x)
len(lst)

for i in lst:
    for n in lst:
        if not n==i:
            print(i+n)