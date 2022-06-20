import game
import frame
from shot import Shot
from shot import ShotFactory

gameInstance = game.Game(1)
sampleFrame = gameInstance.frames[0]

testValues = [0, 5, -10, 17, "Words", 1.4]
expectedResult = [1, 1, 0, 0, 0 ,0]

counter = 0

for i in testValues:
	shot = ShotFactory.createShot(i)
	if shot:
		print("Shot knocked " + str(shot.pinsKnocked) + " pins over")
		if expectedResult[counter]:
			print("GOOD RESULT")
		else:
			print("TEST FAILURE")
	else:
		if expectedResult[counter]:
			print("TEST FAILURE")
		else:
			print("GOOD RESULT")
		
	counter += 1