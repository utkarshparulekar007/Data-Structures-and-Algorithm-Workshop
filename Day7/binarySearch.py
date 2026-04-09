def binarySearch(array,target):
    start = 0
    end  = len(array) - 1   #calculate mid index
    while start<=end:
        mid = (start + end) //2
        if array[mid] == target :
            return mid 
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

array = [1,2,3,4,5]
target = 4 
result = binarySearch(array,target)
print(result)
  