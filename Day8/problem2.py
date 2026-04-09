A = [0,0,1,2,0,3,6]
B = []
started = False
for num in A:
    if num!=0:
        started = True
    if started:
        B.append(num)

print(A)
print(B)