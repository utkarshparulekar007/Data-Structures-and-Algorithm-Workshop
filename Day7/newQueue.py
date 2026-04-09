import sys
class Queue :
    def __init__(self,queueSize):
        self.queueList = []   #Queue = []   #Queuel created
        self.queueSize = queueSize

    def Enqueue(self, value):
        
        if self.isFull(value):
            print("Queue is Full")
        else:
            self.queueList.append(value)

    def displayQueue(self):
        print(" ")
        print(self.queueList)
        print(" ")

    def isEmpty(self):
        if self.queueList == []:
            return True
        else:
            return False
        
    def Dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            return self.queueList.pop(0)
            print("Item is dequeued from the Queue")
        
    def deleteQueue(self) : #delete the queue
        self.queueList = []
        print(" ")
        print("Queue is deleted")
        print(" ")

    def peek(self) : #It returns the first element of the queue
        if self.isEmpty():
            print("Queue is Empty")
        else:
            return self.queueList[0] #Slicing of the list
        
    def isFull(self,value):
        if len(self.queueList) == self.queueSize:
            return True
        else:
            return False
        
size   = int(input("Enter size of Queue: "))      
queueObj = Queue(size)

while True:
    
    print("1. Enqueue Element")
    print("2. Dequeue Element")
    print("3. Display Stack Elements")
    print("4. IsEmpty")
    print("5. Delete Queue")
    print("6. Peek Element")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter the value: "))
        queueObj.Enqueue(val)

    elif choice == 2:
        queueObj.Dequeue()

    elif choice == 3:
        queueObj.displayQueue()

    elif choice == 4:
        print(queueObj.isEmpty())

    elif choice == 5:
        queueObj.deleteQueue()

    elif choice == 6:
        print(queueObj.peek())
          
    elif choice == 8:
        sys.exit()
