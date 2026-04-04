A = {"X": 20, "Y": 10, "Z": 30}

min_key = None
min_value = float('inf')

for i,j in A.items():
    if min_key is None or j < min_value:
        min_key = i
        min_value = j
print(min_key)