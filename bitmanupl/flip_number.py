'''
Given a 32 bit number X, reverse its binary form and print the answer in decimal.
'''
class Solution:
    def reversedBits(self, X):
        inputnum=X
        resultnumber=0
        bitsetlist=[]
        resultlist=[]
        for i in range(0,32):
            if((inputnum>>i)&0x1==1):
                bitsetlist.append(i)
                resultlist.append(31-i)
        print(bitsetlist)
        print(resultlist)
        for j in range(0,len(resultlist)):
            resultnumber = resultnumber | 1<<resultlist[j]
        return resultnumber

def main():
    print("Hello World!")
    test=Solution()
    print(test.reversedBits(4294967295))

if __name__ == "__main__":
    main()