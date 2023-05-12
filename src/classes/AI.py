from .player import Player

class AI(Player):
    def __init__(self):
        super().__init__()
    
    def moveStone(self):
        ...

    def moveToHome(self, stone):
        ...

        