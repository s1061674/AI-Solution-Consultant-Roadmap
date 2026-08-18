class Player:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def hit(self, target):
        target.hp -= self.attack
    def heal(self, amount):
        self.hp += amount

knight = Player("Knight", 200, 30)
mage = Player("Mage", 120, 50)

knight.hit(mage)
mage.hit(knight)
knight.heal(20)
knight.hit(mage)

print(f"Knight HP: {knight.hp}")
print(f"Mage HP: {mage.hp}")