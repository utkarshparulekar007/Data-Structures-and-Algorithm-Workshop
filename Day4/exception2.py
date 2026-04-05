
try :
    n1 = int(input("Enter first value:"))
    n2 = int(input("Enter second value:"))

    print (n1/n2)
except ZeroDivisionError :
    print("Division by zero is not possible")
except ValueError :
    print("Invalid Input")
print("To be continued")


