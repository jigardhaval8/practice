class SearchAlgo:
    '''
    Given an array Arr of N elements and a integer K. Your task is to return the position of first occurence of K in the given array.
    Note: Position of first element is considered as 1.
    Linear Search - https://www.tutorialspoint.com/data_structures_algorithms/linear_search_algorithm.htm
    '''	
    def linearsearch(self,arr, n, k): 
        for i in range(0,n):
            if(arr[i]==k):
                return i+1
        return -1

    '''
    Given a sorted array of size N and an integer K, find the position at which K is present in the array using binary search.
    Binary Search- https://www.tutorialspoint.com/data_structures_algorithms/binary_search_algorithm.htm
    '''
    def binarysearch(self, arr, n, k):
        ip_array = arr
        ip_array.sort()
        lowbound   = 0
        upperbound = n-1
        notfound=1
        while notfound:
            if(lowbound>upperbound):
                return -1          
            mid=lowbound + int((upperbound-lowbound)/2)
    #       print("Low " + str(lowbound) + " Upper " + str(upperbound))
    # 		print("Mid " + str(mid))
            if(arr[mid]==k):
                notfound=0
                return mid
            elif(arr[mid]>k):
                upperbound = mid-1           
            elif(arr[mid]<k):
                lowbound = mid+1
            else:
                return -1
def main():
    algo=SearchAlgo()
    # ---- Linear Seach
    ip_list=[9, 7, 2, 16, 4]
    n = 5
    search=16
    print("\n| Linear seach " + str(search) + " in list " + str(ip_list))
    print(algo.linearsearch(ip_list,n,search))

if __name__=="__main__":
    main()