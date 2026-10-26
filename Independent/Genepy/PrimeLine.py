from math import ceil,sqrt

def range_primes(start,stop):
    lst=[]
    for n in range(start,stop):
        if n == 2:
            print("added", n)
            lst.append(n)
            continue
        elif n > 1:
            if n % ceil(sqrt(n).real) == 0:
                continue
            for i in range(2,ceil(sqrt(n).real)+1):
                if n % i == 0:
                    break
            if n % i != 0:
                print("added", n)
                lst.append(n)
                continue
        elif n == 1 or n < 1:
            continue
    print(*lst, sep=", ")

range_primes(100000000,100500000)