class Player:
    def __init__(self, name: str , level: int):
        self.name = name
        self.level = level

def filter_players(
    players: list[Player],
    min_level: int,
    ) -> list[Player]:
    
    result: list[Player] = []

    for player in players:
        if player.level >= min_level:
            result.append(player)

    return result
    
p1 = Player("Arthur", 50)
p2 = Player("Amy", 30)
p3 = Player("Knight", 80)
p4 = Player("Bob", 20)

result = filter_players([p1, p2, p3, p4], 50)
for player in result:
    print(player.name)
