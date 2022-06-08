import random
import time

#Here we can see an implementation of the alg defined in the notes.txt file

#the simple pair mapping is provided below 
# 0->10
# 1->20
# 2->30
# 3->40
# 4->50
def getType(sock):
	return int((sock/10)-1)

# make a shuffled list of elems 
types = [10,20,30,40,50]
shuffled = []
for i in range(10000):
	for t in types:
		shuffled.append(t)


random.shuffle(shuffled)

#sort it into pairs
matchedPairs = []
buffer = [None] * 5
start = time.time()
for sock in shuffled:
	sockType = getType(sock)
	if buffer[sockType] == None:
		buffer[sockType] = sock
	else:
		matchedPairs.append((sock, buffer[sockType]))
		buffer[sockType] 

end = time.time()

print("sort time:", end - start) 

# iterate over result, check for errors
for pair in matchedPairs:
	pairSum = pair[0] - pair[1]
	if pairSum != 0:
		print(pair)


print("done")

