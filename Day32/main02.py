class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Woof!")

dog = Dog()

dog.eat()
dog.bark()