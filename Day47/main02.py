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

    def is_inventory_full(self) -> bool:
        return self.get_item_count() >= 3
    
    def add_item(self, item: str) -> bool:
        if self.is_inventory_full():
            return False

        self.items.append(item)
        return True

    def get_item_count(self) -> int:
        return len(self.items)
    
p1 = Player("Arthur", 50)

p1.add_item("Sword")
p1.add_item("Potion")
p1.add_item("Shield")

print(p1)
print(p1.get_item_count())
print(p1.is_inventory_full())
result = p1.add_item("Armor")
print(result)



