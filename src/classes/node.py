from classes.stack import Stack

class Node:
    """
    Node class
    """

    def __init__(self):
        """
        Constructor - initialize node
        """
        self.stones = Stack()

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
        Push - push stone to the stack of selected node

        Parameters:
        stone (Any): stone to be added into stack

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
    

#---------------------------------------------------------
#                       TEST DATA
#---------------------------------------------------------
if __name__ == "__main__":
    test_node = Node()
    assert test_node.isEmpty() == True, "Node should be empty"
    assert len(test_node) == 0, "Node should be empty"
    test_node.push("TEST")
    assert test_node.isEmpty() == False, "Node should not be empty"
    assert len(test_node) == 0, "Node should not be empty"
