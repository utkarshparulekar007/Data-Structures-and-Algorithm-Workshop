list = []
A    = int(input("Enter size of array: "))
B    = int(input("Enter no. of elements: "))
even = []
odd  = []
for i in list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("arranged list:",even+odd)