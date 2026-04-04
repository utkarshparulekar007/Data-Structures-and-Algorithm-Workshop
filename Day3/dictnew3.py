box    ={}
jars   ={}
crates ={}
box['biscuit'] = 1
box['cake'] = 2
jars['jam'] = 3
crates['box']= box
crates['jars']= jars
print(len(crates[box]))