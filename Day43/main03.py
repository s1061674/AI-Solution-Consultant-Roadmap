class GameCharacter:
    character_count = 0
    max_level = 100

    def __init__(self, name, level, attack, defense):
        self.name = name
        self.level = level
        self.attack = attack
        self.defense = defense
        GameCharacter.character_count += 1

    def calculate_power(self):
        return self.attack + self.defense

    @classmethod
    def beginner(cls, name):
        return cls(name, 1, 20, 10)

    @classmethod
    def get_character_count(cls):
        return cls.character_count

    @staticmethod
    def is_valid_level(level):
        return 0 < level <= 100

p1 = GameCharacter.beginner("Arthur")
p2 = GameCharacter("Amy", 50 , 80, 40)
result1 = p1.calculate_power()
result2 = p2.calculate_power()

print(f"Arthur Level: {p1.level}")
print(f"Arthur Power: {result1}")
print(f"Amy Level: {p2.level}")
print(f"Amy Power: {result2}")
print(f"Character Count: {GameCharacter.get_character_count()}")
print(f"Valid Stat 50: {GameCharacter.is_valid_level(50)}")
print(f"Valid Stat 150: {GameCharacter.is_valid_level(150)}")