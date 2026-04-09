rows   = int(input("Enter the no. of rows :"))
cols   = int(input("Enter the no. of cols :"))
matrix = []

for i in range (rows):
    row = list(map(int,input(f"Enter the elements of row {i+1} :").split()))
    matrix.append(row)

print("Biggest number from each row :")
for row in matrix:
    print(max(row),end = " ")
