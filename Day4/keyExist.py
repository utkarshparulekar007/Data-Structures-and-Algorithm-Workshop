myDict = {
    "name": "Alice",
    "age": 30,
}

i = input("Enter the key: ")

if i in myDict:
    print("Key exists")
else:
    print("Key does not exist")
