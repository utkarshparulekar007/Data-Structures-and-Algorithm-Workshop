myList = [1,2,2,3,4,3,5]
freq = {}
for i in myList:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)
