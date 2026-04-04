rec = {"name": "John", "age": 30, "city": "New York"}
id1 = id(rec)
del rec
rec = {"name": "John", "age": 30, "city": "New York"}
id2 = id(rec)
print(id1==id2)
print(id(id1))
print(id(id2))