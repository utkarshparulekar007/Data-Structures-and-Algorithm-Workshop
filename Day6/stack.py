import sys
class Stack :
    def __init__(self):
        self.stackList = []   #Stackl created

    def push(self, value):
        self.stackList.append(value)

    def displayStack(self):
        print(" ")
        print(self.stackList)
        print(" ")

    def isEmpty(self):
        if self.stackList == []:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.stackList.pop()
        
    def deleteStack(self) :
        self.stackList = None
        print(" ")
        print("Stack is deleted")
        print(" ")

    def peek(self) :
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.stackList[-1]
        
stackObj = Stack()

while True:
    
    print("1. Push Element")
    print("2. Pop Element")
    print("3. Display Stack Elements")
    print("4. IsEmpty")
    print("5. Delete Stack")
    print("6. Peek Element")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter the value: "))
        stackObj.push(val)

    elif choice == 2:
        stackObj.pop()

    elif choice == 3:
        stackObj.displayStack()

    elif choice == 4:
        print(stackObj.isEmpty())

    elif choice == 5:
        stackObj.deleteStack()

    elif choice == 6:
        print(stackObj.peek())

    elif choice == 7:
        sys.exit()
