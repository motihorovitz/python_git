from datetime import datetime
current_year = datetime.now().year
print(current_year)


class Student:
    def __init__(self, name, year, id):
        self.name = name
        self.year = year
        self.id = id

    def year(self):
       return datetime.now().year - self.year

    def list_stu(self):
        return len(self.name)






