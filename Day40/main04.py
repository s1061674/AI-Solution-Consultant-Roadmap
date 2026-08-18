class Monster:
    count = 0

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        Monster.count += 1

goblin = Monster("Goblin", 100)
orc = Monster("Orc", 150)     
dragon = Monster("Dragon", 500)

print(f"{goblin.name}: {goblin.hp} HP")
print(f"{orc.name}: {orc.hp} HP")
print(f"{dragon.name}: {dragon.hp} HP")

print(f"Total monsters: {Monster.count}")