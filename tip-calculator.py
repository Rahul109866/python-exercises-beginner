# this program calculates the amount per head after accounting for tip at a restaurant

bill_amount = float(input("Enter the bill amount $"))
tip_percentage = int(input("Enter the tip percentage. Is it 10%, 12%, or 15%"))
total_amount = bill_amount * (tip_percentage / 100.00) + bill_amount
person_number = int(input("Enter the number of people"))
share_amount = round((total_amount / person_number), 2)
print(f"Each person's share is {share_amount:.2f}")
