from cmath import sqrt
from math import ceil

def is_prime(n):
    if n > 2:
        if n % ceil(sqrt(n).real) == 0:
            return False
        for i in range(2,ceil(sqrt(n).real)):
            if n % i == 0:
                return False
    elif n < 1 or n == 1:
        return False
    return True

for n in range(1,100):
    print(n,is_prime(n))

print(is_prime(3))
print(ceil(sqrt(4).real))
