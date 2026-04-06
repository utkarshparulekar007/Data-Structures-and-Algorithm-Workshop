class New :
    def __init__(self):
        self.a = 10

obj1 = New()
obj2 = New()
obj3 = New()
print(obj1.a)
print(obj2.a)
print(obj3.a)

obj1.a = 20
print()
print(obj1.a)
print(obj2.a)
print(obj3.a)