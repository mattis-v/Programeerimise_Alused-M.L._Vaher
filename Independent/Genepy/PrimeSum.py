from math import ceil,sqrt

def sum_primes(n):
    lst=[]
    for n in range(1,n):
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
    return sum(lst)

print(sum_primes(79))