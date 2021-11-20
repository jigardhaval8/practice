'''Write code to make existing string to palindrome by making minimum removal

Input : aebcbda
Output : 2
Remove characters 'e' and 'd'
Resultant string will be 'abcba'
which is a palindromic string

Input : ee  o  ee
Output : 8
https://www.techiedelight.com/find-minimum-number-deletions-convert-string-into-palindrome/
https://practice.geeksforgeeks.org/problems/minimum-deletitions1648/1


r f
ks ks
g g
'''

class Solution:
    def MakeStringPalindrom(self,ipstring):
        ip = ipstring
        ip_len = len(ip)
        mid = round(ip_len/2) 
        discard_counter=0
        match_flag = 0
        match_flag_i=0
        match_flag_j=0
        for i in range(ip_len-1,mid-1,-1):
            for j in range(0,ip_len):
                print("-" + str(ip[i])  + "-" + str(ip[j]))
                if(ip[i]==ip[j]):
                    match_flag=1
                    match_flag_i=i
                    match_flag_j=j
                    break
            if((match_flag==0)):
                discard_counter = discard_counter + 1
                print("Discarded : " + str(ip[i]) + "at index " + str(i) )
            else:
                if((match_flag_i==match_flag_j)):
                    discard_counter = discard_counter + 1
                    print("Discarded : " + str(ip[i]) + "at index " + str(i) )
                else:
                    pass
        return discard_counter
                    
def main():
    print("Hello World!")
    test=Solution()
    print(test.MakeStringPalindrom('aebcbda'))

if __name__ == "__main__":
    main()


# a e b c b d a


# aebcbda -> abcba
# aebbda  -> abba
