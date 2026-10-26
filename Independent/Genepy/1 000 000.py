from math import ceil,sqrt

def find_prime_after(start):
    n = start
    while True:
        n += 1

        if n == 2:
            return n

        elif n > 2:
            if n % ceil(sqrt(n).real) == 0:
                continue
            for i in range(2,ceil(sqrt(n).real)+1):
                if n % i == 0:
                    break
            if n % i != 0:
                return n
        continue
    return n

print(find_prime_after(100000001))
