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
        stone = self.stones.pop()
        stone.player.popSpike(self._index)
        return stone
    
    def peek(self):
        """
        Peek - returns the item at the top of jail

        Returns:
        Any - last added item
        """
        return self.stones.peek()
    
    def __str__(self):
        try:
            player = self.stones.peek().player
            return f"Jail - {colored((player.symbol) * len(self.stones), player.color)} - ({len(self.stones)})"
        except:
            return f"Jail - "