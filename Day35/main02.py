class Animal:
    pass

class Dog(Animal):
     pass

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()

print(type(dog) == Dog)
print(type(dog) == Animal)
print(isinstance(dog, Animal))
print(type(cat) == Dog)