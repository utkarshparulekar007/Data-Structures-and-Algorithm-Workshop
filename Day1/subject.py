phy = int(input("Enter the marks for physics:"))
chem = int(input("Enter the marks for chem:"))
maths = int(input("Enter the marks for maths:"))
gender = input("Enter gender(m/f)?:")
total = (phy+chem+maths)
percentage = total/3

if percentage>=60 and gender == "m" :
    print("Eligible for placement")

else :
    print("Eligible for data entry job")