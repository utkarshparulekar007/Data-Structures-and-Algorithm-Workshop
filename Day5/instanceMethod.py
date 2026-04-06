# class Student :
#     def __init__(self,name,roll_no,mob):
#         self.name = name 
#         self.roll_no = roll_no
#         self.mob = mob

#     def display(self):
#         print(self.name," ",self.roll_no," ",self.mob)

# stud = Student("prashant",101,87945654)
# stud.display()


class Student :

    @staticmethod
    def get_personal_details(firstname,lastname):
       print("Your personal details = ",firstname,lastname)

    @staticmethod
    def get_contact_details(mob,rollno):
        print("Your contact details = ",mob,rollno)

Student.get_personal_details("Prashant","Jha")
Student.get_contact_details(87945654,101)