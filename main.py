import game
import tkinter as tk

def createGame(gameName):
	return game.Game(gameName)

def loadGame(gameName):
	for game in games:
		if (game.gameName == gameName):
			return game

def printGames():
	counter = 0
	for game in games:
		counter += 1
		print(str(counter) + ") " + game.gameName)

isRunning = True
games = []

while isRunning:
	print("BOWLING")
	print("1) Start New Game")
	print("2) Load a Game")
	print("3) Exit")
	choice = input("Select an Option: ")
	
	if choice == '1':
		gameName = input("Enter New Game name: ")
		currentGame = createGame(gameName)
		games.append(currentGame)
		currentGame.runGame()
	elif choice == '2':
		printGames()
		gameName = input("Enter game name to load: ")
		currentGame = loadGame(gameName)

		if currentGame:
			currentGame.runGame()
	elif choice == '3':
		isRunning = False
	else:
		print("ERROR: Invalid Input, Try Again")

