from shot import ShotFactory

class Frame:
	def __init__(self, game, frameNum, prevFrame):
		self.game = game
		self.frameNum = frameNum
		self.score = 0
		self.isStrike = False
		self.isSpare = False

		self.shots = []
		self.observers = []

		self.shots.append(ShotFactory.createShot(0))
		self.shots.append(ShotFactory.createShot(0))
		if frameNum == 9:
			self.shots.append(ShotFactory.createShot(0))

		self.prevFrame = prevFrame

	def calculateScore(self):
		#print("Calculating score of ", self.frameNum)
		if self.shots[0].pinsKnocked == 10: #If first shot hit 10 then strike
			self.isStrike = True
			self.calculateStrike()
		elif self.sumOfShots() == 10:
			self.isSpare = True
			self.calculateSpare()
		else:
			self.isStrike = False
			self.isSpare = False
			self.score = self.sumOfShots()

	def calculateStrike(self):
		self.score = self.sumOfShots() + self.game.getStrikeBonus(self.frameNum)

	def calculateSpare(self):
		self.score = self.sumOfShots() + self.game.getSpareBonus(self.frameNum)

	def sumOfShots(self):
		total = 0
		for i in self.shots:
			total += i.pinsKnocked

		return total

	def modifyShot(self, shotNum, pinsKnocked):
		print("Modifying shot", shotNum)
		if self.isValidShot(shotNum, pinsKnocked):
			self.shots[shotNum].pinsKnocked = pinsKnocked
			self.calculateScore()

	def isValidShot(self, shotNum, pinsKnocked):
		if self.frameNum != 9:
			newSum = self.sumOfShots() - self.shots[shotNum].pinsKnocked + pinsKnocked

			if newSum > 10:
				print("ERROR: Total pins knocked cannot be more than 10")
				return False
			elif self.shots[0] == 10 and shotNum != 0:
				print("ERROR: This frame is already a strike")
				return False
			else:
				return True
		else:
			if shotNum == 2 and self.sumOfShots() < 10:
				print("ERROR: You do not have any extra shots to play")
				return False
			else:
				return True
