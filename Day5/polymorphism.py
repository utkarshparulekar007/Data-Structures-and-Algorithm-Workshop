class Principal :
    def role(self):
        print("I am managing all the activities in college")

class Dean :
    def role(self):
        print("Dean = I am taking all the decisions in college")

class Hod :
    def role(self):
        print("Hod = I have responsibility of my department")

class Faculty :
    def role(self):
        print("Faculty = I have to complete the syllabus of my subjects")

def func(obj) :
    obj.role() #calling function
campus = [Principal(),Dean(),Hod(),Faculty()]
for obj in campus :
    func(obj)