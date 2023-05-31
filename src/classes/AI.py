from src.classes.player import Player
from random import choice

class AI(Player):
    def __init__(self, name, increase, symbol, color, min, max, toHomeArea):
        super().__init__(name, increase, symbol, color, min, max, toHomeArea)
    
    def turn(self, possible_moves):
        #FROM ALL POSSIBLE MOVES RANDOM PICK
        chosen = choice(possible_moves)
        return chosen

    def moveStone(self):
        ...

    def moveToHome(self, stone):
        ...

        