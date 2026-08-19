class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def heal(self):
        self.hp += 10
    def get_status(self):
        return (f"{self.name}: {self.hp} HP")

class Paladin(Character):
    def heal(self):
        super().heal()
        self.hp += 20

paladin = Paladin("Arthur", 100)
paladin.heal()

print(paladin.get_status())