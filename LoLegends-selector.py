print(
    "This program helps you choose the role you might like in the game League of Legends!"
)
user_input = int(input("Do you like to 1) pew pew! or 2) Bam Bam!\nPress 1 OR 2 "))
if user_input == 1:
    user_input2 = int(input("Do you like to 1)Shoot 2)Use Magic?\nPress 1 or 2 "))
    if user_input2 == 1:
        print("The role suitable for you is: Marksman!")
    else:
        print("The role suitable for you is: Mage!")
else:
    user_input3 = int(
        input(
            "Do you like to 1)Fight or do you like to 2) catch enemies?\nPress 1 or 2 for your response!"
        )
    )
    if user_input3 == 1:
        print("The role suitable for you is: Juggernaught!")
    else:
        print("The role suitable for you is: Engage Support!")
