from Person import Person
from StudentClass import Student
from TeacherClass import Teacher
def main():
    Hanna = Person("Hanna Al-Zadjali", 23, 20000)
    person2 = Person("Hamza")
    
    std1 = Student("Latifa", 18, 2021)
    std2 = Student("Harith", 21, 2022)
    
    teacher1 = Teacher("Dr.Mohammed" , 33, 5)
    teacher2 = Teacher("AB" , 25, 3)
    
    print(person2.descrip())
    print(Hanna.get_name())
    Hanna.set_name("Hanaa Abdulwahab Al-Zadjali")
    print(Hanna.get_name())
    print(Hanna.descrip())
    Hanna.run()
    Hanna.laugh()
    person2.laugh()
    
    print(std1.say_hi())
    print(Student.say_hi(std2))
    std1.run()
    
    print(teacher1.say_hi())
    print(Student.say_hi(teacher2))
    teacher1.laugh()
    
    print(Hanna.say_hi())
    print(Person.say_hi(person2))
    
    """
    std2.run()
    print(teacher1.say_hi())
    print(Teacher.say_hi(teacher2))
    teacher1.laugh()
    """
      
main()