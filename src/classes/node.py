from src.classes.stack import Stack

class Node:
    """
    Node class
    """

    def __init__(self, index):
        """
        Constructor - initialize node
        """
        self._stones = Stack()
        self._index = index

    @property
    def stones(self):
        return self._stones
    
    @property
    def index(self):
        return self._index

    def push(self, stone):
        """
        Push - push stone to the stack of selected node

        Parameters:
        stone (Any): stone to be added into stack

        Returns: 
        None
        """
        self.stones.push(stone)

    def isEmpty(self):
        """
        IsEmpty - determines whether node is empty or not

        Returns: 
        Bool - False if empty, True if not empty
        """
        return False if len(self.stones) else True

    def __len__(self):
        """
        len - return number of stones

        Returns: 
        Int - number of stones in the stack
        """
        return len(self.stones)