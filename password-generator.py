import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

letters_input = int(input("How many letters do you want:\n"))
numbers_input = int(input("How many numbers do you want:\n"))
symbols_input = int(input("HOw many symbols do you want:\n"))
"""temp = letters + numbers + symbols
temp1 = random.choice(temp)
print("\n")


for letters1 in range(1, letters_input + 1):
    print(random.choice(temp1), end="")

for numbers1 in range(1, numbers_input + 1):
    print(random.choice(temp1), end="")

for symbols1 in range(1, symbols_input + 1):
    print(random.choice(temp1), end="")

print("\n")"""

password = ""

for letters1 in range(1, letters_input + 1):
    password += random.choice(letters)

for numbers1 in range(1, numbers_input + 1):
    password += random.choice(numbers)

for symbols1 in range(1, symbols_input + 1):
    password += random.choice(symbols)

print(password)
password1 = list(password)
passwordnew = random.sample(password1, len(password1) - 1)
# print("".join(passwordnew))
print("".join(str(e) for e in passwordnew))

print(password)
