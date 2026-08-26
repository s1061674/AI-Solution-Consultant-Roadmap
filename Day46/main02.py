class Player:
    def __init__(self, name: str , level: int):
        self.name = name
        self.level = level

def find_players(
    players: list[Player],
    name: str
    ) -> Player | None:

    for player in players:
        if player.name == name:
            return player

    return None

p1 = Player("Arthur", 50)
p2 = Player("Amy", 30)
p3 = Player("Knight", 80)

players = [p1, p2, p3]

result1 = find_players(players, "Amy")
result2 = find_players(players, "Bob")


if result1 is not None:
    print(f"{result1.name} - Level {result1.level}")
else:
    print("Player not found")

if result2 is not None:
    print(f"{result2.name} - Level {result2.level}")
else:
    print("Player not found")



