class Enemy:
    def __init__(self, name, power):
            self.name = name
            self.power = power

    def __str__(self):
            return f"Enemy {self.name} - Power {self.power}"