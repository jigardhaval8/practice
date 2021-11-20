'''
Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. 
Find the missing element.
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