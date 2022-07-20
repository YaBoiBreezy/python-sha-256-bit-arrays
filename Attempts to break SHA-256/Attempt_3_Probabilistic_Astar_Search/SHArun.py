from lipo import GlobalOptimizer
import random
import time
random.seed()
from SHA_256_PROBABILISTIC import hash
import nlopt
from numpy import *

def objective(x, grad):
    curr=hash(x,6)
    Ascore=0
    for i in range(256):
        Ascore+=curr[i]
    return Ascore

t0=time.time()
opt = nlopt.opt(nlopt.LN_SBPLX, 512)
opt.set_lower_bounds(0.0)
opt.set_upper_bounds(1.0)
opt.set_min_objective(objective)
opt.set_stopval(127)
xmin=[]
for x in range(512):
   xmin.append(random.random())
xGood=opt.optimize(xmin)
t1=time.time()
print(xGood)
print(hash(xGood,4))
print('best: '+str(opt.last_optimum_value()))
print('time: '+str(t1-t0))
