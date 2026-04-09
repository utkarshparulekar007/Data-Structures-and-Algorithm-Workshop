A = {"C":3,"B":2,"A":1}
# output = {"A":1,"B":2,"C":3}
# output = {"C":3,"B":2,"A":1}
sorted_dict = dict(sorted(A.items()))
print(sorted_dict)

print("Descending order")
sorted_dict = dict(sorted(A.items(),reverse = True))
print(sorted_dict)