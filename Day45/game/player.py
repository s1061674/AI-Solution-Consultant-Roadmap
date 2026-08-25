class Player:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __str__(self):
        return f"Player {self.name} - Power {self.power}"

