def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    l = [1]
    pp = 0
    for i in range(0,n-1):
        ip = l[i] + pp
        pp = l[i]
        l.append(ip)
    return(l)

print(fibonacci(0))