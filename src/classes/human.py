from src.classes.player import Player

class Human(Player):
    def __init__(self, name, increase, symbol, color, min, max, toHomeArea):
        super().__init__(name, increase, symbol, color, min, max, toHomeArea)

    def turn(self, possible_moves):
        """
        Turn - prints all the possible moves along with an index that user can choose from
        
        Parameters: 
        possible_moves: A list of tuples representing possible moves. Each tuple contains three elements: start, step, and end.
        
        Returns: 
        tuple representing the move selected by the user. The tuple contains three elements: start, step, and end.
        """
        possibilities = ""
        i = 0
        for start, step, end in possible_moves:
            possibilities += f"[{i}] {start} -> {end} ({step}),\t"
            i += 1
        print(possibilities)
        print("----------------------------------------")
        choice = input("CHOOSE POSSIBLE MOVE: ")
        while not ((int)(choice) >= 0 and (int)(choice) < i):
            choice = input(f"Invalid choice. Choose option (0-{i-1}): ")
        return possible_moves[(int)(choice)]
    
    # def moveStone(self):
    #     ...

    # def moveToHome(self, stone):
    #     ...
