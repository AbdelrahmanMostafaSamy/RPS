import random
import time

def playagain():
    time.sleep(1.3)
    if input("Do you want to play again? (Yes/No or Y/N)").lower() == "yes" or "y":
        start_game()
def start_game():
    userchoice = input("Please choose rock, Paper or Scissors (Or Alternatively you can enter r, P, or S)").lower()

    if (userchoice == "rock") or (userchoice == "r"):
        userchoice = "rock"
    elif (userchoice == "paper") or (userchoice == "p"):
        userchoice = "paper"
    elif (userchoice == "scissors") or (userchoice == "s"):
        userchoice = "scissors"

    while userchoice not in ["rock", "paper", "scissors"]:
        userchoice = input("Please choose rock, Paper or Scissors (Or Alternatively you can enter r, P, or S)").lower()

        if (userchoice == "rock") or (userchoice == "r"):
            userchoice = "rock"
        elif (userchoice == "paper") or (userchoice == "p"):
            userchoice = "paper"
        elif (userchoice == "scissors") or (userchoice == "s"):
            userchoice = "scissors"

    print("Generating a random choice..")
    time.sleep(1)
    computerchoice = random.choice(["rock", "paper", "scissors"])
    #=======================================
    print("Checking winner..")
    time.sleep(1)
    #=======================================
    #Checks for checking for winner
    if userchoice == computerchoice:
        print("It's a Draw")
        playagain()

    elif userchoice == "rock":
        if computerchoice == "paper":
            print("The Computer wins!")
            playagain()
        elif computerchoice == "scissors":
            print("The User wins!")
            playagain()

    elif userchoice == "paper":
        if computerchoice == "rock":
            print("The User wins!")
            playagain()
        elif computerchoice == "scissors":
            print("The Computer wins!")
            playagain()

    elif userchoice == "scissors":
        if computerchoice == "rock":
            print("The Computer wins!")
            playagain()
        elif computerchoice == "paper":
            print("The User wins!")
            playagain()
start_game()
