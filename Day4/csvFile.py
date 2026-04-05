import csv
f = open("student.csv","a",newline="")
a= csv.writer(f)
# a.writerow(["StudentID","Name","RollNo","MobileNo"])

student = int(input("Enter student id :"))
rollno = int(input("Enter roll no :"))
name = input("Enter name :")
mobile = int(input("Enter mobile no :"))
a.writerow([student,name,rollno,mobile])
print("Data inserted successfully")