class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def heal(self):
        self.hp += 20

monster1 = Monster("Goblin", 100)

monster1.heal()

print(f"Name: {monster1.name}")
print(f"HP: {monster1.hp}")