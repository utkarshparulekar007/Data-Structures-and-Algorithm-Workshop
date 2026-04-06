class Father :
    def __init__(self) :
        print("Father = i am already on the breakfast table")

class child(Father) :
    def __init__(self) :
        print("Son = i will be late for the breakfast")
        super().__init__()
obj = child()