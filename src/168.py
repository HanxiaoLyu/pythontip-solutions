a = 11
b = 20

# def digits(a, x):
#     ret = 0
#     while a > 0:
#         if a % 10 == x:
#             ret += 1
#         a = int(a / 10)
#     return ret
#
# def solve_once(x):
#     count = 0
#     for i in range(a, b+1):
#         count += digits(i, x)
#     return count
#
# for i in range(10):
#     print(solve_once(i))

answers = [0] * 10

def digits(a):
    ret = 0
    while a > 0:
        answers[a % 10] += 1
        a = int(a / 10)
    return ret

for i in range(a, b+1):
    digits(i)

for i in range(10):
    print(answers[i])