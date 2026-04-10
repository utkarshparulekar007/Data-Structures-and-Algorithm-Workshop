# import QueueLinkedList as Queue 

# class BSTNode:
#     def __init__(self,data) :
#         self.data = data
#         self.left = None
#         self.right = None

#     def insertNode(rootNode)


class Node :
    def __init__(self,data) :
        self.data = data
        self.left = None
        self.right = None

class BinaryTree :
    def __init__(self) :
        self.root = None

    def insert(self,value):
        if self.root is None :
            self.root = Node(value)
        else :
            self.insertNode(self.root,value)

    def insertNode(self,rootNode,value) :
        if value < rootNode.value :
            if rootNode.left is None :
                rootNode.left = Node(value)
            else :
                self.insertNode(rootNode.left,value)
        else :
            if rootNode.right is None :
                rootNode.right = Node(value)
            else :
                self.insertNode(rootNode.left,value)

btObj = BinaryTree()
btObj.insert(50)
btObj.insert(30)

print(btObj)