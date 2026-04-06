class Hod :
    def __init__(self,name,age,rollno):
        self.name = name
        self.age = age
        self.empId = rollno
    def info(self):
        print("My Name is  : ",self.name)
        print("My Age is : ",self.age)
        print("My Employee Id is : ",self.empId)
              
obj = Hod('Arjun',45,101)
obj.info()