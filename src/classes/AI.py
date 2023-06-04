from src.classes.player import Player
from random import choice


class AI(Player):
    """
    AI player class
    """

    def __init__(self, name, increase, symbol, color, to_home_area):
        super().__init__(name, increase, symbol, color, to_home_area)

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
