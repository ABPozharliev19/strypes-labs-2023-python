

class SchoolMember:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Course:
    def __init__(self, name: str, year: str, marks: list):
        self.name = name
        self.year = year
        self.marks = marks


class Teacher(SchoolMember):
    _salary: float = None
    _courses: list = None

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def set_salary(self, salary: float):
        self._salary = salary

    def set_courses(self, courses: list):
        self._courses = courses


class Student(SchoolMember):
    _courses: list = None

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def set_courses
