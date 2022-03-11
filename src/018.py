import math

a = 3
b = 180

def solve(a, b):
    a = min(a, b)
    b = max(a, b)
    ret1 = b
    ret2 = b
    for i in range(a, b + 1):
        for j in range(a, b + 1):
            if math.gcd(i, j) == a and i * j / a == b and j % i != 0 and i < j:
                if i + j < ret1 + ret2:
                    ret1 = i
                    ret2 = j
    print(f"{ret1} {ret2}")

solve(a, b)
# result1 = L[0][0]
# result2 = L[0][1]
#
# print(f"{result1} {result2}")
# print(L)

l = [5, 3, 1, 4]
print(l)
l2 = sorted(l)
print(l, l2)
l.sort()
print(l)
def func(x):
    return -x
l.sort(key=func)
print(l)
l = [(1, 2), (3, 4), (-1, 20)]
print(sorted(l))
def get_sum(x):
    return x[0] + x[1]
l.sort(key=get_sum)
print(l)
l.sort(key=lambda x: x[0] + x[1])
print(l)