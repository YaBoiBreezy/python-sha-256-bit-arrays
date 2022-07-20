from lipo import GlobalOptimizer
import random
random.seed()
from SHA_256_PROBABILISTIC import hash
from SHA_256_PROBABILISTIC import plus
import nlopt
from numpy import *

def objective(x, grad):
    goal=[0,1,1,0,0,0,1,1,1,1,0,0,0,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,0,0,0,1]
    curr=plus(x[:32],x[32:])
    Ascore=0
    for i in range(32):
        Ascore+=abs(curr[i]-goal[i])
    return Ascore

#opt = nlopt.opt(nlopt.GN_CRS2_LM, 64)
#opt = nlopt.opt(nlopt.GN_ISRES, 64)
#opt = nlopt.opt(nlopt.GN_ESCH, 64) #GOOD
#opt = nlopt.opt(nlopt.LN_COBYLA, 64) #GOOD
#opt = nlopt.opt(nlopt.LN_BOBYQA, 64) #GOOD
#opt = nlopt.opt(nlopt.LN_SBPLX, 64) #GOOD
opt = nlopt.opt(nlopt.LD_CCSAQ, 64) #GOOD
opt.set_lower_bounds(0.0)
opt.set_upper_bounds(1.0)
opt.set_min_objective(objective)
opt.set_stopval(1)

xmin=[]
for x in range(64):
    xmin.append(random.random())

xGood=opt.optimize(xmin)

print(xGood)
print(opt.last_optimum_value())
print('\a')