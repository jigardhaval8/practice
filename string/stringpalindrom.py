class Solution:
    def isPalindrome(self, S):
        strlen=len(S)
        mid=round(strlen/2)
        for i in range(0,mid):
            if(S[i]!=S[strlen-i-1]):
                return 0
        return 1

    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        astringchar = list(a)
        bstringchar = list(b)
        astringchar.sort()
        bstringchar.sort()
        for i in range(0,len(astringchar)):
            if(astringchar[i]!=bstringchar[i]):
                return('NO')
        return('YES')



def main():
    print("Hello World!")
    test=Solution()
    print(test.isPalindrome('aebcbda'))
    print(test.isAnagram('dusty','study'))

if __name__ == "__main__":
    main()