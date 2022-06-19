from shot import ShotFactory

class Frame:
	def __init__(self, game, frameNum):
		self.game = game
		self.frameNum = frameNum
		self.score = 0
		self.isStrike = False
		self.isSpare = False
		
		self.shots = []
		self.observers = []

		shots.append(ShotFactory.createShot(0, self)])
		shots.append(ShotFactory.createShot(0, self)])
		if frameNum == 9:
			shots.append(ShotFactory.createShot(0, self)])

	def addShot(self, shot):
		if self.isValidShot(shot):
			self.shots.append(shot)
			self.calculateScore()

			shot.bindTo(self.calculateScore)
			for i in self.observers:
				i.callback()
		else:
			print("Shot invalid, shot was not added to frame")

	def calculateScore(self):
		if len(self.shots) > 0:
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
		else:
			self.score = 0

	def calculateStrike(self):
		for shot in self.game.getStrikeBonusShots(self.frameNum):
			shot.bindTo(self.calculateScore)

		self.score = self.sumOfShots() + self.game.getStrikeBonus(self.frameNum)

	def calculateSpare(self):
		shot = self.game.getSpareBonusShot(self.frameNum)
		
		if shot:
			shot.bindTo(self.calculateScore)

		self.score = self.sumOfShots() + self.game.getSpareBonus(self.frameNum)

	def sumOfShots(self):
		total = 0
		for i in self.shots:
			total += i.pinsKnocked

		return total

	def isValidShot(self, shot):
		if self.frameNum != 9:
			if sum([self.sumOfShots(), shot.pinsKnocked]) > 10:
				print("Total pins knocked cannot be more than 10")
				return False
			elif len(self.shots) >= 2:
				print("You cannot add more than 2 shots to a frame")
				return False
			elif len(self.shots) == 1:
				if self.shots[0] == 10:
					print("This frame is already a strike")
					return False
				else:
					return True
			else:
				return True
		else:
			if len(self.shots) == 2 and self.sumOfShots() < 10:
				print("You do not have any extra shots to play")
				return False
			else:
				return True

	def bindTo(self, callback):
		if callback not in self.observers:
			self.observers.append(callback)
			
	def modifyShot(self, shotNum, pinsKnocked)