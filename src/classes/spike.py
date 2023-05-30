from src.classes.node import Node
from termcolor import colored
from src.classes.colors import Colors

class Spike(Node):
    """
    Spike class
    """

    def __init__(self, index):
        """
        Constructor - initialize spike
        """
        super().__init__(index)

    def __str__(self):
        try:
            player = self.stones.peek().player
            return f"{self.index:02d} - {colored((player.symbol) * len(self.stones), player.color)}"
        except:
            return f"{self.index:02d} - "
        