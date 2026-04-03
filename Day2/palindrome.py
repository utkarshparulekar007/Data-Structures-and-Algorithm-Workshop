name = "raceca"
print(name) #left to right
print(name[::-1]) #right to left 

if name == name[::-1]:
    print("This is a palindrome")
else:
    print("This is not a palindrome")