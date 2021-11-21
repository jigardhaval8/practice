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
        ip=ipstring
        ip_len=len(ipstring)
        first=0
        last=ip_len-1
        discard_counter=0
        while(first<last):
            if(ip[first]==ip[last]):
                first=first+1
                last=last-1
            else:
                if(ip[(first+1)]==ip[last]):
                    discard_counter=discard_counter+1
                    # print('Discard @' + str(ip[first]) + " At index " +  str(first))
                    # print(" Comaring " + str(first+1) + " & " + str(last))
                    first=first+2
                    last=last-1
                else:
                    if(ip[(first)]==ip[(last-1)]):
                        discard_counter=discard_counter+1
                        # print('Discard #' + str(ip[last]))
                        first=first+1
                        last=last-2
                    else:
                        discard_counter=discard_counter+2
                        # print('Discard $' + str(ip[first]))
                        # print('Discard %' + str(ip[last]))
                        first=first+1
                        last=last-1                        
        return discard_counter

    def isPossible(self, S):
        ip = S
        uniquechar=[]
        uniquechar_cnt=[]
        odd_numerelementinlist=0
        ip_list=list(ip)
        ip_list.sort()
        # print(ip_list)
        for i in ip_list:
            if i not in uniquechar:
                uniquechar.append(i)
        # print(uniquechar)
        for i in uniquechar:
            tmp_cnt=0
            for j in range(0,len(ip_list)):
                if(ip_list[j]==i):
                    tmp_cnt=tmp_cnt+1
            uniquechar_cnt.append(tmp_cnt)
        # print(uniquechar_cnt)
        for i in uniquechar_cnt:
            if(i%2!=0):
                odd_numerelementinlist=odd_numerelementinlist+1
        if(odd_numerelementinlist>1):
            return('No')
        else:
            return('Yes')
    #Function to reverse words in a given string.
    def reverseWords(self,S,chr):
        ip=S
        a=ip.split(chr)
        # print(a)
        newstr=''
        for i in range(0,len(a)):
            newstr=newstr+str(a[len(a)-1-i])+chr
        return(newstr)
def main():
    print("Hello World!")
    test=Solution()
    print(test.MakeStringPalindrom('aebcbda'))
    print(test.MakeStringPalindrom('geeksforgeeks'))
    print(test.isPossible('geeksforgeeks'))
    print(test.reverseWords('i.like.this.program.very.much','.'))

if __name__ == "__main__":
    main()


# a e b c b d a


# aebcbda -> abcba
# aebbda  -> abba
