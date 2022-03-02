a = {4: 3, 8: 7, 3: 4}


def solve_it():
    x = []
    for key in a:
        x.append(str(key))

    return ",".join(sorted(x))


print(solve_it())
