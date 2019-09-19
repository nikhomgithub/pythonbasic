"""
#class a group of varuable, function within one object
class Student:
    def __init__(self, name,major,gpa,status):
        self.name=name
        self.major=major
        self.gpa=gpa
        self.status=status
"""

from my_util import student
from my_util.teacher import Teacher
from my_util.teacher import sum
from my_util.teacher import BadStudent
from cal import square
from my_util.student import GoodStudent
from my_util.teacher import test

student1 = student.Student("Peter","Math",3.1,True)
print(student1.name)
#Peter

good_student = GoodStudent("Mic","Math",2.1,True)
print(good_student.gpa)
#4.0

bad_student = BadStudent("Kug","Math",3.0,True)
print(bad_student.gpa)
#1.0

teacher1 = Teacher("Jim")
print(teacher1.name)
#Jim

teacher1.yell()
#Jim!!!!!

print(sum(1,2))
#3
print(square(2))
#4

test()