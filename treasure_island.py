print("Welcome to The Knight's Quest!\nYour mission is to find the treasure.")
player_name = input("What is your name?: ")

print(
    '''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
'''
)
print(
    "You arrive at the obelisk that was foretold in your dreams.\nThe path diverges into a fork and you must make a decision which one you will be walking."
)
path_choice = input("Type left or right: ").lower()

if path_choice == "left":
    print(
        """You eventually reach the decrepit lake near the foot of the mountain Gha'agru.
        The waters look too dark and troublesome to swim across.
        But then, you recount the village rumor of Dagongorn, the hermit by the mountain who knows the lay of the land and might get you across.IF he is to be found.
        """
    )
    swim_choice = input(
        "Do You want to swim or take your chances with a village tale?"
    ).lower()
    if swim_choice == "wait":
        print(
            """You decide bet your life on a village tale and that village tale eventually came to be true.
        A tall figure draped in black robes and a lamp on his hand walks towards you.
        You overcome your crippling sense of anxiety and fear and bellow out.
          "I need to get across this lake at any cost for such doom awaits humanity if i dont make it!"
            "Yes.Dagongorn can take you across but Dagongorn doubts your claim of doom awaiting.Prove it by sacrifice or die fighting me for invading my land!"
        You are left with no choice but to sacrifice.\n You ask what proof does he need knowing full well it will be something impossible.
            "Your index and ring finger" came the reply.
        This was much better than what you feared. You chop it off with your dagger and he agrees to help you cross the lake.
        Before you could thank him for his help, he was long gone and the boat tracks on the mud were found to be nowhere.
        You press on with the task at hand and arrive at the abandoned mineshaft at the foot of the legendary Gha'agru mountain.
        There are two mineshafts burrowing deep into the mine and you must make a choice.
          """
        )
        mine_choice = input("Left or right").lower()
        if mine_choice == "right":
            print(
                """You fall through for a couple of seconds and land in a dimly lit cave.
            Something catches your eye and it is none other than the golden chest that will be the answer to your predicament.
            You open it with bated breath and hope it is a divine weapon or armor that will help you fight off the demonwraith invasion that is inevitable.
            In the chest you find........
            The divine Bow of the Gods that binds to its owner and smites demons.
            Your elation soon disappears and dread fills your system as you look down on your right hand.
            ...
            ...
            ...
            ...
            ...
            """
            )
            print(
                r"""           
            .
            .
            .
            .
            .
            !-!-*-!-||GAME OVER||-!-*-!-!"
            """
            )

        else:
            print(
                f'''You fall into a bottomless pit and before you could come to your senses of where you are, the fall halts.
            A burning sensation spreads across your torso as you realise the pointy rock formation impaling you.
            Unfortunate.
            ***{player_name}*** died.
            
            !-!-*-!-||GAME OVER||-!-*-!-!"'''
            )

    else:
        print(
            f"""Unbeknownst to you, this lake is the hunting ground of the Gael'ims, alligator like monsters that swarm their prey and leave only the tint of blood in the lake.
           ***{player_name}*** died.
            
          !-!-*-!-||GAME OVER||-!-*-!-!"""
        )

else:
    print(
        f"""You walked right into the necromancer lair.\nThere was no coming back from that.
            ***{player_name}*** died.
            
      !-!-*-!-||GAME OVER||-!-*-!-!"""
    )
