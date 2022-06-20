import frame
import math
from shot import ShotFactory

class Game:
	def __init__(self, gameName):
		self.gameName = gameName
		self.frames = []

		for i in range(0, 10):
			prevFrame = None
			
			if i > 0:
				prevFrame = self.frames[i-1]

			newFrame = frame.Frame(self, i, prevFrame)
			self.frames.append(newFrame)
			
			if prevFrame:
				prevFrame.nextFrame = newFrame

	def runGame(self):
		isRunning = True

		while (isRunning):
			print("\n")
			print("Bowling Game", self.gameName)
			self.drawScoreBoard()
			print("Enter a frame number to Modify that Frame")
			print("Or enter 'exit' to Close Game and go back to the Main Menu")
			choice = input("\tEnter Selection: ")
			
			if choice.lower() == 'exit':
				isRunning = False
			else:
				#try:
				choice = int(choice)-1
				self.modifyFrame(choice)
				#except:
				#	print("ERROR: Invalid Input for Frame")
				
	def getFrame(self, frameNum):
		return self.frames[frameNum]

	def modifyFrame(self, frameNum):
		isRunning = True

		while (isRunning):
			print("\n")
			self.printFrame(frameNum)
			
			choice = 0
			
			if frameNum != 9:
				choice = input("\tChange which shot? (1, 2 or 'cancel'): ")
			else:
				choice = input("\tChange which shot? (1, 2, 3 or 'cancel'): ")

			if choice.lower() == 'cancel':
				isRunning = False
			else:
				#print("Going to Modify Shot")
				choice = int(choice)-1
				
				if choice < len(self.frames[frameNum].shots):
					self.modifyShot(frameNum, choice)
				else:
					print("ERROR: Pick a valid shot to modify")

	def modifyShot(self, frameNum, shotNum):
		#print("In modify Shot")
		currentFrame = self.frames[int(frameNum)]
		currentShot = currentFrame.shots[shotNum-1]
		print("\n")
		print("\tCurrent Shot Value", currentShot.pinsKnocked)
		newPinsKnocked = input("\tReplace with: ")

		self.getFrame(frameNum).modifyShot(shotNum, int(newPinsKnocked))
		isRunning = False
		
	def addNewShot(self, frameNum):
		currentFrame = self.frames[int(frameNum)]
		pinsKnocked = int(input("Enter number of pins knocked down: "))
		newShot = ShotFactory.createShot(pinsKnocked, currentFrame)
		currentFrame.addShot(newShot)

	def drawScoreBoard(self):
		lines = ["","","","","",""]
		for frame in self.frames:
			self.printFrame(frame.frameNum)

	def getStrikeBonusShots(self, frameNum):
		if frameNum != 9 and frameNum != 8:
			nextFrame = self.frames[frameNum+1]
			nextNextFrame = self.frames[frameNum+2]
			
			if len(nextFrame.shots) > 0:
				if not nextFrame.isStrike:
					return nextFrame.shots
				elif len(nextNextFrame.shots) > 0:
					return [nextFrame.shots[0], nextNextFrame.shots[0]]
				else:
					return [nextFrame.shots[0]]
			else:
				return []
		

	def getStrikeBonus(self, frameNum):
		if frameNum != 9:
			nextFrame = self.frames[frameNum+1]
			nextNextFrame = self.frames[frameNum+2]

			if len(nextFrame.shots) > 0:
				if not nextFrame.isStrike:
					return nextFrame.sumOfShots()
				elif len(nextNextFrame.shots) > 0:
					return nextFrame.shots[0].pinsKnocked + nextNextFrame.shots[0].pinsKnocked
				else:
					return nextFrame.shots[0].pinsKnocked
			else:
				return 0

	def getSpareBonusShot(self, frameNum):
		if frameNum != 9:
			if len(self.frames[frameNum+1].shots) > 0:
				return self.frames[frameNum+1].shots[0]
			else:
				return []
		else:
			return []

	def getSpareBonus(self, frameNum):
		if frameNum != 9:
			if len(self.frames[frameNum+1].shots) > 0:
				return self.frames[frameNum+1].shots[0].pinsKnocked
			else:
				return 0
		else:
			return 0

	def calcTotalScore(self, frameNum):
		totalScore = 0
		for i in range(frameNum+1):
			self.frames[i].calculateScore()
			totalScore += self.frames[i].score

			#print("Calcing frame: ", i, " individual score", self.frames[i].score)
			#for shot in self.frames[i].shots:
			#	print("Shot score", shot.pinsKnocked)
		
		return totalScore
		
	def printFrame(self, frameNum):
		currFrame= self.frames[frameNum]
		shotsList = currFrame.shots
		numShots = len(shotsList)

		frameScore = self.calcTotalScore(frameNum)

		print("Frame", frameNum+1)
		if frameNum != 9:
			print("===========")
			if numShots == 0:
				print("||   |   ||")
				
			elif numShots == 1 or currFrame.isStrike:
				if currFrame.isStrike:
					print("|| X | - ||")
				else:
					print("|| " + str(shotsList[0].pinsKnocked) + " | - ||")
			elif numShots == 2:
				if currFrame.isSpare:
					print("|| " + str(shotsList[0].pinsKnocked) + " | / ||")
				else:
					print("|| " + str(shotsList[0].pinsKnocked) + " | " + str(shotsList[1].pinsKnocked) + " ||")
			print("||   ----||")
			if math.floor(frameScore / 100) > 0:
				print("||   "  + str(frameScore) + " ||")
				print("===========")
			elif math.floor(frameScore / 10) > 0:
				print("||    "  + str(frameScore) + " ||")
				print("===========")
			else:
				print("||     "  + str(frameScore) + " ||")
				print("===========")
		else:
			thirdScore = ""
			if numShots == 3:
				if shotsList[2].pinsKnocked == 10:
					thirdScore = "X"
				else:
					thirdScore =  str(shotsList[2].pinsKnocked)


			print("===============")
			if currFrame.isStrike:
				print("|| X | - | "+thirdScore+" ||")
			elif currFrame.isSpare:
				print("|| " + str(shotsList[0].pinsKnocked) + " | / | "+thirdScore+" ||")
			elif numShots >= 2:
				print("|| " + str(shotsList[0].pinsKnocked) + " | " + str(shotsList[1].pinsKnocked) + " | " + thirdScore + " ||")
			elif numShots == 1:
				print("|| " + str(shotsList[0].pinsKnocked) + " |   | " + thirdScore + " ||")
			else:
				print("||   |   |   ||")

			print("||   --------||")
			if math.floor(frameScore / 100) > 0:
				print("||       "  + str(frameScore) + " ||")
			elif math.floor(frameScore / 10) > 0:
				print("||        "  + str(frameScore) + " ||")
			else:
				print("||         "  + str(frameScore) + " ||")
			print("===============")