# this program prints all the even numbers from 1-100

total = 0
for number in range(2, 101):
    if number % 2 == 0:
        total += number

print(f"The sum of even numbers from 1-100 is: {total}.")
