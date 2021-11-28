class Car:
    def __init__(self,carmodel,carfuel):
        self.carmodel=carmodel
        self.carfuel=carfuel
    def testdrive(self):
        print('this is test drive function')

def main():
    jigarfirstcar=Car('Centro','EV')
    print("My First Car model: " + str(jigarfirstcar.carmodel))
    print("My First Car Fuel: " + str(jigarfirstcar.carfuel))

if __name__=='__main__':
    main()