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

# easy version

"""password = ""

for a in range(1, letters_input + 1):
    password += random.choice(letters)

for b in range(1, numbers_input + 1):
    password += random.choice(numbers)

for c in range(1, symbols_input + 1):
    password += random.choice(symbols)

print(password)"""


# hard version

password_list = []
# using addition operator
"""for a in range(1, letters_input + 1):
    password_list += random.choice(letters)

for b in range(1, numbers_input + 1):
    password_list += random.choice(numbers)

for c in range(1, symbols_input + 1):
    password_list += random.choice(symbols)"""


# using .append() function
for a in range(1, letters_input + 1):
    password_list.append(random.choice(letters))

for b in range(1, numbers_input + 1):
    password_list.append(random.choice(numbers))

for c in range(1, symbols_input + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
print(password_list)

"""password = ""

for char in password_list:
    password += char
"""

password = "".join(password_list)
print(f"Your password is: {password}")
