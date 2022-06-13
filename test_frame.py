import game
import frame
import shot
from shot import ShotFactory

currentGame = game.Game("Game 1")

testValues = [8, 2, 5, 4, 9, 0, 10, 0, 10, 0, 5, 5, 5, 3, 6, 3, 9, 1, 9, 1]
#Values to emulate Example shown in http://www.fryes4fun.com/Bowling/scoring.htm
#For testing frame only, skips actual game logic to be implemented later (ie shouldn't need 0s to space out Strikes)

frameCounter = 0
for i in range(len(testValues)):
	print("Frame # ", frameCounter, "Attempting to Add ", testValues[i])
	currentFrame = currentGame.frames[frameCounter]
	currentFrame.addShot( ShotFactory.createShot(testValues[i], currentFrame))

	if i % 2 == 1:
		frameCounter += 1
		
	if i == len(testValues)-1:
		currentFrame.addShot(ShotFactory.createShot(10, currentFrame)) #A strike to finish out the bonus for last frame

print("\n")

for i in range(0, 11):
	print("Total Score as of Frame ", i, ": ", str(currentGame.calcTotalScore(i)))
	
if currentGame.calcTotalScore(i) == 149:
	print("TEST SUCCESS")