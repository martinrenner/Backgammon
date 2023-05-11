from node import Node

class Home(Node):
    def __init__(self, sumOfAllStones = 15):
        """
        Constructor - initialize home

        Parameters:
        sumOfAllStones (Int): number of stones that determine end of game
        """
        super().__init__()
        self.sumOfAllStones = sumOfAllStones

    def allStonesHome(self):
        """
        AllStonesHome - check if all stones are home

        Returns: 
        Bool - False unless all stones are home, otherwise True
        """
        return False if len(self.stones) < self.sumOfAllStones else True  