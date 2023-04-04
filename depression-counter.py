# This program calculates how much weeks you got left to live if you are lucky to live until the age of 90

print(
    "Do you want to find out how much time you got left if you live until your expected years old?"
)
expected_years = int(input("Enter your expected age "))
age_in_years = int(input("Enter your current age "))
weeks_left_user = (90 * 52) - (age_in_years * 52)
days_left_user = (90 * 365) - (age_in_years * 365)
months_left_user = (90 * 12) - (age_in_years * 12)

print(
    f"You have {weeks_left_user} weeks, {days_left_user} days and {months_left_user} months left to live"
)
