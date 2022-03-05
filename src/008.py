L = [0, 1, 2, 3, 4]
F = [2, 3, 4, 5, 6]


def median(a):
    a = sorted(a)
    if len(a) % 2 == 0:
        median = (a[int(len(a) / 2)] + a[int(len(a) / 2 - 1)]) / 2
    else:
        median = a[int((len(a) - 1) / 2)]

    answer = round(median, 1)
    return answer


print(median(L))
print(median(F))


# L = sorted(L)
# if len(L) % 2 == 0:
#
#     median = (L[len(L)//2] + L[len(L)//2 - 1]) / 2
#     answer = round(median, 1)
# else:
#     median = L[(len(L) - 1) // 2]
#
# answer = round(median, 1)
# print(answer)
#
