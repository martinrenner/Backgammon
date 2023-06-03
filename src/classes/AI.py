from src.classes.player import Player
from random import choice

class AI(Player):
    def __init__(self, name, increase, symbol, color, toHomeArea):
        super().__init__(name, increase, symbol, color, toHomeArea)
    
    def turn(self, possible_moves):
        """
        Turn - choose a random move from the given list of possible moves
        
        Parameters:
        possible_moves: A list of possible moves

        Returns: 
        tuple representing the move selected by AI. The tuple contains three elements: start, step, and end.
        """
        chosen = choice(possible_moves)
        return chosen

    # def moveStone(self):
    #     ...

    # def moveToHome(self, stone):
    #     ...

        