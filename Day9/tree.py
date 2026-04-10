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

rootNode     = Tree("Drinks"       )
hot          = Tree("Hot"          )
cold         = Tree("Cold"         )
tea          = Tree("Tea"          )
coffee       = Tree("Coffee"       )
nonAlcoholic = Tree("Non Alcoholic")
alcoholic    = Tree("Alcoholic"    )

#Add child nodes in tree
rootNode.addChild(hot)
rootNode.addChild(cold)
hot.addChild(tea)
hot.addChild(coffee)
cold.addChild(nonAlcoholic)
cold.addChild(alcoholic)

print(rootNode)
