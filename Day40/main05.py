class Character:
    count = 0
    def __init__(self, name, hp ,attack):
        self.name = name
        self.hp = hp
        self.attack = attack
        Character.count += 1

    def hit(self, target):
        target.hp -= self.attack
        if target.hp < 0:
            target.hp = 0

    def heal(self, amount):
        self.hp += amount

    def is_alive(self):
        return self.hp > 0

    def get_status(self):
        return f"{self.name}: {self.hp} HP"

knight = Character("Knight", 200, 40)
mage = Character("Mage", 120, 60)

knight.hit(mage)
mage.hit(knight)
knight.heal(20)
knight.hit(mage)
knight.hit(mage)

print(knight.get_status())
print(f"Knight alive: {knight.is_alive()}")
print(mage.get_status())
print(f"Mage alive: {mage.is_alive()}")
print(f"Total characters: {Character.count}")