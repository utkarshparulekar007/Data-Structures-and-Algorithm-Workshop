from abc import ABC, abstractmethod
class Irctc(ABC) :
    @abstractmethod
    def booktickeet(self) :
        pass

class MakeMyTrip(Irctc) :
    def booktickeet(self) :
        print("=========================================")
        print("Welcome to MakeMyTrip :")
        source = input("Enter source station name :")
        destination = input("Enter destination station name :")
        date = input("Enter travel date :")

class Yatra(Irctc) :
    def booktickeet(self) :
        print("=========================================")
        print ("Welcome to Yatra :")
        source = input("Enter source station name :")
        destination = input("Enter destination station name :")
        date = input("Enter travel date :")

class GoIbibo(Irctc) :
    def booktickeet(self) :
        print("=========================================")
        print("Welcome to GoIbibo :")
        source = input("Enter source station name :")
        destination = input("Enter destination station name :")
        date = input("Enter travel date :")

obj1 = MakeMyTrip()
obj1.booktickeet()

obj2 = Yatra()
obj2.booktickeet()

obj3 = GoIbibo()
obj3.booktickeet()