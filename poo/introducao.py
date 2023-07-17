class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grade = grades

    def avarage_grade(self):
        return sum(self.grade) / len(self.grade)
    

student = Student("Bob", ( 90,90,93,78,90 ))
print(student.name)
print(student.avarage_grade())