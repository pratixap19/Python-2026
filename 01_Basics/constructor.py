class Student:
    college_name = "UMASS"
    
    #default constructor
    def __init__(self):
        pass
    
    #parameterized constructor
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
        print("adding new student in database..")
        
    def welcome(self):
        print("Welcome student")
        
    def get_marks(self):
        return self.marks
        
s1 = Student("Kyle", 88)
print(s1.name, s1.marks)
print(Student.college_name)
print(Student.get_marks)
s1.welcome()

s2 = Student("Shawn", 90)
print(s2.name, s2.marks)
print(Student.college_name)
s2.welcome()