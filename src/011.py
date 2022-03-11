L = [2, 8, 3, 50]
num_of_2 = 0
num_of_5 = 0

for i in L:
    while i % 2 == 0:
        num_of_2 += 1
        i = i // 2
    while i % 5 == 0:
        num_of_5 += 1
        i = i // 5

print(min(num_of_2, num_of_5))

# 大家的答案里是i // 2 and i //5,为什么？
