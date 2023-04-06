# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill_amount = 0
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if size == "S":
    bill_amount = 15
    if add_pepperoni == "Y":
        bill_amount += 2

if size == "M":
    bill_amount = 20
    if add_pepperoni == "Y":
        bill_amount += 3

if size == "L":
    bill_amount = 25
    if add_pepperoni == "Y":
        bill_amount += 3

if extra_cheese == "Y":
    bill_amount += 1

print(f"Your total bill is ${bill_amount}.")
