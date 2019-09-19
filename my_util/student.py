#class a group of varuable, function within one object
class Student:
    def __init__(self, name,major,gpa,status):
        self.name=name
        self.major=major
        self.gpa=gpa
        self.status=status

class GoodStudent(Student):
    def __init__(self, name,major,gpa,status):
        self.gpa=4.0
