import random

print("Rock Paper Scissors")
choice = input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n")

if not choice.isdigit():
    print("Please enter a number between 0 and 2.")
else:
    choice = int(choice)
    if choice not in [0,1,2]:
        print("please enter 0, 1, or 2.")
    else:
        computer = random.randint(0,2)
        choices =["Rock", "Paper", "Scissors"]
        print("you choose:", choices[choice])
        print("Computer choose:", choices[computer])

        if choice == computer:
            print("it's a draw!")
        elif choice == 0 and computer == 2:
            print("You win! Rock beats Scissors.")
        elif choice == 1 and computer == 0:
            print("You win! Paper beats Rock.")
        elif choice == 2 and computer == 1:
            print("You win! Scissors beats Paper.")
        else:
            print("You loose!") 
