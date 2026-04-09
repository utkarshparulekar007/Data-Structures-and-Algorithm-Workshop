import sys
class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def addnode(self,value) :
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
            print()
            print("Node added successfully  !!")
            print()
        else:
            self.tail.next = node
            self.tail = node

if __name__ == "__main__" :
    object = linkedlist()
    while True :
        print("1. Add Node Linked List")
        print("2. Add Node in beginning")
        print("3. Add Node in end")

        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            val = int(input("Enter the value: "))
            object.addnode(val)

        # elif choice == 2:
        #     val = int(input("Enter the value: "))
        #     object.addnodebeginning(val)

        # elif choice == 3:
        #     val = int(input("Enter the value: "))
        #     object.addnodeend(val)

        elif choice == 5:
            sys.exit()

        else:
            print("Invalid Choice")