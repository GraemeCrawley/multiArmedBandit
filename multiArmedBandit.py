import random

armLength = 5


#Epsilon value
epsilon = 0.1

#Values of u to be randomized
u = [0,0,0,0,0]

#Average values of u
uHat = [0,0,0,0,0]

uTimesChosen = [0,0,0,0,0]




#all turns
for t in range(1000):
	#space = raw_input("Press any key to step through")
	print("\n\n\n\nRound " + str(t))

	#initializing values
	maxArmValue = 0
	maxArmI = 0
	chosenArmValue = 0
	chosenArmI = 0
	#update the expected values of each arm, randomly
	print("Randomizing arms:")
	for i in range(armLength):
		u[i] = random.uniform(0,100)
		print("Arm " + str(i) + " random value: " + str(u[i]))

	#Toss a coin
	#random value to choose which arm to select:
	randomValue = random.uniform(0,1)
	print("\nCoin toss: " + str(randomValue))

	#find the maximum empirical mean
	print("Finding the maximum average value:")
	for i in range(armLength):
		print("Average value for arm " + str(i) + " is " + str(uHat[i]))
		if uHat[i] > maxArmValue:
			maxArmValue = uHat[i]
			maxArmI = i
		else:
			continue
	print("Current max average arm is arm " + str(maxArmI) + " with value " + str(maxArmValue) + "\n")

	print("Choosing based on coin toss")
	#Use epsilon to choose either a random arm or the currently best arm. Also randomizes on the first round
	if(randomValue > epsilon) and t != 0:
		print("Chosen current best arm")
		#Choose the currently best arm
		chosenArmValue = u[maxArmI]
		chosenArmI = maxArmI
		uTimesChosen[chosenArmI] += 1

	else:
		print("Chosen random arm")
		#choose a random arm
		randomArmChoice = random.randint(0,armLength-1)
		chosenArmValue = u[randomArmChoice]
		chosenArmI = randomArmChoice
		uTimesChosen[chosenArmI] += 1

	print("Chosen arm is arm " + str(chosenArmI))

	uHat[chosenArmI] = (uHat[chosenArmI]*(uTimesChosen[chosenArmI]-1) + chosenArmValue)/(uTimesChosen[chosenArmI])

	print("Updated average value for arm " + str(chosenArmI) + " to be " + str(uHat[chosenArmI]))
