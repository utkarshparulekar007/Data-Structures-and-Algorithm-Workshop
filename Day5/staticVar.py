class New :
    a= 10

    def __init__(self):
        self.name = "Prashant"

obj1 = New()
obj2 = New()
obj3 = New()
print(obj1.a)
print(obj2.a)
print(obj3.a)
New.a = 50
print()
print(obj1.a)
print(obj2.a)
print(obj3.a)