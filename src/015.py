
def solve_it():

    b = []
    for index, char in enumerate(a):
        if char >= 'A' and char <= 'Z':
            temp = chr(ord(a[index]) - (ord('A') - ord('a')))
        else:
            temp = char
        b.append(temp)
    return ''.join(b) 

print(solve_it())  