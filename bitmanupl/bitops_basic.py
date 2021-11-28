'''
Basic Bitwise Operations
1.Set & Clear nth bit in integer
2.Check if nth bit is set or clear in integer
3.Check which bits are set or clear in integer
4.Find value of specific range of bits(like 8:4) in int
5.Program specific value in range of bits (like 5-3) in int.
6.Flip Kth bit in number
7.Swap value of two integer without using temp 
'''
class Solution:
    '''
    1.Set & Clear nth bit in integer
    '''
    def setKthBit(self,number,K):
        result = number | (0x1<<K)
        return result
    def clearKthBit(self,number,K):
        result = number & ~(0x1<<K)
        return result
    '''
    Check if nth bit is set or clear in integer, return 1 if set return 0 if not
    '''
    def checkKthBit(self,number,K):
        result = number>>K & 0x1
        return result

    '''
    Checks which bit are set or cleared in given number, to find set bits operation is 1 and for
    clear bits operation is 0
    '''
    def checkSetnClearBits(self,number,operation):
        setbits=[]
        clearbits=[]
        for i in range(0,32):
            bitsts = (number>>i)&0x1
            if(bitsts==1):
                setbits.append(i)
            else:
                clearbits.append(i)
        if(operation==1):
            return setbits
        else:
            return clearbits


    '''
    Check value between start and end bits in number
    '''
    def checkvalueinint(self,number,startbit,endbit):
        result=0
        mask=0
        for i in range(startbit,endbit+1):
            mask=mask|(0x1<<i)
        result = (number&mask) >> startbit
        return result

    '''
    Program value between start and end bits in number
    '''
    def programvalueinint(self,number,startbit,endbit,wrvalue):
        result=0
        mask=0
        for i in range(startbit,endbit+1):
            mask=mask|(0x1<<i)
        # means bits in start to end bit will be 0
        modifynumber = number & ~(mask)
        # print(modifynumber)
        # print(bin(modifynumber))
        new_wr_val = wrvalue << startbit
        mask_with_Value=mask & (new_wr_val)
        result = (modifynumber) | mask_with_Value
        return result

    '''
    Flip Kth bit in number
    '''
    def flipKthBit(self,number,bitpos):
        result=number ^ (0x1<<bitpos)
        return result

    '''
    swao two numbers without using temp
    '''
    def swaptwonumbers(self,a,b):
        a=a^b
        b=a^b
        a=a^b
        return (a,b)

    '''
    Count No of set bits in number
    '''
    def noofsetbits(self,number):
        setbits=[]
        for i in range(0,32):
            bitsts = (number>>i)&0x1
            if(bitsts==1):
                setbits.append(i)
        return len(setbits)

    '''
    Swap odd and even bits in number
    '''
    def swapBits(self,n):
        #Your code here
        evenmask=0
        oddmask=0
        evenpos=0
        oddpos=0
        for i in range(0,32):
            if(i%2)==0:
                evenmask = evenmask | (0x1<<i)  
            else:
                oddmask = oddmask | (0x1<<i)
        evenpos = (n&evenmask)<<1
        oddpos = (n&oddmask)>>1
        result=evenpos|oddpos
        return(result)
    def checkvalueinint2(self, number,startbit, endbit):
        mask=0
        result=0
        for i in range(startbit,endbit+1):
            mask=mask|(0x1<<i)
        print(bin(mask))
        result = (number & mask)>>startbit
        print(result)

    def programvalueinint2(self,number,startbit,endbit,val):
        mask=0
        for i in range(startbit,endbit+1):
            mask=mask|(0x1<<i)
        mask=~mask
        print(bin(mask))
        newval=number&mask
        result=newval|(val<<startbit)
        print(result)

    # ACT TACK
    def f(self,str1,str2):
        str1ln=len(str1)
        str2ln=len(str2)
        count=0
        if(str1ln>str2ln):
            return False
        str1list=list(str1)
        str2list=list(str2)
        for i in str1list:
            if i in str2list:
                count = count + 1
        if(count==str1ln):
            return True
        else:
            return False

def main():
    test = Solution()
    # ---- Set Bits
    number=15
    shift=3
    print("\n| Set bit " + str(shift) + " in number " + str(number))
    print(test.setKthBit(number,shift))
    # ---- Clear Bits
    number=15
    shift=2
    print("\n| Clear bit " + str(shift) + " in number " + str(number))
    print(test.clearKthBit(number,shift))
    # ---- Check Bits
    number=8
    shift=2
    print("\n| Check bit " + str(shift) + " in number " + str(number))
    print(test.checkKthBit(number,shift))
    # ---- Check set and Clear bits
    number=85462
    print("\n| Check set bits bit in number " + str(number))
    print(test.checkSetnClearBits(number,1))
    number=852333
    print("\n| Check clear bits bit in number " + str(number))
    print(test.checkSetnClearBits(number,0))
    # ---- Check Value in int
    number=281354685
    startbit=15
    endbit=26
    print("\n| Checking value between bit [" + str(endbit)  + ":" + str(startbit) + "] in number " + str(number))
    print(test.checkvalueinint(number,startbit, endbit))
    # ---- Program Value in int
    number=4564
    startbit=9
    endbit=11
    wrvalue=7
    print("\n| Program value " + str(wrvalue) + " between bit [" + str(endbit)  + ":" + str(startbit) + "] in number " + str(number))
    print(test.programvalueinint(number,startbit, endbit,wrvalue))
    # ---- Flip Bits
    number=12
    bitpos=2
    print("\n| Flip bit " + str(bitpos) + " in number " + str(number))
    print(test.flipKthBit(number,bitpos))
    # ---- Swap two numbers
    number1=7
    number2=5
    print("\n| Swap Number " + str(number1) + " & number " + str(number2))
    print(test.swaptwonumbers(number1,number2))

    # ---- Swap Even and Odd bits of the number
    number1=23
    print("\n| Swapping even and odd bits of Number " + str(number1))
    print(test.swapBits(number1))


    number=15
    startbit=1
    endbit=3
    print("\n| Checking value between bit [" + str(endbit)  + ":" + str(startbit) + "] in number " + str(number))
    print(test.checkvalueinint2(number,startbit, endbit))

    number=15
    startbit=1
    endbit=3
    value=3
    print("\n| Program value " + str(value) + " between bit [" + str(endbit)  + ":" + str(startbit) + "] in number " + str(number))
    print(test.programvalueinint2(number,startbit, endbit,value))

    str1="ACTT"
    str2="ACTEW"
    print(test.f(str1,str2))
if __name__ == "__main__":
    main()