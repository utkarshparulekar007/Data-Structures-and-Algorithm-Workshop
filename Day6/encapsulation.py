class Base : #parent class
    def __init__(self):
        self.a = "Prashant"  #public data member
        self.__c = "Ashish"  #private member

class Derived(Base) : #child class
    def __init__(self):
        Base.__init__(self)
        # print("Calling private member of base class")
        # print(self.a)
        # print(self.__c)

# obj1 = Derived()    
# print(obj1.a)
# print(obj1.__c)

obj2 = Base()
print(obj2.a)
print(obj2.__c)
