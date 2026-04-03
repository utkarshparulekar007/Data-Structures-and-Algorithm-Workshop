n = int(input("Enter size of array: "))
arr= []
print("Enter the elements of array: ")
for i in range(n):
    val = int(input("Enter the value of array: "))
    arr.append(val)
sum = 0
print(arr)
for i in range(n):
    if i+1 in range(n):
        sum+= abs(arr[i] - arr[i+1])
        print(sum)