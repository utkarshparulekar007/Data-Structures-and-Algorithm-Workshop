class SubMarks :
    math = int(input("Enter the marks of math: "))
    DE = int(input("Enter the marks of DE: "))
    english = int(input("Enter the marks of english: "))

class PractMarks :
    cpract = int(input("Enter the marks of c language  : "))

class Result (SubMarks ,PractMarks):
    def total(self) :
        if self.math >= 40 and self.DE >= 40 and self.english >= 40 and self.cpract >= 40 :
           print("Pass")    
        else :
            print("Fail")
obj = Result()
obj.total()   