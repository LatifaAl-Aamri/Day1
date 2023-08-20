class Person:
    #constructr to creat bjects
    #initialize istance varibles
    
    def __init__(self,name, age, salary):
        self.name = name
        self.age= age
        self.salary = salary
        
    def bouns(self):
        b = self.salary * 0.005
        return b
        
    def say_hi(self):
        return f"Hi you {self.name} as Person"
    
    #use term of encapsulation
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    
    #setter / mutotur methods
    def set_name(self,newName):
        self.name = newName
    def set_age(self, newAge):
        self.age = newAge
        
    #printing a string
    def run(self):
        print(self.name ," is running")
        
    #returning a string
    def descrip(self):
        return f"Person name {self.name} is {self.age} years old"
    def laugh(self):
        print(self.name, ' say hahahaha')
    
