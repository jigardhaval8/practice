ipdata = input('Enter Input \n')
stringlength = len(ipdata)
output = {}
max_occur_cnt = 0
max_occur_char = ''
for i in range(0,stringlength):
    tmp_cnt=1
    tmp_char=''
    for j in range(0,stringlength):
        if(j==i):
            pass
        else:
            if(ipdata[j]==ipdata[i]):
                tmp_cnt = tmp_cnt + 1
                tmp_char = ipdata[i]
            else:
                pass

    if(tmp_cnt>=max_occur_cnt):
        if(tmp_cnt==max_occur_cnt):
            if(ord(tmp_char)<ord(max_occur_char)):
                max_occur_cnt = tmp_cnt
                max_occur_char = tmp_char
    
            else:
                pass
        max_occur_cnt = tmp_cnt
        max_occur_char = tmp_char

print("Max Occurance Character is: " + str(max_occur_char))