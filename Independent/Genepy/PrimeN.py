from cmath import sqrt

def is_prime(n):
    i = 1
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    while True:
        i += 1
        if n % i == 0:
            return False
        elif i == sqrt(n).real:
            return False
        elif i >= sqrt(n).real:
            break
    return True

for x in range(1000001):
    print(x,is_prime(x))
