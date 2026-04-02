# #WAP to accept any one no and check pos ,neg,zero
# no = int(input("Enter any one number:"))
# if no>0:
#     print("Positive no.")
# if no<0:
#     print("Negative no.")
# if no==0:
#     print("Zero Number")



no1 = int(input("Enter no1:")) #50
no2 = int(input("Enter no2:")) #30
no3 = int(input("Enter no3:")) #90
no4 = int(input("Enter no4:")) #30
no5 = int(input("Enter no5:")) #40
if no1>no2 and no1>no3 and no1>no4 and no1>no5:
    print("No1 is greater")
if no2>no1 and no2>no3 and no2>no4 and no2>no5:
    print("No2 is greater")
if no3>no1 and no3>no2 and no3>no4 and no3>no5:
    print("No3 is greater")
if  no4>no1 and no4>no2 and no4>no3 and no4>no5 :
    print("No4 is greater")
if  no5>no1 and no5>no2 and no5>no3 and no5>no4 :
    print("No5 is greater")


