import random
dist = [0,0,0,0,0]

armLength = 5
maxArmValue = 0
maxArmI = 0

#Epsilon value
epsilon = 0.01

#5 expected values for 5 arms
uHat = [0,0,0,0,0]

#Initializing 5 probabilities for 5 arms
#The probability of picking each arm is each item
p = [0,0,0,0,0]


#all turns
for t in range(100):
	#random value to choose which arm to select:
	randomValue = random.uniform(0,1)

	#find the maximum empirical mean
	for i in uHat:
		if uHat[i] > maxArmValue:
			maxArmValue = maxArmValue[i]
			maxArmI = i
		else:
			continue

	if(randomValue > epsilon):
		#select the arm with the highest empirical mean
	else:
		randomArmChoice = random.randint(0,armLength-1)



	#update the expected value every turn
	for i in uHat:
		#some way to update uHat



