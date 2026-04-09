# import re 
# count = 0
# pattern = re.compile("function")

# matcher = pattern.finditer(" This is a function in python that is the function of the index and the function")

# for i in matcher:
#     count += 1
#     print(i.start(),"....",i.end(),"....",i.group())

# print("The no. of occurences",count)


# =============================================================================================================

# import re
# count = 0
# matcher = re.finditer("Hi","HiHiHiHi")

# for i in matcher:
#     count += 1
#     print(i.start(),"....",i.end(),"....",i.group())

# print("The no. of occurences",count)


# =============================================================================================================


# import re
# obj = input("Enter a character :")
# objMatch = re.finditer(obj,"4gdfgmf ew")

# for match in objMatch:
#     print(match.start(),"....",match.end(),"....",match.group())


# =============================================================================================================
            #MATCH 0PERATION

# import re
# a = input("Enter string to perform match operations :")
# mtch = re.match(a,"Python is very important language")
# print(mtch)
# if mtch !=None :
#     print("Match found at beginning level")
#     print(mtch.start(),"",mtch.end())

# else :
#     print("There is no match")


# =============================================================================================================
           #FULL MATCH OPERATION 
             #as a name suggests when we have to match a function name in the string then we use full match operation


# import re
# a = input("Enter string to perform match operations :")
# mtch = re.fullmatch(a,"Pythonisvery")
# print(mtch)
# if mtch !=None :
#     print("Match found at beginning level")
#     print(mtch.start(),"",mtch.end())

# else :
#     print("There is no match")


# =============================================================================================================
           #SEARCH OPERATION    
            #if the match is found anywhere in the string it return object else it will return none


# import re
# a = input("Enter string to perform match operations :")
# mtch = re.search(a,"Python sss dynamic lann")
# print(mtch)
# if mtch !=None :
#     print(mtch.start(),"",mtch.end())

# else :
#     print("There is no match")


# =============================================================================================================

# findall function

# import re
# mtch = re.findall("[a-zA-Z0-9]","dfhjshUFbduYWU849@#$%^")
# print(mtch)

# =============================================================================================================

#SUB FUNCTION
        #This function perform a substitution or replacement 

# import re
# obj = re.sub("[a-zA-Z]","*","2345 ABCD Fabc deff")
# print(obj)


# =============================================================================================================

#SUB N FUNCTION
        #This function is similar ass sub() function only one thing is different that it also return 
        #the no. of replacement.This return in tuple where first element is 
        #the string and second is no. of replacement 

# import re
# obj = re.subn("[0-5]","@","ab3dg6nk17")
# print(obj)
# print("The string is =",obj[0])
# print("The no. of replacement =",obj[1])


# =============================================================================================================


#wap to check the valid phone number 

# import re
# mo = input("Enter phone number :")
# obj = re.fullmatch("[0-9]\d{9}",mo)
# if obj !=None :
#     print("Valid phone number")
# else :
#     print("Invalid phone number")


# =============================================================================================================


#wap to check the valid email id 

# import re
# email = input("Enter email id :")
# obj = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",email)
# if obj != None :
#     print("Valid email id")
# else :
#     print("Invalid email id")


# =============================================================================================================
#PRINT THE CONTENT OF THE FILE AND CHECK FILE EXISTENCE

# import os , sys
# fname = input("Enter file name :")

# if os.path.isfile(fname) :
#     print("File exist :",fname)
#     f = open(fname,"r")
# else :
#     print("File does not exist")
#     sys.exit(0)
# print("Content of file is :")
# data = f.read()
# print(data)

