list = [1,2,2,3,4,2]
a = []

element = int(input("Enter the element to remove: "))
for i in list:
    if i != element:
        a.append(i)
print(a)
