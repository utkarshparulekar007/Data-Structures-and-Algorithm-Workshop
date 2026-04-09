def findbiggestNumber(arr):       #===================>O(1)
    firstValue = arr[0]           #===================>O(1)
    for i in range(1,len(arr)):   #===================>O(n)
        if arr[i] > firstValue:   #===================>O(1)
            firstValue = arr[i]   #===================>O(1)
    return firstValue             #===================>O(1)
array = [1,2,3,4,5]
print(findbiggestNumber(array))