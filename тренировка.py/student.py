class Student:


    def __init__(self, firstname, surname, age, course):
        self.firtsname = firstname
        self.surname = surname
        self.age = age
        self.course = course


    def __str__(self):
        return f"{self.firtsname} {self.surname}, {self.age} лет, курс: {self.course}"