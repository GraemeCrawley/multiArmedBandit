import random
dist = [0,0,0,0,0]

var = [0.1^2,0.01^2,0.05^2,0.03^2,0.08^2]

maxExp = 0

epsilon = 0.1

#all turns
for t in range(100):
	uHat = [1,1,1,1,1]
	p = [0,0,0,0,0,0,0,0,0,0]

	for i in exp:
		exp[i] = random.uniform(0,1)


	#update the expected value every turn

	comment: find the maximum expected value
	for i in exp:
		if i > maxExp:
			maxExp = i
		else:
			continue

