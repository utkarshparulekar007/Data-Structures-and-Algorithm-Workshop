f = open("myfile.txt","w")
mylist = ["Pune ","Nagpur ","Mumbai "]
tuple = ("sawantwadi ","Vengurla ","Kudal ")
dict = {"Zirangwadi":"Harshad","Hodawade":"Atharv","Kariwade":"Atharva"}
f.writelines(mylist)
f.writelines(tuple)
f.writelines(dict)
f.close()
print("file operation done")

f = open("myfile.txt","r")
print(f.read())
f.close