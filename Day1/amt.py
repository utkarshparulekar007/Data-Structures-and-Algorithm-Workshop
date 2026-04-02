p_amount = int(input("Enter principal amount"))
roi = int(input("Enter roi amount"))
time = int(input("Enter duration"))

si = p_amount*roi*time/100
print ("Simple interest=",si)