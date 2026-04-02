#WAP to accept value of a,b,c to find max value

a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))
c = int(input("Enter the value of c"))

if a > b :
    if a > c:
       print("a is greater",a)
    else :
        print("c is greater",c)
else :
    if b > a :
        if b > c:
                     print("b is greater") 
        else :
            print("c is greater")


 
