import random
dist = [0,0,0,0,0]


maxExp = 0

#Epsilon value
epsilon = 0.01

#5 expected values for 5 arms
uHat = [0,0,0,0,0]

#5 Variances for 5 arms
var = [0.1^2,0.01^2,0.05^2,0.03^2,0.08^2]

#Initializing probabilities
p = [0,0,0,0,0,0,0,0,0,0]


#all turns
for t in range(100):
	#random value to choose which arm to select:
	randomValue = uniform.random(0,1)

	#find the maximum expected value
	for i in uHat:
		if i > maxExp:
			maxExp = uHat[i]
		else:
			continue


	if(randomValue > epsilon):
		#select the arm with the highest empirical probability
	else:
		#select a random arm



	#update the expected value every turn
	for i in uHat:
		#some way to update uHat



