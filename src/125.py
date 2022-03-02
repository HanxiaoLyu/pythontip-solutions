from queue import PriorityQueue
L = [1, 2, 3, 4, 5]

# money = 0
# while len(L) > 1:
#     L.sort()
#     a = L[0]
#     b = L[1]
#     L = L[2:]  # delete the first 2 items of L
#     c = a + b
#     L.append(c)
#     money += c
#
# print(money)


q = PriorityQueue()
for a in L:
    q.put(a)
money = 0
while not q.empty():
    a = q.get()
    b = q.get()
    c = a + b
    money += c
    if q.empty():
        break
    q.put(c)

print(money)
