
class Player:

    def __init__(self, name, icon):
        self.name = name
        self.icon = icon


    def draw(self):
        return self.icon


    def __str__(self):
        return self.name
