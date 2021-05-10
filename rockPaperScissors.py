import random

play = "Y"
options = ("R", "P", "S")
while play == "Y":
    computerChoice = options[random.randint(0, 2)]
    userChoice = input("Enter r for rock, p for paper and s for scissors: ").upper()
    if (userChoice == "R" and computerChoice == "S") or (userChoice == "P" and computerChoice == "R") or \
            (userChoice == "S" and computerChoice == "P"):
        print("Congrats! You won")
    elif userChoice == computerChoice:
        print("Tie Game")
    else:
        print("You have lost the game!")
    play = input("Do you want to play again? (y/n): ").upper()
