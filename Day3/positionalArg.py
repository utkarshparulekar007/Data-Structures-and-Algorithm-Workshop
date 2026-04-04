def login(username, password):
    if username == password:
        print("Login successful!")
    else:
            print("Login failed. Please try again.")


username = input("Enter your username: ")
password = input("Enter your password: ")       

login(username, password)


