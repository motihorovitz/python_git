from datetime import datetime
current_year = datetime.now().year
print(current_year)


class student:
    def __init__(self, name, year, id):
        self.name = name
        self.year = year
        self.id = id

    def year(self):
       return datetime.now().year - self.year





