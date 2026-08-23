class Player:
    def __init__(self, name, level , power):
        self.name = name
        self.level = level
        self.power = power

    def __str__(self):
        return f"{self.name} - Level {self.level} - Power {self.power}"

    def __repr__(self):
        return f"Player('{self.name}', {self.level}, {self.power})"

    def __eq__(self, other):
        return self.power == other.power


    def __lt__(self, other):
        return self.power < other.power

p1 = Player("Arthur", 50 , 100)
p2 = Player("Amy", 40, 150)
p3 = Player("Knight", 60 ,100)

print(p1)
print(repr(p1))

print(p1 == p3)

players = [p1, p2, p3]
result = sorted(players)

for player in result:
    print(player)