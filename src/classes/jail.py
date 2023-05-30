from src.classes.node import Node
from termcolor import colored
from src.classes.colors import Colors

class Jail(Node):
    """
    Jail class
    """

    def __init__(self, index = "J"):
        """
        Constructor - initialize home
        """
        super().__init__(index)

    def pop(self):
        """
        Pop - pops stone from jail

        Returns: 
        Any - removed item
        """
        return self.stones.pop()
    
    def __str__(self):
        try:
            player = self.stones.peek().player
            return f"Jail - {colored((player.symbol) * len(self.stones), player.color)}"
        except:
            return f"Jail - "