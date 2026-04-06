# import sys

# class CRUD:
#     def __init__(self):
#         print("Student Management System")
#         self.studentID     =   []
#         self.studentName   =   []
#         self.studentRollNo =   []
#         self.studentCity   =   []

#     def addStudent(self):
#         self.studentID.append(input("Enter Student ID : "))
#         self.studentName.append(input("Enter Student Name : "))
#         self.studentRollNo.append(input("Enter Student Roll No : "))
#         self.studentCity.append(input("Enter Student City : "))

#     def showStudent(self):
#        print(f"{"ID":<10}{'Name':<10}{'Roll No.':<10}{'City':<10}")
#        for i in range(len(self.studentID)):
#             print(f"{self.studentID[i]:<10}{self.studentName[i]:<10}{self.studentRollNo[i]:<10}{self.studentCity[i]:<10}")


#     def delStudent(self):
#          id = input("Enter Student ID : ")
#          if id in self.studentID:
#             self.student.pop(index)
#             self.studentID.pop(index)
#             self.studentName.pop(index)
#             self.studentRollNo.pop(index)
#             self.studentCity.pop(index)

# while True:
#     print ("Student Management System")
#     choice = (input("Enter your choice (1. Add Student, 2. Show Student, 3. Exit): "))
#     print ("1. Add Student")
#     print ("2. Show Student")
#     print ("3. Exit")

#     if choice == 1 :
#             obj.addStudent()
#     elif choice == 2 :
#             obj.showStudent()
#     elif choice == 3 :
#             sys.exit()



# obj = CRUD()
# print (obj.addStudent())
# obj.showStudent()
