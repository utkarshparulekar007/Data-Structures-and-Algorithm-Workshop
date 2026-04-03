name = "Mumbai"
#wap to reverse the string using for loop
n = len(name)
newname = ""
for i in range (n, 0, -1):
    newname = newname + name[i-1]  
print(name)  
print(newname)