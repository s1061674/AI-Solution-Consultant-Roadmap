class Character:
    def __init__(self, name):
        self.name = name
    def damage(self):
        return 10


class Knight(Character):
    def damage(self):
        return super().damage() + 20


class Mage(Character):
    def damage(self):
        return super().damage() + 40

knight = Knight("Arthur")
mage = Mage("Amy")
characters = [knight, mage]

total = 0

for character in characters:
    total += character.damage()

print(f"Arthur damage: {knight.damage()}")
print(f"Amy damage: {mage.damage()}")
print(f"Total damage: {total}")