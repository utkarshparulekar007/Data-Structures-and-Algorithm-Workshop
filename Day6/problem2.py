a = "aaabbbcccc"
b = ""

for i in a:
    if i not in b:
        b+=i
        b+=str(a.count(i))
print(b)