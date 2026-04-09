def linearSearch(array, target):   #=======================>O(n)        C          
    for i in range(len(array)):    #=======================>O(n)         O        
        if array[i] == target:     #=======================>O(1)          M      I
            return i               #=======================>O(1)           P    X  T
    return -1                      #=======================>O(1)            L  E    Y
                                                                           
array = [1,2,3,4,5,6,7,8,9]
target = 4
result = (linearSearch(array, target))

if result == -1:
    print("Element not found")
else:
    print("Element found at index", result)