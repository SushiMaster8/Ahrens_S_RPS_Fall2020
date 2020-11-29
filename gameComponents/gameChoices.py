from gameComponents import gameVars
from random import randint
#from game import computer

def choices(status):

	computer = gameVars.choices[randint(0, 2)]

	print("COMPUTER CHOSE: " + computer)

	if (computer == gameVars.player):
		print("tie")
	#Computer "Rock" clause
	elif (computer == "rock"):
		if (gameVars.player =="scissors"):
			gameVars.player_lives -= 1
			print("YOU LOSE, HOLD THIS L CLOWN!")
		else:
			print("OK FINE YOU WIN... PLAY ME AGAIN SEE WHAT HAPPENS")
			gameVars.computer_lives -= 1
			

	#Computer "Paper" clause
	elif (computer == "paper"):
		if (gameVars.player =="rock"):
			gameVars.player_lives -= 1
			print("YOU LOSE, HOLD THIS L CLOWN!")
		else:
			print("OK FINE YOU WIN... PLAY ME AGAIN SEE WHAT HAPPENS")
			gameVars.computer_lives -= 1

	#Computer "Scissors" clause
	elif (computer == "scissors"):
		if (gameVars.player =="paper"):
			gameVars.player_lives -= 1
			print("YOU LOSE, HOLD THIS L CLOWN!")
		else:
			print("OK FINE YOU WIN... PLAY ME AGAIN SEE WHAT HAPPENS")
			gameVars.computer_lives -= 1
