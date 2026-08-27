from dataclasses import dataclass, field
@dataclass
class Player:
    name: str  
    level: int
    items: list[str]= field(default_factory=list)
    power: int = field(init=False)

    def __post_init__(self):
        if self.level < 1:
            raise ValueError("Level must be at least 1")

        self.power = self.level * 10

p1 = Player("Arthur", 50)
p2 = Player("Amy", 30)

p1.items.append("Sword")
p2.items.append("Staff")

print(p1)
print(p2)

try:
    p3 = Player("Bob", 0)
    print("Player created")
except ValueError as e:
    print(e)