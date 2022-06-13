import frame
import math

class Game:
	def __init__(self, gameName):
		self.gameName = gameName
		self.frames = []

		for i in range(0, 10):
			self.frames.append(frame.Frame(self, i))

	def runGame(self):
		x = 1

	def drawScoreBoard(self):
		lines = ["","","","","",""]
		
		
	def printFrame(self, frameNum):
		currFrame= self.frames[frameNum]
		shotsList = currFrame.shots
		numShots = len(shotsList)

		frameScore = self.calcTotalScore(frameNum)

		print("Frame", frameNum)
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
			thirdScore = "0"
			if shotsList[2].pinsKnocked == 10:
				thirdScore = "X"
			else:
				thirdScore =  str(shotsList[2].pinsKnocked)


			print("===============")
			if currFrame.isStrike:
				print("|| X | - | "+thirdScore+" ||")
			elif currFrame.isSpare:
				print("|| " + str(shotsList[0].pinsKnocked) + " | - | "+thirdScore+" ||")
			else:
				print("|| " + str(shotsList[0].pinsKnocked) + " | " + str(shotsList[1].pinsKnocked) + " | " + thirdScore + " ||")

			print("||   --------||")
			print("||       "  + str(frameScore) + " ||")
			print("===============")

	def getStrikeBonusShots(self, frameNum):
		if frameNum != 9:
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
