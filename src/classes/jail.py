from src.classes.node import Node

class Jail(Node):
    def __init__(self):
        """
        Constructor - initialize home
        """
        super().__init__()

    def pop(self):
        """
        pop - pops stone from jail

        Returns: 
        Any - removed item
        """
        return super().stones.pop()