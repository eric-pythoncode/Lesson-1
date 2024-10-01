import random

userChoice = input("Enter which one you want to choose - rock, paper, or scissors? ")
computerChoice = random.choice(["rock" , "paper" , "scissors"])
cheatCode = input("Enter cheat code: ")
print(computerChoice)
if cheatCode == "cheat":
    print("Player has used cheatcode; instant win")
elif userChoice == computerChoice:
        print("Tie")
elif (userChoice == "rock" and computerChoice == "scissors") or\
    (userChoice == "scissors" and computerChoice == "paper") or\
    (userChoice == "paper" and computerChoice == "rock"):
        print("Player has won")
else:
        print("Computer has won")