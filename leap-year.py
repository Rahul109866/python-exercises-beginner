# program to check if input is leap year or not
year = int(input("Which year do you want to check? "))

if year % 4 != 0:
    print("Not leap year.")  # remove the biggest offending condition first

else:
    if year % 100 != 0:
        print("Leap year.")
    elif year % 400 == 0:
        print("Leap year.")
    else:
        print("Not Leap year.")
