#nested try exception block
try:
    a = int(input("Enter the first integer no :"))
    b = int(input("Enter the second integer no :"))
    try :
        print(a/b)
    except ZeroDivisionError as msg :
        print(msg)
       
except ValueError as msg :
    print(msg)
