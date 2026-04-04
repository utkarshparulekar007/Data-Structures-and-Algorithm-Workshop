import time 
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(1, n + 2 - i):
        time.sleep(1)
        print(n+1-i, end=" ")
    print()
