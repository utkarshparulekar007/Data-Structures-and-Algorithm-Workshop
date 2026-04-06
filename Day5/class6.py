class Student :
    def __init__(self):
        self.name = "Prashant"
        self.roll_no = 101

    def getdata(self):
        self.s_mb = 87945654

obj = Student()
obj.getdata()

del obj.s_mb
obj.s_branch = "CS"
print(obj.__dict__)