import frame

class Game:
	def __init__(self, gameName):
		self.gameName = gameName
		self.frames = []

		for i in range(0, 11):
			self.frames.append(frame.Frame(self, i))
			
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
		for i in range(frameNum):
			self.frames[i].calculateScore()
			totalScore += self.frames[i].score

			#print("Calcing frame: ", i, " individual score", self.frames[i].score)
		
		return totalScore
