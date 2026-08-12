class Animal:
    pass

class Dog(Animal):
     pass

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(cat, Animal))
print(isinstance(cat, Dog))