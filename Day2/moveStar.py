#wap to move *
# input = prashant*is*a*good*programmer
# output = ****prashantisagoodprogrammer 

input = "prashant*is*a*good*programmer"
newname = ''
val = ''
for i in input:
    if i != '*':
        newname += i
    else:
        val += i
print(newname)
print(str(val+newname))