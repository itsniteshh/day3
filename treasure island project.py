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

print("You started your journey and reached an isolated island. You explore the island and reach junction.")
direction = input("\nwhich direction you want to go? left or right:  ").lower()

if direction == "left":
  print("congratulations! you have successfully reached level 2 of the island game! Let's move ahead\nYou see a vast water body in front of you... \n")

  move = input("do you want to move ahead or wait? ").lower()
  if move == "wait":
    print("Your're something else aren't you! Congrats on completion of level 2 arcade. \nLets move on to the final level of the game.. \n")
    
    gate = input("which door would you like to take? red, blue or yellow: ").lower()
    if gate == "yellow":
      print("Hurrah! Champion. You win the game")
    
    elif gate == "red":
      print("You fell into a room of fire! Game Over")
    elif gate == "blue":
      print("You were eaten by beasts! Game Over")
  else:
      print("You were attacked by sharks! Game Over")

elif direction == "right":
  print("opps! you fell into a hole. Game Over")
else:
  print("You're disqualified")