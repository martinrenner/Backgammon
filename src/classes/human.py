from src.classes.player import Player

class Human(Player):
    def __init__(self, increase, symbol, color):
        super().__init__(increase, symbol, color)

    #possible_moves je list, kazdy prvek je list [z jakeho spiku, posun o kolik]
    def turn(self, possible_moves, rolled):
        #PRINT ALL POSSIBLE MOVES & USER INPUT CHOOSE FROM IT
        for move_index in range(possible_moves):
            print(f"[{move_index + 1}] {possible_moves[0]} -> {possible_moves[0] + possible_moves[0]}", sep=", ")
        print(possible_moves)
        chosen = input("CHOOSE POSSIBLE MOVE: ")
        while not (choice >= 1 and choice <= len(possible_moves)):
            choice = input("Invalid choice. ")
        return chosen - 1
    
    def moveStone(self):
        ...

    def moveToHome(self, stone):
        ...
