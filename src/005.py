a = 'xyzwd'
list_a = list(a)
b = []
for i in range(len(a)):
    if i % 2 == 0:
        b.append(list_a[i])

print(''.join(b))