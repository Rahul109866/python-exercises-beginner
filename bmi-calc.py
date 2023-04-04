# this program is to calculate the Body Mass Index of a person with their height and weight as data

height = input("Enter your height in metres: ")
weight = input("Enter your weight in kilograms: ")

bm_index = float(weight) / (float(height) * float(height))
print(f"Your Body Mass Index is : {int(bm_index)}!")
