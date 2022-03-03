def is_prime(a):
    for j in range(2, a):
        if a % j == 0:
            return False
    return True


answer = []
for i in range(2, 101):
    if is_prime(i):
        answer.append(str(i))
print(" ".join(answer))

# is_first = True
# for i in range(2, 101):
#     if is_prime(i):
#         if is_first:
#             is_first = False
#         else:
#             print(" ", end="")
#         print(f"{i}", end="")
