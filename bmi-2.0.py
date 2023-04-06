# this program is an updated version of the bmi calculator that calculates the user's bmi and shows them their diagnosis

height = float(input("Enter your height in metres: "))
weight = round(float(input("Enter your weight in Kilograms: ")))
body_mass_index = weight / (height**2)
formatted_bmi = float("{:.1f}".format(body_mass_index))


print(f"Your Body Mass Index is {formatted_bmi}")


# code to check bmi value and their inferences

if formatted_bmi < 18.5:
    print("You are underweight")

elif formatted_bmi < 25:
    print("You have a normal weight")

elif formatted_bmi < 35:
    print("You are overweight")

else:
    print("You are clinically obese")
