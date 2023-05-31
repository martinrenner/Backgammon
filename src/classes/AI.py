from src.classes.player import Player
from random import choice

class AI(Player):
    def __init__(self, increase, symbol, color, min, max):
        super().__init__(increase, symbol, color, min, max)
    
    def turn(self, possible_moves):
        #FROM ALL POSSIBLE MOVES RANDOM PICK
        chosen = choice(possible_moves)
        return chosen

    def moveStone(self):
        ...

    def moveToHome(self, stone):
        ...

        