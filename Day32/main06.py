class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")


class Student(Person):
    def __init__(self, name, score):
        super().__init__(name)
        self.score = score

    def introduce(self):
        super().introduce()
        print(f"My score is {self.score}")


student = Student("Alice", 95)
student.introduce()