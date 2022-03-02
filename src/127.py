def get_one_from(a):
    ret = 0
    while a > 0:
        if a % 10 == 1:
            ret += 1
        a = int(a / 10)
    return ret


def solve_it():
    count = 0
    for i in range(1, 12):
        count += get_one_from(i)
    return count


print(solve_it())
