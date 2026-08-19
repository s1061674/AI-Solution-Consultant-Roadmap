class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def get_status(self):
        return (f"{self.name}: {self.hp} HP")
    
class Mage(Character):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana
    def cast_spell(self):
        self.mana -= 20

mage = Mage("Amy", 100, 80)  
mage.cast_spell()

print(mage.get_status())
print(f"Mana: {mage.mana}")