class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

dog = Dog("Lucky", 3)

print(dog.name) 
print(dog.age)   
