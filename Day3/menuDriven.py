#wap for menu driven code
import sys

def add():
    val1 = int(input("Enter the value of A: ")) 
    val2 = int(input("Enter the value of B: "))
    print("Addition =", val1 + val2)

def sub():
    val1 = int(input("Enter the value of A: ")) 
    val2 = int(input("Enter the value of B: "))
    print("Subtraction =", val1 - val2)

def mul():
    val1 = int(input("Enter the value of A: ")) 
    val2 = int(input("Enter the value of B: "))
    print("Multiplication =", val1 * val2)

def div():
    val1 = int(input("Enter the value of A: ")) 
    val2 = int(input("Enter the value of B: "))
    print("Division =", val1 / val2)

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        mul()
    elif choice == 4:
        div()
    elif choice == 5:
        sys.exit()
