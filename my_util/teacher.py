from .student import *

class Teacher():
    def __init__(self,name):
        self.name=name

    def yell(self):
        print(self.name+"!!!!!")

def sum(a,b):
    return(a+b)

class BadStudent(Student):
    def __init__(self, name,major,gpa,status):
        self.gpa=1.0

def test():
    test_student=Student("Mee","Math",4.0,True)
    print(test_student.name+" Test!")