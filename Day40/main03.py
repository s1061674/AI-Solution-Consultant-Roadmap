class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
 
    def heal(self, amount):
        self.hp += amount

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0

    def get_status(self):
        return f"{self.name}: {self.hp} HP"
   
knight = Player("Knight", 100)
mage = Player("Mage", 80)

knight.take_damage(30)
knight.heal(10)
mage.take_damage(100)

print(knight.get_status())
print(f"Knight alive: {knight.is_alive()}")
print(mage.get_status())
print(f"Mage alive: {mage.is_alive()}")