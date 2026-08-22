class Player:
    player_count = 0

    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense
        Player.player_count += 1

    def calculate_power(self):
        return self.attack + self.defense

    @classmethod
    def get_player_count(cls):
        return Player.player_count

    @staticmethod
    def is_valid_stat(value):
        return 0 < value < 100

p1 = Player("Arthur", 50, 30)
p2 = Player("Amy", 80, 40)

result1 = p1.calculate_power()
result2 = p2.calculate_power()

print(f"Arthur Power: {result1}")
print(f"Amy Power: {result2}")
print(f"Player Count: {Player.get_player_count()}")
print(f"Valid Stat 50: {Player.is_valid_stat(50)}")
print(f"Valid Stat 150: {Player.is_valid_stat(150)}")