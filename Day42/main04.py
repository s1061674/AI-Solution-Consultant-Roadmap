class GameAccount:
    def __init__(self, name, gold, level):
        self.name = name
        self.__gold = gold
        self.__level = level

    @property
    def gold(self):
        return self.__gold

    @property
    def level(self):
        return self.__level

    def earn_gold(self, amount):
        if amount <= 0:
            raise ValueError("金幣增加量必須大於 0")
        else:
            self.__gold += amount

    def spend_gold(self, amount):
        if amount <= 0:
            raise ValueError("消費金額必須大於 0")
        elif amount > self.__gold:
            return False
        else:
            self.__gold -= amount
            return True

    def level_up(self):
        self.__level += 1

account = GameAccount("Arthur", 100, 1)

account.earn_gold(50)
result2 = account.spend_gold(80)
account.level_up()

try:
    account.earn_gold(-20)
except ValueError as e:
    error = str(e)

result4 = account.spend_gold(100)

print(f"Name: {account.name}")
print(f"Gold: {account.gold}")
print(f"Level: {account.level}")
print(f"First purchase: {result2}")
print(error)
print(f"Second purchase: {result4}")
