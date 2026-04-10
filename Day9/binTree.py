
    #  Each node has either 0 or 2 children
    #  No node has a single child


# Complete binary tree
    #   All levels except possibly the last are completely filled
    #   Nodes in the last level are filled from left to right

# Perfect binary tree
    #   All internal nodes have exactly two nodes
    #   All leaf nodes are at the same level


#Depth First Search


class Tree :
    def __init__(self,data) :
        self.data = data
        self.children = []

    def addChild(self,child) :
        self.children.append(child)

    def __str__(self,level = 0) :
        ret = " "* level + str(self.data) + "\n"
        for child in self.children :
            ret += child.__str__(level+1)
        return ret


rootNode  = Tree("N1")
N2        = Tree("N2")
N3        = Tree("N3")
N4        = Tree("N4")
N5        = Tree("N5")
N6        = Tree("N6")
N7        = Tree("N7")
N9        = Tree("N9")
N10       = Tree("N10")
#Add child nodes in tree
rootNode.addChild(N2)
rootNode.addChild(N3)
N2.addChild(N4)
N2.addChild(N5)
N3.addChild(N6)
N3.addChild(N7)
N4.addChild(N9)
N4.addChild(N10)

print(rootNode)
