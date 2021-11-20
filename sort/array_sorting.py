class Array:
    def Sort_assending(self,iparray):
        iparray.sort()
        return (iparray)
    
    def Sort_dessending(self,iparray):
        iparray.sort(reverse=True)
        return iparray


def main():
    ip_array = [1,5,9,8,2,5,6,3,8,9,2,10,226,4,-8,-999,55]
    test=Array()
    print('Assending Sort')
    print(test.Sort_assending(ip_array))
    print('Dessending Sort')
    print(test.Sort_dessending(ip_array))
    ip_list2=[(1,2),(3,3),(1,1)]
    print(test.Sort_assending(ip_list2))


if __name__ == "__main__":
    main()