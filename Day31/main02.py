class Student:

    school = "Python School"

    def __init__(self, name):
        self.name = name

student1 = Student("Alice")
student2 = Student("Bob")

print(student1.name)  
print(student2.name)  

student1.school = "AI School"

print(student1.school)  
print(student2.school)  