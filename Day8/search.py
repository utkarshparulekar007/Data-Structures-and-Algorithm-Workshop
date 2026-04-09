import re
a = input("Enter string to perform match operations :")
f = open("file122.txt","r")
c = f.read()

mtch = re.search(a,c)
print(mtch)
if mtch !=None :
    print("Match found at beginning level") 
    print(mtch.start(),"",mtch.end())

else :
    print("There is no match")