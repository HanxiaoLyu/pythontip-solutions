a = "21abcba"
n = 5
def check(x):
    for i in range(n):
        print(x+i, x+n-1-i)

        if a[x + i] != a[x + n -1 - i]:
            return False
    return True

def solve():
    for i in range(len(a)- n +1):
        if check(i):
            return True
    return False

if solve():
    print("YES")
else:
    print("NO")