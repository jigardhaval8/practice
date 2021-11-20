class Solution:
    '''
    Function to find if Given String S is palindrom or not - If Palindrom then return 1 else return 0
    '''
    def isPalindrome(self, S):
        strlen=len(S)
        mid=round(strlen/2)
        for i in range(0,mid):
            if(S[i]!=S[strlen-i-1]):
                return 0
        return 1

    '''
    Function to check if two strings are anagram of each other or not,
    If so returns 'YES' else returns 'NO'
    '''
    def isAnagram(self,a,b):
        astringchar = list(a)
        bstringchar = list(b)
        astringchar.sort()
        bstringchar.sort()
        for i in range(0,len(astringchar)):
            if(astringchar[i]!=bstringchar[i]):
                return('NO')
        return('YES')

    '''
    Function merges two string character by character and returns output string
    '''
    def merge(self, S1, S2):
        a=list(S1)
        b=list(S2)
        alen=len(a)
        blen=len(b)
        op_str=''
        if(alen==blen):
            for i in range(0,alen):
                op_str = op_str + str(a[i]) + (b[i])
        elif(alen>blen):
            for i in range(0,blen):
                op_str = op_str + str(a[i]) + (b[i])
            stri=''
            for i in range(blen,alen):
                stri=stri+a[i]
            op_str = op_str + stri

        else:
            for i in range(0,alen):
                op_str = op_str + str(a[i]) + (b[i])
            stri=''
            for i in range(alen,blen):
                stri=stri+b[i]
            op_str = op_str + stri
        return op_str

    '''
    Function takes input string and prints in reversed order
    '''
    def ReverseSort(self, str): 
        inp=list(str)
        revstr=''
        for i in range(len(inp)-1,-1,-1):
            revstr=revstr+inp[i]
        return revstr

    '''
    Function takes input string and sorts in revers order prints 
    '''
    def LexReverseSort(self, str): 
        inp=list(str)
        inp.sort(reverse=True)
        revstr=''
        for i in range(0,len(inp)):
            revstr=revstr+inp[i]
        return revstr

    '''
    Given a string str, convert the first letter of each word in the string to uppercase. 
    ASCII - 
    A - 65
    Z - 90
    --- 
    a - 97 
    z - 122
    '''
    def ConvertToUpperCase(self, s):
        ip=s
        ip_list=list(s)
        newstring=ip.split(' ')
        # print(newstring)
        output=''        
        for i in range(0,len(newstring)):
            firstchar = ord(newstring[i][0])
            if(firstchar>=97):
                firstchar_cap=chr(firstchar-32)
                tmprst=firstchar_cap       
            else:
                tmprst=str(newstring[i][0])
            for j in range(1,len(newstring[i])):
                tmprst = tmprst + str(newstring[i][j]) 
            output=output+tmprst+' '
            tmprst=''
        return(output)

    '''
    Convert string to list with char by char - i.e. helo -> [‘h’,’e’,’l’,’o’]
    '''
    def stringtolist(self,inputstr):
        op = list(inputstr)
        return op

    '''
    Split String to substring by pattern
    '''
    def splitstringtolist(self,inputstr,pattern):
        op = inputstr
        rslt=op.split(pattern)
        return rslt

    '''
    Convert list element to string -> [‘h’,’e’,’l’,’o’] -> helo
    '''
    def listtostring(self,inputlist):
        op=''
        for i in range(0,len(inputlist)):
            op=op+inputlist[i]
        return op

    '''
    Remove duplicate elements from list - [1,2,2,2,7,5] -> [1,2,7,5]
    '''
    def removeduplicatefromlist(self,inputlist):
        result=[]
        for i in (inputlist):
            if i not in result:
                result.append(i)
        return result
# Given a sequence, find the length of the longest palindromic subsequence in it & print longest palindromic subsequence
# Given string find maxim numeric value from given string i.e. kl985swr75 -> 985
# Reverse string without reversing words for e.x. i.like.this->this.like.i
# Write a program to find substring in a string. If found return position where it occurred first.
# Given a string find longest distinct characters(/substring) in a string
# Check if two string are k-anagrams or not
# Find first non repeating character in string
# Find minimum num of characters to be deleted to make both strings anagram



def main():
    
    test=Solution()
    # ---- Palindorm
    ip_string1='aebcbda'
    print("\n| Checking if " + str(ip_string1) + " is palindrom or not")
    print(test.isPalindrome(ip_string1))
    # ---- Anagram
    ip_string1='dusty'
    ip_string2='study'
    print("\n| Checking if " + str(ip_string1) +  " & " + str(ip_string2) + " are anagram or not")
    print(test.isAnagram(ip_string1,ip_string2))
    # ---- merge
    ip_string1='hello'
    ip_string2='bye'
    print("\n| Merging String " + str(ip_string1) +  " & " + str(ip_string2) )
    print(test.merge(ip_string1,ip_string2))
    # ---- ReverseSort
    ip_string1='geeks'
    print("\n| Reversing " + str(ip_string1))
    print(test.ReverseSort(ip_string1))
    # ---- LexReverseSort
    ip_string1='geeks'
    print("\n| Lex Reversing " + str(ip_string1))
    print(test.LexReverseSort(ip_string1))
    # ---- ConvertToUpperCase
    ip_string1='my Name is jigar Soni Q'
    print("\n| Convert each first char to uppercase " + str(ip_string1))
    print(test.ConvertToUpperCase(ip_string1))
    # ---- StringToList
    ip_string1='hithisisjigar'
    print("\n| String to list " + str(ip_string1))
    print(test.stringtolist(ip_string1))
    # ---- ListToString
    ip_string1=['h','e',' ','m','w']
    print("\n| list to String " + str(ip_string1))
    print(test.listtostring(ip_string1))
    # ---- Split STring to pattern
    ip_string1='my name$is$jigar  Soni'
    ip_string2='$'
    print("\n| Split input string " + str(ip_string1) + " with character " + str(ip_string2))
    print(test.splitstringtolist(ip_string1,ip_string2))
    # ---- removeduplicatefromlist
    ip_string1=[1,23,4,5,7,89,43,2,3,1,2,3,4,2,1,1,2]
    print("\n| Removing Duplicates from list " + str(ip_string1))
    print(test.removeduplicatefromlist(ip_string1))
if __name__ == "__main__":
    main()