def get_one_from(a):
    ret = 0
    while a > 0:
        if a % 10 == 1:
            ret += 1
        a = int(a / 10)
    return ret


def solve_it():
    sum = 0
    for i in range(1, n + 1):
        sum += get_one_from(i)
    return sum


print(solve_it())
