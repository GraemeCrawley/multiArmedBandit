# Reources:
# http://slivkins.com/work/MAB-book.pdf
# https://pdfs.semanticscholar.org/aa32/c33e7c832e76040edc85e8922423b1a1db77.pdf
# https://en.wikipedia.org/wiki/Multi-armed_bandit
# https://www.cs.mcgill.ca/~vkules/bandits.pdf


import random
import math
from random import gauss
import matplotlib.pyplot as plt
import sys, os


#Used to disable and enable printing for specific code blocks
#https://stackoverflow.com/questions/8391411/suppress-calls-to-print-python
# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


#turn the printing and plotting on/off
printing = False
plotting = False

if(printing == False):
	blockPrint()

#number of options
armLength = 5

#Epsilon value
epsilon = 0.01

#bound on error
boundOnError = 0.001



# variances of each arm, randomized between 0 and 0.1
# used to generate random output
variances = []
for i in range(armLength):
	variances.append(random.uniform(0.00, 0.10)**2)



# expected values of each arm in pdf, randomized between 0 and 100
# used to generate random output
expectedValues = []
for i in range(armLength):
	expectedValues.append(random.uniform(0, 100))

# used to track when the average value of an arm falls 
# within a confidence imterval
withinIntervalTimestep = []
for i in range(armLength):
	withinIntervalTimestep.append(0)


#Initializing values of each arm to be randomized
armRandomValue = [0,0,0,0,0]

#Average values of each arm
uHat = [0,0,0,0,0]

#tracking how many times each arm has been chosen
uTimesChosen = [0,0,0,0,0]

#initializing the total expected regret
expectedRegret = 0

#initializing the regret list to plot
expectedRegretList = []


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

	#expected regret
	expectedRegret = (t)*epsilon*(maxArmValue - (sum(uHat)/armLength))
	expectedRegretList.append(expectedRegret)

	#calculate time it takes to get within a vertain interval of the expected value
	if(abs(uHat[chosenArmI] - expectedValues[chosenArmI]) > boundOnError and withinIntervalTimestep[chosenArmI] == 0):
		withinIntervalTimestep[chosenArmI] = t



plt.plot(expectedRegretList)
plt.ylabel('regret')
plt.xlabel('turn')
if(plotting):
	plt.show()

for i in range(armLength):
	print("\nArm " + str(i) + ":")
	print("Original Value: " + str(expectedValues[i]))
	print("Original Variance: " + str(variances[i]))
	print("Final average: " + str(uHat[i]))
	print("Steps to get within CI: " + str(withinIntervalTimestep[i]))


