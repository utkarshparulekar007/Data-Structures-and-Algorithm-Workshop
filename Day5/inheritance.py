# Extending the property from one classs to another is called ass inheritance 
# Base class : Parent class
# Derived class : Child class

class College :
    def college_name(self):
        print("YBIT")

class Student(College):
    def student_info(self):
        print("Name   :  Prashant Jha")
        print("Branch :  Mechanical")
obj = Student()
obj.college_name()
obj.student_info()