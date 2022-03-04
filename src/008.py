L = [0, 1, 2, 3, 4]
L = sorted(L)
if len(L) % 2 == 0:

    median = (L[int(len(L)/2)] + L[int(len(L)/2 - 1)]) / 2
    answer = round(median, 1)
else:
    median = L[int((len(L) - 1) / 2)]

answer = round(median, 1)
print(answer)

