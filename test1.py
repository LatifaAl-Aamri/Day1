
from Person import Person
from TeacherClass import Teacher
def main():
    p1 = Person('Ahmed', 24, 1500)
    print(p1.descrip())
    print(p1.bouns())
    teacher1 = Person('Ali', 44, 1500)
    print(teacher1.descrip())
    print(teacher1.bouns())
    
main()