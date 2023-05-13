from src.classes.node import Node

class Jail(Node):
    """
    Jail class
    """

    def __init__(self):
        """
        Constructor - initialize home
        """
        super().__init__()

    def pop(self):
        """
        Pop - pops stone from jail

        Returns: 
        Any - removed item
        """
        return self.stones.pop()