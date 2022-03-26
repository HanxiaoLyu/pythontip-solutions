n = 5
limit = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
#if it can finish, start from the given point
#p is the current position
def finish(start):
    gas_remain = 0
    for i in range(n):
        p = (start + i) % n
        gas_remain += limit[p]
        gas_remain -= cost[p]
        if gas_remain < 0:
            return False
    return True
# call finish n times
def solve():
    for i in range(n):
        if finish(i):
            return i
    return -1

print(solve())


