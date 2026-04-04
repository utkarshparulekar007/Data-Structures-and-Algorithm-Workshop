arr = {}
arr[1] = 1
arr['1'] = 2
arr[1] += 1

sum = 0
for i in arr:
    sum += arr[i]
print(sum)