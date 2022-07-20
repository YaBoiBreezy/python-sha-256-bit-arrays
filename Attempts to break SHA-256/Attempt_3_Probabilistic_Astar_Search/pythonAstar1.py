import random
from SHA_256_PROBABILISTIC import hash
from SHA_256_PROBABILISTIC import plus

def eval(curr,goal,overall):
	Ascore=0
	for i in range(32):
		Ascore+=abs(curr[i]-goal[i])
	for i in range(len(overall)):
		Ascore+=abs(-1*((2*overall[i]-1)**2)+1)*0.1
	return Ascore

score=999999
generation=0
step=0.1
goal=[0,1,1,0,0,0,0,0,1,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,1,1,1,0,1,0,0,0]
curr=[]
for x in range(128):
	curr.append(random.randint(0,10)/10)

while score>14:
	generation+=1
	best=[0,0]
	bestScore=5000
	for x in range(128):
		if curr[x]!=0 and curr[x]!=1:
			curr[x]=min(curr[x]+step,1)
			score=eval(plus(plus(plus(curr[:32],curr[32:64]),curr[64:96]),curr[96:]),goal,curr)
			if score<bestScore:
				bestScore=score
				best=[x,1]
			curr[x]-=step
			curr[x]=max(curr[x]-step,0)
			score=eval(plus(plus(plus(curr[:32],curr[32:64]),curr[64:96]),curr[96:]),goal,curr)
			if score<bestScore:
				bestScore=score
				best=[x,-1]
			curr[x]+=step
	if best[1]==1:
		curr[best[0]]=min(curr[x]+step,1)
	else:
		curr[best[0]]=max(curr[x]-step,0)
	print(best)
	print(curr[:5])
	if generation%100==0:
		print('GENERATION '+str(generation)+'  CURRENT: '+str(bestScore))
		print(curr)
print(plus(plus(plus(curr[:32],curr[32:64]),curr[64:96]),curr[96:]))
print(goal)