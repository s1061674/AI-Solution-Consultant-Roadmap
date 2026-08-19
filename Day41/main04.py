class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def take_damage(target, damage):
        target.hp -= damage
        if target.hp < 0:
            target.hp = 0

    def is_alive(self):
        self.hp > 0

    def damage(self):
        return self.attack

class Knight(Character):
    def damage(self):
        return super().damage() + 20

class Mage(Character):
    def __init__(self, name, hp, attack, mana):
        super().__init__(name, hp, attack)
        self.mana = mana
    def damage(self):
        return super().damage() + 40

    def cast_spell(self, target):
        target.take_damage(self.damage())
        self.mana -= 20

knight = Knight("Arthur", 200, 30)
mage = Mage("Amy", 120, 40, 100)

mage.take_damage(knight.damage())
mage.cast_spell(knight)

characters = [knight, mage]

print(f"Arthur HP: {knight.hp}")
print(f"Amy HP: {mage.hp}")
for character in characters:
    print(f"{character.name} damage: {character.damage()}")
print(f"Amy mama: {mage.mana}")