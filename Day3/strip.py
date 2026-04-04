# rstrip()==> To remove spaces at r.h.s
#lstrip()==> To remove the spaces at l.hs
#strip()==> To remove the spaces bothe sides 
programming = input(int("Enter"))
p_name = programming.rstrip()
if p_name == 'Python':
   print(p_name)
elif p_name == 'Java' :
   print(p_name)
else :
   print("Wrong")
