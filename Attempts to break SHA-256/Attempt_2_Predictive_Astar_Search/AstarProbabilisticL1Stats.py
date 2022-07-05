#These A* searches weren't performing well, so this tracks their progress. 
#As can be seen from running this program (Basically L1 with extra data logging),
#The average searched value "newVal" has score 128, aka exactly 50%, aka equal to 
#random guessing, despite the expected average (based on the predictive data) being 153. 
#This proves my entire method is faulty. Again. Sad

import random
import hashlib
import binascii
import json

def evalScore(one,two):
    score=0
    for i in range(256):
        score+=(one[i]==two[i])
    return score

def evalDiff(one,two):
    bitEval=[]
    for i in range(256):
        bitEval.append(int(one[i]!=two[i]))
    return bitEval

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
    world.append([])
taken={}
goal='0'*256
highest=0
globalHighest=0
generation=0
totalScore=0
expectedTotalScore=0

for y in range(5):
    first=''
    for x in range(512):
        first+=str(random.randint(0,1))
    firstHashed=runHash(first)
    if(firstHashed):
        world[evalScore(firstHashed,goal)].append(first)

with open('./json_data.json', 'r') as f:
    data = json.load(f)

while globalHighest<255:
    generation+=1
    while len(world[highest])==0:
        highest-=1
    newVal=world[highest].pop(0)

    newValHashed=runHash(newVal)
    if not newValHashed:
        continue
    score=evalScore(newValHashed,goal)
    totalScore+=score
    expectedTotalScore+=highest
    globalHighest=max(globalHighest,score)
    bitEval=evalDiff(newValHashed,goal)

    for y in range(512):
        expected=data[0][y]
        expectedScore=evalScore(bitEval,expected)
        newVal=newVal[:y]+('0' if newVal[y]=='1' else '1')+newVal[y+1:]
        if (not newVal in taken) and expectedScore>highest-20:
            world[expectedScore].append(newVal)
            highest=max(highest,expectedScore)
            taken[newVal]=True
        newVal=newVal[:y]+('0' if newVal[y]=='1' else '1')+newVal[y+1:]

     #   for x in range(y):
     #       expected=data[1][y][x][int(newVal[y]!=newVal[x])]
     #       expectedScore=evalScore(bitEval,expected)
     #       newVal=newVal[:x]+('0' if newVal[x]=='1' else '1')+newVal[x+1:y]+('0' if newVal[y]=='1' else '1')+newVal[y+1:]
     #       if (not newVal in taken) and expectedScore>highest-5:
     #           world[expectedScore].append(newVal)
     #           highest=max(highest,expectedScore)
     #           taken[newVal]=True
     #       newVal=newVal[:x]+('0' if newVal[x]=='1' else '1')+newVal[x+1:y]+('0' if newVal[y]=='1' else '1')+newVal[y+1:]

    if generation%100==0:
        print('GENERATION '+str(generation)+'  CURRENT BEST: '+str(globalHighest)+'  CURRENT: '+str(score)+'  avgScore: '+'{:11.8f}'.format(totalScore/generation)+'  expectedAvgScore: '+'{:11.8f}'.format(expectedTotalScore/generation))
print(newVal)
print(newValHashed)
