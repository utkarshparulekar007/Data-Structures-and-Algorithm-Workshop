class Rbi:
    def publicPolicy(self):
        print("Check the public policy of rbi")

    def __privatePolicy(self):
        print("There is some private policy that is not accessible")

class Sbi(Rbi):
    def __init__(self): #first sbi class count called
        Rbi.__init__(self) #second parent class count called

    def callingPublicMethod(self): #public method
        print("\nInside child class") #parent class public method
        self.publicPolicy()
        
    def callingPrivateMethod(self): #child class public method
        self.__privatePolicy()  #calling private class private method

# obj1 = Sbi()
# obj1.callingPublicMethod()
# obj1.callingPrivateMethod()
# obj1.publicPolicy()
# obj1.__privatePolicy()

# obj2 = Rbi()
# obj2.publicPolicy()
# obj2.__privatePolicy()
