print("Welcome to the rollercoaster")
height=int(input("What is your height in cm: "))
bill=0

if height<120:
	print("Sorry you cannot ride this rollercoaster yet. Grow more!")

else:
	age=int(input("What is your age: "))
	if age<12:
		print("Children's tickets are 5$")
		bill=5

	elif age<18:
		print("Youth tickets are 7$")
		bill=7

	else:
		print("Adult tickets are 12$")
		bill=12

	photo_choice=input("Would you like a photograph taken for 3$? Press Y for yes and N for no: ")
	if photo_choice=="Y":
		bill+=3

	print(f"Your total bill is {bill}$.")


