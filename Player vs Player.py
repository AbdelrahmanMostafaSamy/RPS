import time

playerOne = input("What do you want Player1 to be called? ")
playerTwo = input("What do you want Player2 to be called? ")

def playagain():
	time.sleep(1.3)
	if input("Do you want to play again? (Yes/No or Y/N)").lower() == "yes" or "y":
		start_game()


def start_game():
	playerOneChoice = input(f"{playerOne}, Please choose Rock, Paper or Scissors (Or Alternatively you can enter R, P, or S)").lower()

	while playerOneChoice not in ["rock", "paper", "scissors", "r", "p", "s"]:
	    playerOneChoice = input(f"{playerOne}, Please choose Rock, Paper or Scissors (Or Alternatively you can enter R, P, or S)").lower()


	playerTwoChoice = input(f"{playerTwo}, Please choose Rock, Paper or Scissors (Or Alternatively you can enter R, P, or S)").lower()

	while playerTwoChoice not in ["rock", "paper", "scissors", "r", "p", "s"]:
	    playerTwoChoice = input(f"{playerTwo}, Please choose Rock, Paper or Scissors (Or Alternatively you can enter R, P, or S)").lower()
    #=======================================
	print("Checking for winner..")
	time.sleep(1)
    #=======================================
    #Checks for checking for winner
	if playerOneChoice == playerTwoChoice:
		print("It's a Draw")
		playagain()	

	elif playerOneChoice == "rock" or "r":
		if playerTwoChoice == "paper" or "p":
			print(f"{playerTwo} wins!")
			playagain()
		elif playerTwoChoice == "scissors" or "s":
			print(f"{playerOne} wins!")
			playagain()
	elif playerOneChoice == "paper" or "p":
		if playerTwoChoice == "rock" or "r":
			print(f"{playerOne} wins!")
			playagain()
		elif playerTwoChoice == "scissors" or "s":
			print(f"{playerTwo} wins!")
			playagain()
	elif playerOneChoice == "scissors" or "s":
		if playerTwoChoice == "rock" or "r":
			print(f"{playerTwo} wins!")
			playagain()
		elif playerTwoChoice == "paper" or "p":
			print(f"{playerOne} wins!")
			playagain()
start_game()
