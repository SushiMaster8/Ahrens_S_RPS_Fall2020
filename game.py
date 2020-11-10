# import packages to extend python (just like we extend sublime, or Atom, or VSCode)
from random import randint

# [] => this is an array. an array is a special type of container that can hold multiple items
#arrays are indexed (their contents get assigned a number)
# the index starts at 0
choices = ["rock", "paper", "scissors"]

player = input("choose rock, paper, or scissors: ")

# this will be the AI choice -> a random pick from the choices array
computer = choices[randint(0, 2)]

#check to see what the user input

# print outputs whatever is in the round brackets -> in this case it outputs player to the command print window
print("user chose: " + player)

#validate that the random choice worked for AI
print("AI chose: " + computer)

if (computer == player): 
	print("tie")

elif (computer == "rock"):
	if (player =="scissors"):
		print("YOU LOSE, HOLD THIS L CLOWN!")
	if (player =="paper"):
		print("OK FINE YOU WIN... PLAY ME AGAIN SEE WHAT HAPPENS")
