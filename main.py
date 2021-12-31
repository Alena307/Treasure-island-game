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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
name = input("Whats your name? ")
print(name)
first = input("You are crossroad. Where do you want to go? left or right\n").lower()
print(first)
if first == "left":
  print("Sorry! You fall in a whole. Game over!\n")
else:
    print(f"Good choice, {name}. ")
    input2 = input("You cam to a lake. Do you want to swim or take a boat? Write swim or boat\n")
    if input2 == "swim":
      print("What are you doing? There are so many sharkes and crocodiles in the lake. Game over!\n")
    else:
      print("Wow! You crossed safe the lake!")
      input4 = input("You arrive the island unharmed. There are 3 doors. One red, one yellow, one blue and one black. Which colour do you choose?\n")
      print(input4)
      if input4 == "red":
        print("You chose a door that doesn't exist. Game over!")
      elif input4 == "yellow":
        print("You enter a room of beast. Game over.")
      #elif input4 == "black":
        print("Black is like the death. Game over!")
      #elif input4 <> "black" and input4 <> "blue" and input4 <> "yellow" and input4 <> "red":
        print("Wrong answer. What colour do you choose?")
      else:
        print(f"You find the treasure! You win, {name}!")


