class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Dog: {self.name}, Age: {self.age}"

dog = Dog("Lucky", 3)

print(dog)
