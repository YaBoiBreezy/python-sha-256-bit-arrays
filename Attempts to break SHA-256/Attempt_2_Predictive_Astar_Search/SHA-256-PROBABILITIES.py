#SHA-256 basic, last 3 operation functions altered to handle probabilities instead of binaries (0.56=56% chance of being 1, 44% change of being 0)
#Main function generates diff of [0.5,...,0.5] arr with bit x being 0 and 1 respectively, then saves to json file
#Also has code for changing 2, 3 bits at a time. JSON file not included due to size.
#For use, run this file, then AstarProbabilisticL1 or L1Stats. Alternatively, uncomment the 2 part (NOT THE 3 PART) in main, lines 227-251, then you can run the L2 script after a couple hours
#WARNING: 2 bits takes 2 hours to run, 3 bits takes 30 days

import json

#main function, takes array of size 512 of numbers 0<=x<=1
def hash(inp):
    if len(inp)!=512:
        return 'BAD_LENGTH'
    input=[]
    for x in range(512):
        input.append(inp[x])
    for x in range(512):
        input[x]=int(input[x])
        if input[x]<0 or input[x]>1:
            return 'BAD_VALUE_AT_INDEX: '+str(x)
        
    K = [[0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,0,1,1,0,0,0],[0,1,1,1,0,0,0,1,0,0,1,1,0,1,1,1,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1],
         [1,0,1,1,0,1,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1],[1,1,1,0,1,0,0,1,1,0,1,1,0,1,0,1,1,1,0,1,1,0,1,1,1,0,1,0,0,1,0,1],
         [0,0,1,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,0,0,1,0,1,1,0,1,1],[0,1,0,1,1,0,0,1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,1],
         [1,0,0,1,0,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,0,1,1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,1,0,1,1,0,1,0,1,0,1],
         [1,1,0,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,1,0,1,0,1,0,1,0,0,1,1,0,0,0],[0,0,0,1,0,0,1,0,1,0,0,0,0,0,1,1,0,1,0,1,1,0,1,1,0,0,0,0,0,0,0,1],
         [0,0,1,0,0,1,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,1,1,0,1,1,1,1,1,0],[0,1,0,1,0,1,0,1,0,0,0,0,1,1,0,0,0,1,1,1,1,1,0,1,1,1,0,0,0,0,1,1],
         [0,1,1,1,0,0,1,0,1,0,1,1,1,1,1,0,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,0],[1,0,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,1,1,1,1,0],
         [1,0,0,1,1,0,1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,1,1,0,1,0,1,0,0,1,1,1],[1,1,0,0,0,0,0,1,1,0,0,1,1,0,1,1,1,1,1,1,0,0,0,1,0,1,1,1,0,1,0,0],
         [1,1,1,0,0,1,0,0,1,0,0,1,1,0,1,1,0,1,1,0,1,0,0,1,1,1,0,0,0,0,0,1],[1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1,0],
         [0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,1,1,1,0,1,1,1,0,0,0,1,1,0],[0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,1,1,1,0,0,1,1,0,0],
         [0,0,1,0,1,1,0,1,1,1,1,0,1,0,0,1,0,0,1,0,1,1,0,0,0,1,1,0,1,1,1,1],[0,1,0,0,1,0,1,0,0,1,1,1,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,1,0,1,0],
         [0,1,0,1,1,1,0,0,1,0,1,1,0,0,0,0,1,0,1,0,1,0,0,1,1,1,0,1,1,1,0,0],[0,1,1,1,0,1,1,0,1,1,1,1,1,0,0,1,1,0,0,0,1,0,0,0,1,1,0,1,1,0,1,0],
         [1,0,0,1,1,0,0,0,0,0,1,1,1,1,1,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0],[1,0,1,0,1,0,0,0,0,0,1,1,0,0,0,1,1,1,0,0,0,1,1,0,0,1,1,0,1,1,0,1],
         [1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0],[1,0,1,1,1,1,1,1,0,1,0,1,1,0,0,1,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1],
         [1,1,0,0,0,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,0,0,1,1],[1,1,0,1,0,1,0,1,1,0,1,0,0,1,1,1,1,0,0,1,0,0,0,1,0,1,0,0,0,1,1,1],
         [0,0,0,0,0,1,1,0,1,1,0,0,1,0,1,0,0,1,1,0,0,0,1,1,0,1,0,1,0,0,0,1],[0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,1,0,0,1,1,1],
         [0,0,1,0,0,1,1,1,1,0,1,1,0,1,1,1,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,1],[0,0,1,0,1,1,1,0,0,0,0,1,1,0,1,1,0,0,1,0,0,0,0,1,0,0,1,1,1,0,0,0],
         [0,1,0,0,1,1,0,1,0,0,1,0,1,1,0,0,0,1,1,0,1,1,0,1,1,1,1,1,1,1,0,0],[0,1,0,1,0,0,1,1,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,1,0,0,0,1,0,0,1,1],
         [0,1,1,0,0,1,0,1,0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,1,0,1,0,1,0,1,0,0],[0,1,1,1,0,1,1,0,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,1,1,0,1,1],
         [1,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,1,1,0,0,1,0,0,1,0,0,1,0,1,1,1,0],[1,0,0,1,0,0,1,0,0,1,1,1,0,0,1,0,0,0,1,0,1,1,0,0,1,0,0,0,0,1,0,1],
         [1,0,1,0,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,1,0,0,0,0,1],[1,0,1,0,1,0,0,0,0,0,0,1,1,0,1,0,0,1,1,0,0,1,1,0,0,1,0,0,1,0,1,1],
         [1,1,0,0,0,0,1,0,0,1,0,0,1,0,1,1,1,0,0,0,1,0,1,1,0,1,1,1,0,0,0,0],[1,1,0,0,0,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,0,1,1,0,1,0,0,0,1,1],
         [1,1,0,1,0,0,0,1,1,0,0,1,0,0,1,0,1,1,1,0,1,0,0,0,0,0,0,1,1,0,0,1],[1,1,0,1,0,1,1,0,1,0,0,1,1,0,0,1,0,0,0,0,0,1,1,0,0,0,1,0,0,1,0,0],
         [1,1,1,1,0,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,0,1,0,1,1,0,0,0,0,1,0,1],[0,0,0,1,0,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,1,1,1,0,0,0,0],
         [0,0,0,1,1,0,0,1,1,0,1,0,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,1,0,1,1,0],[0,0,0,1,1,1,1,0,0,0,1,1,0,1,1,1,0,1,1,0,1,1,0,0,0,0,0,0,1,0,0,0],
         [0,0,1,0,0,1,1,1,0,1,0,0,1,0,0,0,0,1,1,1,0,1,1,1,0,1,0,0,1,1,0,0],[0,0,1,1,0,1,0,0,1,0,1,1,0,0,0,0,1,0,1,1,1,1,0,0,1,0,1,1,0,1,0,1],
         [0,0,1,1,1,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1,1,0,0,1,0,1,1,0,0,1,1],[0,1,0,0,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0],
         [0,1,0,1,1,0,1,1,1,0,0,1,1,1,0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,1,1,1],[0,1,1,0,1,0,0,0,0,0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,0,0,1,1],
         [0,1,1,1,0,1,0,0,1,0,0,0,1,1,1,1,1,0,0,0,0,0,1,0,1,1,1,0,1,1,1,0],[0,1,1,1,1,0,0,0,1,0,1,0,0,1,0,1,0,1,1,0,0,0,1,1,0,1,1,0,1,1,1,1],
         [1,0,0,0,0,1,0,0,1,1,0,0,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,0,1,0,0],[1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0],
         [1,0,0,1,0,0,0,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0],[1,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,1,0,1,1,0,0,1,1,1,0,1,0,1,1],
         [1,0,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,0,1,0,0,0,1,1,1,1,1,1,0,1,1,1],[1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,1,0,1,1,1,1,0,0,0,1,1,1,1,0,0,1,0]]

    h0 = [0,1,1,0,1,0,1,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1,1,0,0,1,1,0,0,1,1,1]
    h1 = [1,0,1,1,1,0,1,1,0,1,1,0,0,1,1,1,1,0,1,0,1,1,1,0,1,0,0,0,0,1,0,1]
    h2 = [0,0,1,1,1,1,0,0,0,1,1,0,1,1,1,0,1,1,1,1,0,0,1,1,0,1,1,1,0,0,1,0]
    h3 = [1,0,1,0,0,1,0,1,0,1,0,0,1,1,1,1,1,1,1,1,0,1,0,1,0,0,1,1,1,0,1,0]
    h4 = [0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,0,0,1,0,0,1,1,1,1,1,1,1]
    h5 = [1,0,0,1,1,0,1,1,0,0,0,0,0,1,0,1,0,1,1,0,1,0,0,0,1,0,0,0,1,1,0,0]
    h6 = [0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1,1,0,0,1,1,0,1,0,1,0,1,1]
    h7 = [0,1,0,1,1,0,1,1,1,1,1,0,0,0,0,0,1,1,0,0,1,1,0,1,0,0,0,1,1,0,0,1]

    # Prepare message schedule
    W = []
    for i in range(0, 64):
        if i <= 15:
            W.append(input[i*32:(i*32)+32])
        else:
            s0=xor(xor(rightRotate(W[i-15],7),rightRotate(W[i-15],18)),rightShift(W[i-15],3))
            s1=xor(xor(rightRotate(W[i-2],17),rightRotate(W[i-2],19)),rightShift(W[i-2],10))
            W.append(plus(plus(plus(W[i-16],s0),W[i-7]),s1))

    a = h0
    b = h1
    c = h2
    d = h3
    e = h4
    f = h5
    g = h6
    h = h7

    for i in range(64):
        S1=xor(xor(rightRotate(e,6),rightRotate(e,11)),rightRotate(e,25))
        ch=xor(ander(e,f),ander(noter(e),g))
        temp1=plus(plus(plus(plus(h,S1),ch),K[i]),W[i])
        S0=xor(xor(rightRotate(a,2),rightRotate(a,13)),rightRotate(a,22))
        maj=xor(xor(ander(a,b),ander(a,c)),ander(b,c))
        temp2=plus(S0,maj) 
        h = g
        g = f
        f = e
        e = plus(d,temp1)
        d = c
        c = b
        b = a
        a = plus(temp1,temp2)

    h0 = plus(h0,a)
    h1 = plus(h1,b)
    h2 = plus(h2,c)
    h3 = plus(h3,d)
    h4 = plus(h4,e)
    h5 = plus(h5,f)
    h6 = plus(h6,g)
    h7 = plus(h7,h)
    return h0+h1+h2+h3+h4+h5+h6+h7
    
#basic rotation
def rightRotate(arr,dist):
    ret=[]
    for x in range (32):
        ret.append(arr[(x-dist)%32])
    return ret
    
#shift over, leave 0's in wake
def rightShift(arr,dist):
    ret=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for x in range (dist,32):
        ret[x]=arr[x-dist]
    return ret
    
#invert every value
def noter(arr):
    ret=[]
    for x in range (32):
        ret.append(1-arr[x])
    return ret
    
#apply probabilistic xor to every pair of bits
def xor(arr1,arr2):
    ret=[]
    for x in range (32):
        ret.append((arr1[x]*(1-arr2[x]))+((1-arr1[x])*arr2[x]))
    return ret
    
#apply probabilistic and to every pair of bits
def ander(arr1,arr2):
    ret=[]
    for x in range (32):
        ret.append(arr1[x]*arr2[x])
    return ret
    
#binary probabilistic addition, discard overflow
def plus(arr1,arr2):
    ret=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    carry=0
    for x in range(31, -1, -1):
        r = carry+arr1[x]+arr2[x]
        P1=(carry*(1-arr1[x])*(1-arr2[x]))+((1-carry)*arr1[x]*(1-arr2[x]))+((1-carry)*(1-arr1[x])*arr2[x])
        P2=(carry*arr1[x]*(1-arr2[x]))+(carry*(1-arr1[x])*arr2[x])+((1-carry)*arr1[x]*arr2[x])
        P3=carry*arr1[x]*arr2[x]
        ret[x] = P1+P3
        carry = P2+P3
    return ret

def run3(out,hold):
    for z in range(512):
        print('z='+str(z))
        for y in range(z):
            for x in range(y):
                hold[z]=0
                hold[y]=0
                hold[x]=0
                temp000=hash(hold)
                hold[z]=0
                hold[y]=0
                hold[x]=1
                temp001=hash(hold)
                hold[z]=0
                hold[y]=1
                hold[x]=0
                temp010=hash(hold)
                hold[z]=0
                hold[y]=1
                hold[x]=1
                temp011=hash(hold)
                hold[z]=1
                hold[y]=0
                hold[x]=0
                temp100=hash(hold)
                hold[z]=1
                hold[y]=0
                hold[x]=1
                temp101=hash(hold)
                hold[z]=1
                hold[y]=1
                hold[x]=0
                temp110=hash(hold)
                hold[z]=1
                hold[y]=1
                hold[x]=1
                temp111=hash(hold)
                hold[x]=0.5
                hold[y]=0.5
                hold[z]=0.5
                diff000=[]
                diff001=[]
                diff010=[]
                diff011=[]
                for j in range(256):
                    diff000.append(abs(temp111[j]-temp000[j]))
                    diff001.append(abs(temp110[j]-temp001[j]))
                    diff010.append(abs(temp101[j]-temp010[j]))
                    diff100.append(abs(temp100[j]-temp011[j]))
                out.append([[z,y,x],[0,0,0],diff000])
                out.append([[z,y,x],[0,0,1],diff001])
                out.append([[z,y,x],[0,1,0],diff010])
                out.append([[z,y,x],[0,1,1],diff011])
    print('done3')

if __name__ == "__main__":
    hold=[]
    for x in range(512):
        hold.append(0.5)
    out=[]
    for x in range(512):
        hold[x]=0
        temp0=hash(hold)
        hold[x]=1
        temp1=hash(hold)
        hold[x]=0.5
        diff0=[]
        for j in range(256):
            diff0.append(abs(temp1[j]-temp0[j]))
        out.append([[x],[0],diff0])
    print('done1')
  #  for y in range(512):
  #      print(y)
  #      for x in range(y):
  #          hold[y]=0
  #          hold[x]=0
  #          temp00=hash(hold)
  #          hold[y]=0
  #          hold[x]=1
  #          temp01=hash(hold)
  #          hold[y]=1
  #          hold[x]=0
  #          temp10=hash(hold)
  #          hold[y]=1
  #          hold[x]=1
  #          temp11=hash(hold)
  #          hold[x]=0.5
  #          hold[y]=0.5
  #          diff00=[]
  #          diff01=[]
  #          for j in range(256):
  #                      diff00.append(abs(temp11[j]-temp00[j]))
  #                      diff01.append(abs(temp10[j]-temp01[j]))
  #          out.append([[y,x],[0,0],diff00])
  #          out.append([[y,x],[0,1],diff01])
  #  print('done2')
  #  run3(out,hold)
    json_string=json.dumps(out)
    with open('json_data.json', 'w') as outfile:
        outfile.write(json_string)