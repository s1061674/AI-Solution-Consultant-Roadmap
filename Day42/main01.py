class Player:
    def __init__(self, name , hp):
        self.name = name
        self.__hp = hp

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
         if value >= 0:
            self.__hp = value

knight = Player("Knight", 100)

knight.hp = 150
knight.hp = -500

print(f"Name: {knight.name}")
print(f"HP: {knight.hp}")
print(f"HP: {knight.hp}")