class Hod :
    def __init__(self):
        self.name = "Prashant jha"
        self.age = 22
        self.empId = 1001
    def info(self):
        print("My Name is  : ",self.name)
        print("My Age is : ",self.age)
        print("My Employee Id is : ",self.empId)
              
obj = Hod()
obj.info()