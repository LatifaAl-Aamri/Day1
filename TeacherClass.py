from Person import Person
class Teacher(Person):

    #constructor
    def __init__(self, tname, tage, year, salary):
        super().__init__(tname, tage, salary)
        self.experiance_year = year
        
    def bouns(self):
        teacherB = super().get_bouns() * 2
        return teacherB
        
    def say_hi(self):
        print(super().say_hi())
        return f"Helloo {self.name} as Teacher"