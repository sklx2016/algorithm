#递归法

def gcd(m, n):
    if m > n:
        return gcd(m - n, n)
    elif m < n:
        return gcd(m, n - m)
    else:
        return m


#辗转相除法

def gcd2(m, n):
    if m < n:
        m, n = n, m
    a = m % n
    while a != 0:
        m = n
        n = a
        a = m % n
    return n


print(gcd(100, 80))
print(gcd2(100, 80))
