class SortAlgo:
    '''
    Bubble Sort: https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm
    '''	
    def BubbleSort(self,ip_list,operation):
        iplen=len(ip_list)
        last=iplen
        tmp=0
        #Assending Order
        if(operation==1):
            while(last!=1):
                for i in range(1,last):
                    if(ip_list[i-1]>ip_list[i]):
                        tmp=ip_list[i]
                        ip_list[i]=ip_list[i-1]
                        ip_list[i-1] = tmp
                # print(ip_list)
                last=last-1
            return (ip_list)
        #Desending Order
        else:
            while(last!=1):
                for i in range(1,last):
                    if(ip_list[i-1]<ip_list[i]):
                        tmp=ip_list[i]
                        ip_list[i]=ip_list[i-1]
                        ip_list[i-1] = tmp
                last = last - 1
            return(ip_list)

def main(): 
    print("| Sort Algorithms ")
    inputlist=[1,5,9,2,3,5,6,7,8,2,0,2,3,88,2]
    test = SortAlgo()
    print(test.BubbleSort(inputlist,1))
    print(test.BubbleSort(inputlist,0))

if __name__=="__main__":
    main()
