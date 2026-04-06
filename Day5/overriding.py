class Rbi :
    def home_loan(self) :
        print("Home loan = 8%")
    def car_loan(self) :
        print("Car loan = 9.4%")

    def education_loan(self) :
        print("Education loan = 6.8%")

class Sbi(Rbi) :
    def home_loan(self) :
        print("Sbi provides Home loan = 7%")
        super().home_loan()     #Using super method you can access parent class method in the child class

obj = Sbi()
obj.home_loan()
obj.car_loan()