'''
Given a number N having only one ‘1’ and all other ’0’s in its binary representation, 
find position of the only set bit. If there are 0 or more than 1 set bit the answer should be -1. 
Position of  set bit '1' should be counted starting with 1 from LSB side in binary representation of the number.
'''
class Solution:
    def findPosition(self, N):
        numberof1=0
        positionof1=0
        for i in range(0,32):
            if(((N>>i)&0x1)==1):
                numberof1=numberof1+1
                positionof1=i
                if(numberof1>1):
                    return(-1)
        if(numberof1==0):
            return(-1)
        else:
            return(positionof1+1)

def main():
    test=Solution()
    print(test.findPosition(2))

if __name__ == "__main__":
    main()