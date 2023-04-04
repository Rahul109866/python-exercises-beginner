# This program gets a two digit number and then adds the two digits and displays the sum!

two_digit_number = input("Enter the two digit number: \n")

# print(type(two_digit_number))
# to check the datatype of the data input

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
result = first_digit + second_digit

print(f"The sum of the digits of {two_digit_number} is {result}")
