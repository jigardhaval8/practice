'''
Basic Bitwise Operations
1. Set nth bit in integer
2. Clear nth bit in integer
3. Check if nth bit is set or clear in integer
4. Check which bits are set or clear in integer
5. Program specific value in range of bits (like 5-3) in integer
6. Flip bits
7. Swap value of two integer without using temp 
'''
class Solution:
    def MissingNumber(self,array,n):
        inputarray=array
        inputarray.sort()
        if(inputarray[len(inputarray)-1]!=n):
            return n
        elif(inputarray[0]!=1):
            return 1
        else:
            for i in range(0,len(inputarray)-1):
                if((inputarray[i+1]-inputarray[i])>1):
                    return inputarray[i+1]-1

def main():
    print("Hello World!")
    test=Solution()
    print(test.MissingNumber([2,3,4],4))

if __name__ == "__main__":
    main()