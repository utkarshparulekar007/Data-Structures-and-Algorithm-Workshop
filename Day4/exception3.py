try :
    a = int(input("Enter the first integer no :"))
    b = int(input("Enter the second integer no :"))
    print(a/b)
except (ValueError,ZeroDivisionError) as message :      
    print(message)
except :
    print("This is the defalt part")