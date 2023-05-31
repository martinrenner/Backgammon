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

    def peek(self):
        """
        Peek - returns the item at the top of spike

        Returns:
        Any - last added item
        """
        return self.stones.peek()
    
    def pop(self):
        """
        Pop - removes and returns item at the top of spike

        Returns:
        Any - removed item
        """
        stone = self.stones.pop()
        stone.player.popSpike(self._index)
        return stone

    def __str__(self):
        try:
            player = self.stones.peek().player
            return f"{self.index:02d} - {colored((player.symbol) * len(self.stones), player.color)}"
        except:
            return f"{self.index:02d} - "
        