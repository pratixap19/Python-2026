class Person: #class starts from here
    __name="anonymous"
    
    def __init__(self, name):
        self.__name=name
    
    def __hello(self):
        print("Hello", self.__name)
        
    def welcome(self):
        self.__hello()
#class end here      
p1 = Person("Pratixa")
p1.welcome()
print(p1._Person__name) #Python secretly renamed __name to _Person__name.