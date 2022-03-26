L = [1, 1, 3, 3, 4]

if L == sorted(L):
    print('UP')
elif L == sorted(L, reverse=True):
    print('DOWN')
else:
    print('WRONG')
