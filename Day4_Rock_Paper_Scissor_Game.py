import random

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_input = random.randint(0,2)

print((user_input,computer_input)) #converting it to a tuple

ASCII_Code =[("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""),
("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""),
("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")]


if(user_input in [0,1,2]):
    print("User input",user_input)
    print("You Choose",ASCII_Code[user_input])
    print("Computer Choose",ASCII_Code[computer_input])
    if ((user_input,computer_input) in [(0,2),(1,0),(2,1)]): #All possible outcomes for wins
        print("You Win")
    elif ((user_input,computer_input) in [(0,1),(1,2),(2,0)]):
        print("You Loose")
    else:
        print("It's a draw") #Conditions to check the draw
else:
   print("Incorrect choice. Please select between 0, 1 and 2.")