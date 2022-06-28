#this is the main file

#main function, takes array of size <= 512 of numbers 0 <= num <= 1
def generate_hash(input):
    
#basic rotation
def rightRotate(arr,dist):
    for x in range (32):
        hold=arr[(x+dist)%32]
        arr[(x+dist)%32]=arr[x%32]
        arr[x%32]=hold
    
#shift over, leave 0's in wake
def rightShift(arr,dist):
    
#invert every value
def noter(arr,dist):
    
#apply xor to every pair of bits
def xor(arr1,arr2):
    
#apply and to every pair of bits
def ander(arr1,arr2):
    
#binary addition, discard overflow
def plus(arr1,arr2):

if __name__ == "__main__":
    print(rightRotate([0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,1],2))
