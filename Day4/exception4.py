try :
    a = int(input("Enter the first integer no :"))
    b = int(input("Enter the second integer no :"))
    print(a/b)
except (ValueError,ZeroDivisionError) as message :      
    print("Enter the correct no.",message)
except :
    print("This is the default part")