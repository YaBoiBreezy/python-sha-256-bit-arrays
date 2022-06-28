#this is the main file

#main function, takes array of size <= 512 of numbers 0 <= num <= 1
def generate_hash(input):
    
#basic rotation
def rightRotate(arr,dist):
    ret=[]
    for x in range (32):
        ret.append(arr[(x+dist)%32])
    return ret
    
#shift over, leave 0's in wake
def rightShift(arr,dist):
    ret=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for x in range (dist,32):
        ret[x]=arr[x-dist]
    return ret
    
#invert every value
def noter(arr,dist):
    ret=[]
    for x in range (32):
        ret.append(1-arr[x])
    return ret
    
#apply xor to every pair of bits
def xor(arr1,arr2):
    ret=[]
    for x in range (32):
        ret.append(1 if arr1[x]==arr2[x] else 0)
    return ret
    
#apply and to every pair of bits
def ander(arr1,arr2):
    ret=[]
    for x in range (32):
        ret.append(1 if arr1[x] and arr2[x] else 0)
    return ret
    
#binary addition, discard overflow
def plus(arr1,arr2):
    ret=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    carry=0
    for x in range(31, -1, -1):
        r = carry+arr1[x]+arr2[x]
        ret[x] = int(r%2==1)
        carry = int(r>=2)
    return ret

if __name__ == "__main__":
    print(rightRotate([0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,1],2))
    print(rightShift([1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,1],2))
    print(noter([1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,1],2))
    print(xor([1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,1],2))
    print(ander([1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,1],2))
    print(plus([1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,1],2))
