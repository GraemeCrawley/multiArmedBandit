import random

armLength = 5


#Epsilon value
epsilon = 0.01

#Values of u to be randomized
u = [0,0,0,0,0]

#Average values of u
uHat = [0,0,0,0,0]



#all turns
for t in range(10):
	maxArmValue = 0
	maxArmI = 0
	chosenArm = 0
	chosenArmI = 0
	#update the expected values of each arm, randomly
	print("Randomizing arms: \n")
	for i in range(armLength):
		u[i] = random.uniform(0,100)
		print("Arm " + str(i) + " random value: " + str(u[i]) + "\n")

	#Toss a coin
	#random value to choose which arm to select:
	randomValue = random.uniform(0,1)
	print("Coin toss: " + str(randomValue) + "\n")

	#find the maximum empirical mean
	print("Finding the maximum average value: \n")
	for i in range(armLength):
		if uHat[i] > maxArmValue:
			maxArmValue = uHat[i]
			maxArmI = i
		else:
			continue
	print("Current max average arm is arm " + str(maxArmI) + " with value " + str(maxArmValue) + "\n")

	print("Choosing based on coin toss: \n")
	#Use epsilon to choose either a random arm or the currently best arm
	if(randomValue > epsilon):
		print("Chosen current best arm: \n")
		#Choose the currently best arm
		chosenArm = u[maxArmI]
		chosenArmI = maxArmI
	else:
		print("Chosen random arm: \n")
		#choose a random arm
		randomArmChoice = random.randint(0,armLength-1)
		chosenArm = u[randomArmChoice]
		chosenArmI = randomArmChoice
	print("Chosen arm is arm " + str(chosenArmI) + "\n")

	uHat[chosenArmI] = (uHat[chosenArmI]*(t) + chosenArm)/(t+1)

	print("Updated average value for arm " + str(chosenArmI) + " to be " + str(uHat[chosenArmI]))
