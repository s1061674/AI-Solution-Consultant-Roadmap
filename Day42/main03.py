class Player:
    def __init__(self, name ,gold):
        self.name = name
        self.__gold = gold

    @property
    def gold(self):
        return self.__gold

    def earn_gold(self, amount):
        if amount > 0:
            self.__gold += amount

    def spend_gold(self, amount):
        if self.__gold >= amount:
            self.__gold -= amount
            return True
        return False

knight = Player("Knight", 100)

knight.earn_gold(50)
result1 = knight.spend_gold(80)
result2 = knight.spend_gold(100)

print(f"Knight Gold: {knight.gold}")
print(f"First purchase: {result1}")
print(f"Second purchase: {result2}")