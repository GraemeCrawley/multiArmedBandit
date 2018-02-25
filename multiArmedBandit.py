import random

armLength = 5


#Epsilon value
epsilon = 0.01

#5 expected values for 5 arms
uHat = [0,0,0,0,0]


#all turns
for t in range(100):
	maxArmValue = 0
	maxArmI = 0
	#update the expected values of each arm, randomly
	for i in uHat:
		uHat[i] = random.uniform(0,100)

	#Toss a coin
	#random value to choose which arm to select:
	randomValue = random.uniform(0,1)

	#find the maximum empirical mean
	for i in uHat:
		if uHat[i] > maxArmValue:
			maxArmValue = maxArmValue[i]
			maxArmI = i
		else:
			continue

	#Use epsilon to choose either a random arm or the currently best arm
	if(randomValue > epsilon):
		#Choose the currently best arm
		chosenArm = uHat[maxArmI]
	else:
		#choose a random arm
		randomArmChoice = random.randint(0,armLength-1)
		chosenArm = uHat[randomArmChoice]

	#do something with the chosen arm
	chosenArm


