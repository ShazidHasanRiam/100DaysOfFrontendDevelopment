#Day-03 of 100 Days of Coding
#November 20, 2020
#Shazid Hasan Riam

print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, Where do you want to go? Type "left" or "right".\n').lower()

if choice1 == "left":
    #Continue in the game
    choice2 = input('You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type '
          '"swim" to swim across. \n').lower()
    if choice2 == "wait":
        #Game will continue
        choice3 = input("You arrived at the island unarmed. There is a house with three doors. One red, one yellow and one blue."
              "Which color do you choose?\n").lower()
        if choice3 == "red":
            print("Its a room full of fire. Game Over.")
        elif choice3 =="yellow":
            print("You Found The Treasure! You Win!")
        elif choice3 == "blue":
            print("You entered a room of beasts. Game Over.")
        else:
            print("You choose a door that does not exixt. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You Fell into a hole. Game Over.")







