L = [2, 8, 3, 50]
a = 1
for i in L:
    a *= i
    while a % 10 == 0:
        a = a // 10

print(a % 2)
