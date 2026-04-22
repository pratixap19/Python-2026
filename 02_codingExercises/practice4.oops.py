#Define a Employee class with attributes role, department and salary. This class has
#showDetails() method.
#Create an Engineer class that inherits properties from Employee & has additional
#attributes:name & age.

class Employee:
    
    def __init__(self, role, dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
        
    def showDetails(self):
        print("Role =" , self.role)
        print("Dept =" , self.dept)
        print("Salary =" , self.salary)
        
class Engineer(Employee): #inheritance
    
    def __init__(self, name, age):
        self.name=name
        self.age=age
        super().__init__("Engineer", "IT", "75000")
        
e1 = Employee("Accountant", "Finance", "60000")  
print(e1.showDetails())

engg1=Engineer("Dyllan", 35)
engg1.showDetails()
    