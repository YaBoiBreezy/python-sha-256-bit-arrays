#First attempt to break SHA-256 by making an A* search algorithm:
#While not done:
#  Take best value
#  For each bit in value:
#    Flip bit, hash new value, compare to goal, sort into list
#Conclusion: This does not tend towards goal, due to SHA-256 
#avalanche effect being good. No better than random guessing.

import random
import hashlib
import binascii

def eval(curr,goal):
	score=0
	for i in range(256):
		score+=(curr[i]==goal[i])
	return score

def runHash(input):
	hexstr = "{0:0>4X}".format(int(input,2))
	if len(hexstr)==128:
		data = binascii.a2b_hex(hexstr)
		output = hashlib.sha256(data).hexdigest()
		formatOutput=(bin(int(output,16))[2:]).zfill(256)
		return formatOutput
	return 0

world=[]
for x in range (256):
	world.append({})
old={}
goal='0'*256
highest=0
globalHighest=0
generation=0

for y in range(500):
	first=''
	for x in range(512):
		first+=str(random.randint(0,1))
	firstHashed=runHash(first)
	if(firstHashed):
		world[eval(firstHashed,goal)][first]=True

while highest<255:
	generation+=1
	while len(world[highest])==0:
		highest-=1
	newVal=list(world[highest].keys())[0]
	world[highest].pop(newVal)
	old[newVal]=True
	for x in range(512):
		newVal= newVal[:x]+('0' if newVal[x]=='1' else '1')+newVal[x+1:]
		newValHashed=runHash(newVal)
		if not newValHashed:
			continue
		score=eval(newValHashed,goal)
		if (not (newVal in world[score] or newVal in old)) and score>highest-5: #set to highest
			world[score][newVal]=True
			highest=max(highest,score)
			globalHighest=max(globalHighest,highest)
		newVal= newVal[:x]+('0' if newVal[x]=='1' else '1')+newVal[x+1:]
	if generation%100==0:
		print('GENERATION '+str(generation)+'  CURRENT BEST: '+str(globalHighest)+'  CURRENT: '+str(highest))
print(list(world[highest].keys())[0])