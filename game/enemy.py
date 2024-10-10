class Enemy:
    def __init__(self, name, description, weapon ,health):
        self.name = name
        self.description = description
        self.weapon = weapon
        self.health = health

    def __str__(self):
        return f"Enemy: {self.name}, {self.description}, Item: {self.weapon}"