class Character:
    def __init__(self, name, level , hp):
        self.name = name
        self.level = level
        self.hp = hp

    def __str__(self):
        return (f"{self.name} - Level {self.level} - HP {self.hp}")

    def __repr__(self):
        return (f"Character('{self.name}', {self.level}, {self.hp})")

c1 = Character("Arthur", 50, 200)
c2 = Character("Amy", 30, 150)

print(c1)
print(repr(c1))

characters = [c1, c2]
print(characters)