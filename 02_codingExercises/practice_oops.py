#Create student class that takes name and marks of 3 subjects as arguments in constructor.
#Then create a method to print the average.

class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
        
    def get_avg(self):
        sum=0
        for value in self.marks:
            sum+=value
        print("Hi", self.name, "your avg score is:" , sum/3)
        
    @staticmethod #decorator, with the help of decorator "self" is nor required to pass it inside method
    def college():
        print("University ofMassachusetts")
        
s1=Student("Tony", [99,98,97])
s1.get_avg()
s1.college()
        