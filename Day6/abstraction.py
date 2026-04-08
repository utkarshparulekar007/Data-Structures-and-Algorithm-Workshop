from abc import ABC, abstractmethod
class Help4code(ABC):
    @abstractmethod
    def training(self):
        pass

    @abstractmethod
    def placement(self):
        pass    

class Ashish(Help4code):
    def training(self):
        print("C , Java , Python")

    def placement(self):
        print("Providing placement in Python")

class Ankush(Help4code):
    def training(self):
        print("C , C++ ")

    def placement(self):
        print("Providing placement in C++")

class Prashant(Help4code):
    def training(self):
        print("Machine Learning ")

    def placement(self):
        print("Data science placement")

obj1 = Ashish()
obj1.training()
obj1.placement()

obj2 = Ankush()
obj2.training()
obj2.placement()

obj3 = Prashant()
obj3.training()
obj3.placement()