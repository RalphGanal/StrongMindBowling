class Shot:
	def __init__(self, pinsKnocked):
		self._pinsKnocked = pinsKnocked;
		self.observers = []

	@property
	def pinsKnocked(self):
		return self._pinsKnocked

	@pinsKnocked.setter
	def pinsKnocked(self, value):
		self._pinsKnocked = value

		for callback in self.observers:
			callback()
			
	def bindTo(self, callback):
		self.observers.append(callback)
	
	@staticmethod
	def isValidPins(pinsKnocked):
		if not isinstance(pinsKnocked, int):
			print("Invalid Shot, # of pins knocked must be an integer")
			return False
		elif pinsKnocked > 10:
			print("Invalid Shot, # of pins knocked cannot be greater than 10")
			return False
		elif pinsKnocked < 0:
			print("Invalid Shot, # of pins knocked cannot be less than 0")
			return False
		else:
			return True

class ShotFactory:
	@staticmethod
	def createShot(pinsKnocked):
		if Shot.isValidPins(pinsKnocked):
			return Shot(pinsKnocked)
		else:
			return None