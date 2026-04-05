try:
    a = int(input("Enter the first integer no :"))
    b = int(input("Enter the second integer no :"))
    print(a/b)

except (ZeroDivisionError,ValueError) as msg :
        print(msg)

else :
    print("There is no error")

finally :
    print("I will always execute")