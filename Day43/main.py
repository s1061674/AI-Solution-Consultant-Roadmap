class Character:
    def __init__(self, name, level):
        self.name = name 
        self.level = level

    @classmethod
    def beginner(cls, name):
        return cls(name, 1)

    @classmethod
    def max_level(cls, name):
        return cls(name, 100)

p1 = Character("Arthur", 20)
p1 = Character.beginner("Arthur")
p2 = Character.max_level("Amy")

print(f"Arthur Level: {p1.level}")
print(f"Amy Level: {p2.level}")