name1 = input("Enter the first person's name: ")
name2 = input("Enter the second person's name: ")

name1 = name1.lower()
name2 = name2.lower()

name = name1 + name2

count_t = int(name.count("t"))
count_r = int(name.count("r"))
count_u = int(name.count("u"))
count_e = int(name.count("e"))

count_l = int(name.count("l"))
count_o = int(name.count("o"))
count_v = int(name.count("v"))


count_true = count_t + count_r + count_u + count_e
count_love = count_l + count_o + count_v + count_e

percentage = 10 * count_true + 1 * count_love
if percentage < 10 or percentage > 90:
    print(f"Your score is {percentage}, you go together like coke and mentos.")

elif percentage >= 40 and percentage <= 50:
    print(f"Your score is {percentage}, you are alright together.")

else:
    print(f"Your score is {percentage}.")
