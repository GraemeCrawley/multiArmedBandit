import random
dist = [0,0,0,0,0]

var = [0.1^2,0.01^2,0.05^2,0.03^2,0.08^2]
p = [0,0,0,0,0,0,0,0,0,0]

maxExp = 0

comment: all turns
for t in range(100):
	exp = [1,1,1,1,1]
	for i in exp:
		exp[i] = random.uniform(0,1)

	comment: find the maximum expected value
	for i in exp:
		if i > maxExp:
			maxExp = i
		else:
			continue

