from datetime import datetime
# print(current_year)


class Student:
    def __init__(self, name, year, id):
        self.name = name
        self.year = year
        self.id = id

    def c_year(self):
       return datetime.now().year - self.year

    def list_stu(self):
        return len(self.name)

student = Student("moti", 2001, 2122345)
print(student.c_year())





