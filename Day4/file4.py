with open("myfile.txt","w") as f:
    f.write("amit\n")
    f.write("sawantwadi\n")
    f.write("vengurla\n")
    f.write("kudal\n")
    print("file closed:",f.closed)

print("file closed:",f.closed)


with open("myfile.txt","r") as f:
    content = f.read()
    print(content)

