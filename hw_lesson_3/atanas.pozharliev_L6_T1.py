class SchoolMember():
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        self.courses = {}

    def getSalary(self):
        return self.salary

    def addCourse(self, signature, name):
        self.courses[signature] = name

    def getCourses(self):
        for signature, name in self.courses.items():
            print(f"{signature} {name}")


class Student(SchoolMember):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.courses = {}

    def attendCourse(self, signature, year):
        self.courses[signature] = {
            "grades": [],
            "year": year
        }

    def addGrade(self, signature, grade):
        if signature in self.courses:
            self.courses[signature]["grades"].append(grade)

    def getCourses(self):
        for signature, course_info in self.courses.items():
            print(f"{signature} {course_info}")

    def getAvgGrade(self, signature):
        if signature in self.courses:
            grades = self.courses[signature]["grades"]
            if len(grades) > 0:
                return sum(grades) / len(grades)
        return None
