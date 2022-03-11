a = 6
b = 4


def gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


print(a * b // gcd(a, b))
