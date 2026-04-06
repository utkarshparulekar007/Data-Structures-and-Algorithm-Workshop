class College :
    def college_name(self) :
        print("YBIT is a Great college")

class Student(College) :
    def student_info(self) :
        print("Name     :  Prashant Jha")
        print("Branch   :  Mechanical")

class Exam(Student) :
    def subject(self) :
        print("Subject1 :  Design Engineering")
        print("Subject2 :  Maths")
        print("Subject3 :  C language")

obj = Exam()
obj.college_name()
obj.student_info()
obj.subject()