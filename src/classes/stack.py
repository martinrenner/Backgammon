class Stack:
    """
    Abstract data type Stack
    """

    def __init__(self):
        """
        Constructor - initialize empty stack
        """
        self.__data = []

    def push(self, item):
        """
        Push - insert item at the top of stack

        Parameters:
        item (Any): item to be added

        Returns: 
        None
        """
        self.__data.append(item)

    def pop(self):
        """
        Pop - removes and returns item at the top of stack

        Returns:
        Any - removed item
        """
        return self.__data.pop()

    def peek(self):
        """
        Peek - returns the item at the top of stack

        Returns:
        Any - last added item
        """
        return self.__data[-1]

    def isEmpty(self):
        """
        IsEmpty - determines whether stack is empty or not

        Returns:
        Boolean - true if empty
        """
        return not self.__data 