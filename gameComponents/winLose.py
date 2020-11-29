from gameComponents import gameVars

#define a win/lose function and refer to it (invoke it) in our game loop
def winorlose(status):
	#print("called winorlose", status)

	if status == "won":
		pre_message = "THERE'S NO WAY YOU WON, WHAT, HOW? YOU MUST BE CHEATING! ADMIT IT YOU CHEATER! I NEVER LOSE!!!!!"
	else: 
		pre_message = "YOU LOST HAHAHAHAHA! YOU MUST BE SUCH A DISSAPOINTMENT TO YOUR FAMILY, PLAY ME AGAIN IF YOU FEEL LIKE LOSING!\n"
	
	print(pre_message + "WOULD YOU LIKE TO PLAY AGAIN?\n")

	choice = input("Y / N")

	if choice == "Y" or choice == "y":
		#reset the game and start over again
		gameVars.player_lives = 3
		gameVars.computer_lives = 3
		gameVars.player = False

	elif choice == "N" or choice == "n":
		# exit message and quit
		print("AWWWW, TOO TOUGH? DON'T WORRY I UNDERSTAND, GO CRY ALONE YOU SORRY EXCUSE FOR A HUMAN.")
		exit()
	else:
		print("DID I STUTTER??? -- TYPE Y or N")
		choice = input("Y / N")