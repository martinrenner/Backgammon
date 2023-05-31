from src.classes.player import Player

class Human(Player):
    def __init__(self, increase, symbol, color):
        super().__init__(increase, symbol, color)

    #possible_moves je list, kazdy prvek je list [z jakeho spiku, posun o kolik]
    def turn(self, possible_moves):
        #PRINT ALL POSSIBLE MOVES & USER INPUT CHOOSE FROM IT
        possibilities = ""
        i = 0
        for start, step, end in possible_moves:
            possibilities += f"[{i}] {start} -> {end}, "
            i += 1
        print(possibilities)
        choice = input("CHOOSE POSSIBLE MOVE: ")
        while not ((int)(choice) >= 0 and (int)(choice) < i):
            choice = input(f"Invalid choice. Choose option (0-{i-1}): ")
        return possible_moves[(int)(choice)]
    
    def moveStone(self):
        ...

    def moveToHome(self, stone):
        ...
