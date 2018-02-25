# Reources:
# http://slivkins.com/work/MAB-book.pdf
# https://pdfs.semanticscholar.org/aa32/c33e7c832e76040edc85e8922423b1a1db77.pdf
# https://en.wikipedia.org/wiki/Multi-armed_bandit
# https://www.cs.mcgill.ca/~vkules/bandits.pdf


import random
import math
from random import gauss
import matplotlib.pyplot as plt

armLength = 5


#Epsilon value
epsilon = 0.005

#variances of each arm, used to generate random output
variances = [0.1**2, 0.01**2, 0.05**2, 0.08**2, 0.02**2]


#expected values of each arm in pdf, used to generate random output
expectedValues = [67, 65, 70, 52, 43]


#Initializing values of each arm to be randomized
armRandomValue = [0,0,0,0,0]

#Average values of each arm
uHat = [0,0,0,0,0]

#tracking how many times each arm has been chosen
uTimesChosen = [0,0,0,0,0]

#initializing the sum of the arm averages
sumOfAverages = 0

#initializing the total expected regret
regret = 0

#initializing the regret list to plot
regretList = []

#initilizing the list to track the means of each arm
uHatList = []

regretTotal = 0

#Iterate through turns
for t in range(1000):
	#space = raw_input("Press any key to step through")
	print("\n\n\n\nYou are on round " + str(t))

	#initializing values
	maxArmValue = 0
	maxArmI = 0
	chosenArmValue = 0
	chosenArmI = 0

	#update the expected values of each arm
	print("Randomizing arms:")
	for i in range(armLength):
		#randomizing using variances and expected means
		#https://stackoverflow.com/questions/8815706/random-number-with-specific-variance-in-python
		armRandomValue[i] = gauss(expectedValues[i], math.sqrt(variances[i]))
		print("Arm " + str(i) + " random value: " + str(armRandomValue[i]))

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
		chosenArmValue = armRandomValue[maxArmI]
		chosenArmI = maxArmI
		uTimesChosen[chosenArmI] += 1

	else:
		print("Chosen random arm")
		#choose a random arm
		randomArmChoice = random.randint(0,armLength-1)
		chosenArmValue = armRandomValue[randomArmChoice]
		chosenArmI = randomArmChoice
		uTimesChosen[chosenArmI] += 1

	print("Chosen arm  " + str(chosenArmI))

	# Set new average value of the chosen arm based on 
	# the new information (random value)
	uHat[chosenArmI] = (uHat[chosenArmI]*(uTimesChosen[chosenArmI]-1) + chosenArmValue)/(uTimesChosen[chosenArmI])
	print("Updated average value for arm " + str(chosenArmI) + " to be " + str(uHat[chosenArmI]))

	uHatList.append(uHat[chosenArmI])
	# # update the uHatList of averages to match either the current average for
	# # a non-selected arm, or the new average of the selected arm
	# for i in range(armLength):
	# 	if chosenArmI == i:
	# 		uHatList[i].append(uHat[chosenArmI])


	# regret of current round is equal to the number of rounds 
	# multiplied by the maximum average value of all arms, minus the 
	# sum of all averages for the currently chosen arm
	print(len(uHatList))
	print(t*maxArmValue)
	print(sum(uHatList))
	regret = (t)*maxArmValue - sum(uHatList)
	regretList.append(regret)

plt.plot(regretList)
plt.ylabel('regret')
plt.xlabel('turn')
plt.show()