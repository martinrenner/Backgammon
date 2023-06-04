from src.classes.node import Node
from termcolor import colored
from src.classes.colors import Colors


class Home(Node):
    """
    Home class
    """

    def __init__(self, index="H", sum_of_all_stones=15):
        """
        Constructor - initialize home

        Parameters:
        sumOfAllStones (Int): number of stones that determine end of game
        """
        super().__init__(index)
        self._sumOfAllStones = sum_of_all_stones

    def allStonesHome(self):
        """
        AllStonesHome - check if all stones are home

        Returns:
        Bool - False unless all stones are home, otherwise True
        """
        return False if len(self.stones) < self._sumOfAllStones else True

    def __str__(self):
        try:
            player = self.stones.peek().player
            return f"Home - {colored((player.symbol) * len(self.stones), player.color)} - ({len(self.stones)})"
        except:
            return f"Home - "
