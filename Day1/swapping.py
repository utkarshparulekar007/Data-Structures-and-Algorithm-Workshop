val1= int(input("Enter val1 :")) #100
val2= int(input("Enter val2 :")) #200
print("Before swapping val1= ",val1,"val2=",val2)

temp = val1 #100
val1=val2   #200
val2=temp   #100

print("After swapping val1= ",val1,"val2=",val2)


#swapping using two variables

a= int(input("Enter val1 :")) #100
b= int(input("Enter val2 :")) #200
print("Before swapping val1= ",a,"val2=",b)
a= a+b
b=a-b
a=a-b
print(a,b)