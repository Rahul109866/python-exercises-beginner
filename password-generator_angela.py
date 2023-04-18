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
    "a",
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
# get how many preferred charecter sets in the password from user
letters_input = int(input("How many letters do you want:\n"))
numbers_input = int(input("How many numbers do you want:\n"))
symbols_input = int(input("HOw many symbols do you want:\n"))

# easy version
# in this version just get random letters from each list and print them together. easier to crack
"""password = ""

for a in range(1, letters_input + 1):
    password += random.choice(letters)

for b in range(1, numbers_input + 1):
    password += random.choice(numbers)

for c in range(1, symbols_input + 1):
    password += random.choice(symbols)

print(password)"""


# hard version
# in this method, get the required random chars from each set as a list and then randomize the list and print

password_list = []
# -----> method 1:using addition operator
"""for a in range(1, letters_input + 1):
    password_list += random.choice(letters)

for b in range(1, numbers_input + 1):
    password_list += random.choice(numbers)

for c in range(1, symbols_input + 1):
    password_list += random.choice(symbols)"""


# ----->method 2:  using .append() function
# in this we just append the resulting random charecter to the password list
for a in range(1, letters_input + 1):
    password_list.append(random.choice(letters))

for b in range(1, numbers_input + 1):
    password_list.append(random.choice(numbers))

for c in range(1, symbols_input + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)  # shuffles the elements of list in place
print(password_list)

# print list as string:
# ----->method 1: use for loops to get each char from list and add it to string variable
"""password = ""

for char in password_list:
    password += char
"""
# ----->method 2;use .join function to convert list to string
password = "".join(password_list)
print(f"Your password is: {password}")


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# def forward:
# move()


def jump():
    if wall_in_front():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

    else:
        move()


while not at_goal():
    jump()
