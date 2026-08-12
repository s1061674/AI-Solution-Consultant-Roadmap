class Animal:
    pass

class Dog(Animal):
     pass

class Cat(Animal):
    pass

print(issubclass(Dog, Animal))
print(issubclass(Cat, Animal))
print(issubclass(Dog, Cat))
print(issubclass(Animal, Dog))