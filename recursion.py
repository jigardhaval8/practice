def factorial(num):
    if(num<=1):
        return 1
    else:
        return num*factorial(num-1)

print(factorial(3.14))

def fibonacci(num):
    if(num<0):
        exit(1)
    elif(num==0):
        print(num)
        return(0)
    elif((num==1)|(num==2)):
        print(num)
        return(1)
    else:
        print(num)
        return ((fibonacci(num-2)+fibonacci(num-1))

print(fibonacci(4))