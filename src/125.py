money = 0
while len(L) > 1:
    L.sort()
    a = L[0]
    b = L[1]
    L = L[2:]
    c = a + b
    L.append(c)
    money += c

print(money)