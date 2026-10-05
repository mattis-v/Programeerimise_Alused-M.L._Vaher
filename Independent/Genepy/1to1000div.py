def sumOfDigits(n):
    sum = 0
    while n != 0:
        last = n % 10
        sum += last
        n //= 10
    return sum



for n in range(0,1001):
    if (n % 7) == 0 and (sumOfDigits(n) % 3) == 0:
        print(n)