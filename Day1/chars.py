ch = ord(input("Enter the character:"))
if ch>65 and ch<=91:
  print("Your charaacter is in upper case")
elif ch>=97 and ch<=122:
  print("Your entered character is in lower case")
elif ch>=48 and ch<=57:
  print("Your character is digit")
else:
  print("Your character is special symbol")