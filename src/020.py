a = "cagy"
b = 3
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]

for letter in a:
    print(letters[(letters.index(letter) + b) % 26], end='')
