def login(username, password):
    if username == password:
        print("Login successful!")
    else:
            print("Login failed. Please try again.")

login(username="prashant", password="prashant")

def cityName(city="Goa"):
    print(city)

cityName("Pune")
cityName("Mumbai")
cityName()
    