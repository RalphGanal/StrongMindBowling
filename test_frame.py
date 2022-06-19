import game
import frame
import shot
from shot import ShotFactory

currentGame = game.Game("Game 1")

testValues = [8, 2, 5, 4, 9, 0, 10, 0, 10, 0, 5, 5, 5, 3, 6, 3, 9, 1, 9, 1]
#Values to emulate Example shown in http://www.fryes4fun.com/Bowling/scoring.htm
#For testing frame only, skips actual game logic to be implemented later (ie shouldn't need 0s to space out Strikes)

frameCounter = 0
shotNum = 0
for i in range(len(testValues)):
	print("Frame # ", frameCounter, "Attempting to Add ", testValues[i])
	currentFrame = currentGame.frames[frameCounter]
	currentFrame.modifyShot(shotNum, testValues[i])
	shotNum += 1

	if i % 2 == 1:
		frameCounter += 1
		shotNum = 0

#Manually add a strike to finish out the bonus for last frame due to not having game logic here to decide a third input is needed
currentGame.frames[9].modifyShot(2, 10)

print("\n")

for i in range(0, 10):
	print("Total Score as of Frame ", i, ": ", str(currentGame.calcTotalScore(i)))
	
if currentGame.calcTotalScore(9) == 149:
	print("TEST SUCCESS")
else:
	print("TEST FAILURE")

currentGame.frames[6].shots[1].pinsKnocked = 4

for i in range(0, 10):
	print("Total Score as of Frame ", i, ": ", str(currentGame.calcTotalScore(i)))
	
if currentGame.calcTotalScore(9) == 150:
	print("TEST SUCCESS")
else:
	print("TEST FAILURE")