import csv
f = open("student12.csv","a",newline="")
a= csv.writer(f)
# a.writerow(["StudentID","Name","RollNo","MobileNo"])

rollno = int(input("Enter roll no :"))
name = input("Enter name :")
mobile = int(input("Enter mobile no :"))
p1 = int(input("Enter no of marks of p1:"))
p2 = int(input("Enter no of marks of p2:"))
p3 = int(input("Enter no of marks of p3:"))
email = input("Enter email id :")
total = p1+p2+p3
percentage = total/3
result = []
if percentage <40 :
    result = "Fail"

else :
    result = "Pass"

print("Data inserted successfully")
a.writerow([rollno,name,mobile,p1,p2,p3,email,total,percentage,result])

