from lipo import GlobalOptimizer
import random
import time
random.seed()
from SHA_256_PROBABILISTIC import hash
from SHA_256_PROBABILISTIC import plus
import nlopt
from numpy import *


#opt = nlopt.opt(nlopt.GN_ISRES, 64) #BAD
#opt = nlopt.opt(nlopt.LD_CCSAQ, 64) #BAD
#opt = nlopt.opt(nlopt.GN_CRS2_LM, 64) #MEH
#opt = nlopt.opt(nlopt.GN_ESCH, 64) #MEH
#opt = nlopt.opt(nlopt.LN_COBYLA, 64) #OKAY
#opt = nlopt.opt(nlopt.LN_BOBYQA, 64) #VERY GOOD, BUT CRASHES
#opt = nlopt.opt(nlopt.LN_SBPLX, 64) #VERY GOOD

def objective(x, grad):
    goal=[0,1,1,0,0,0,1,1,1,1,0,0,0,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,0,0,0,1]
    curr=plus(plus(plus(x[:32],x[32:64]),x[64:96]),x[96:128])
    Ascore=0
    for i in range(32):
        Ascore+=abs(curr[i]-goal[i])
    return Ascore
print('LN_COBYLA')
for difficulty in range (16,-1,-1):
    t0=time.time()
    for attempt in range (10):
        opt = nlopt.opt(nlopt.LN_COBYLA, 128)
        opt.set_lower_bounds(0.0)
        opt.set_upper_bounds(1.0)
        opt.set_min_objective(objective)
        opt.set_stopval(difficulty)
        xmin=[]
        for x in range(128):
            xmin.append(random.random())
        xGood=opt.optimize(xmin)
    t1=time.time()
    print(str(difficulty)+': '+str((t1-t0)/10))








