myList = [5,7,8,3,7,8,9,2,3]
newList = []
for i in range(len(myList)):
    count = 0
    key = myList[i]

    j = i+1
    while j < len(myList):
        if key == myList[j]:
            newList.append(key)
        j = j+1
print(len(newList))