# import packages to extend python (just like we extend sublime, or Atom, or VSCode)
#from random import randint

#reimport our game variables
from gameComponents import gameVars, winLose, gameChoices

#set up our game loop
while gameVars.player is False:
	#this is the gameVars.player choice
	print("@@@@} THE GREAT ROCK PAPER SCISSORS SHOWDOWN {@@@@")
	print("@                                                @")
	print("@             Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives, "             @")
	print("@               Player Lives:", gameVars.player_lives, "/", gameVars.total_lives, "             @")		
	print("@                                                @")
	print("@  CHOOSE YOUR WEAPON! or type quit to exit      @")
	print("@                                                @")
	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
	gameVars.player = input("choose rock, paper, or scissors: \n")

	# if the player chooses to quit, then don't do anything else
	# just exit the process (kill python) and quit the game
	if gameVars.player == "quit":
		print("YOU QUIT? WOW, JUST LIKE EVERYTHING ELSE IN YOUR LIFE....")
		exit()

	# this will be the AI choice -> a random pick from the choices array
	#gameVars.computer = gameVars.choices[randint(0, 2)]

	

	# print outputs whatever is in the round brackets -> in this case it outputs gameVars.player to the command print window
	print("YOU CHOSE: " + gameVars.player)

	#validate that the random choice worked for AI
	#print("COMPUTER CHOSE: " + gameVars.computer)

	gameChoices.choices(gameVars.player)

	#check player lives and AI lives
	if gameVars.player_lives == 0:
		winLose.winorlose("lost")

	elif gameVars.computer_lives == 0:
		winLose.winorlose("won")

	else: 
		gameVars.player = False
