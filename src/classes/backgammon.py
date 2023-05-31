from src.classes.spike import Spike
from src.classes.AI import AI
from src.classes.human import Human
from src.classes.stone import Stone
from src.classes.colors import Colors
from src.classes.dice import Dice
from sys import exit
from os import system
from termcolor import colored

NUM_SPIKES = 24
STONES_LAYOUT = [2,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,3,0,5,0,0,0,0,0]

class Backgammon:
    """
    Backgammon game class
    """
    def __init__(self):
        """
        Constructor - initialize game board + dice
        """
        self.spike_list = [Spike(i) for i in range(NUM_SPIKES)]
        self.dice = Dice()

    def run(self):
        """
        Run - runs the game 
        First prompts the user to select a game mode, either Player vs Player or Player vs AI. 
        If Player vs Player is selected, the game will instantiate two Human objects, one for each player, and they will play against each other. 
        If Player vs AI is selected, the game will instantiate a Human object for the first player and an AI object for the second player, and they will play against each other. 
        If any other value is entered, the function will exit. 
        The function then creates stones and starts the game.
        """
        mode = self.menu()
        self.clear_console()
        if mode == 1:
            # Player vs Player
            self.player_one = Human("+", "X", Colors.red)
            self.player_two = Human("-", "Y", Colors.blue)
        elif mode == 2:
            # Player vs AI
            self.player_one = Human("+", "X", Colors.red)
            self.player_two = AI("-", "Y", Colors.blue)
        else:
            exit()

        self.player_one.oppositePlayer = self.player_two
        self.player_two.oppositePlayer = self.player_one

        self.create_stones()
        self.start_game()

    def start_game(self):
        """
        Start_game - runs the game loop until one of the players has all their stones in their home
        
        Returns: 
        None
        """
        current_player = self.player_one
        while True:
            rolled = self.roll_double_dice()
            while rolled:
                self.game_layout(rolled)
                possible_moves = self.all_possible_moves(rolled, current_player)
                if not possible_moves:
                    break
                choice_index = current_player.turn(possible_moves)
                rolled.remove(possible_moves[choice_index][1])
                current_player.move()
                if self.player_one.home.allStonesHome() or self.player_two.home.allStonesHome():
                    break
            if self.player_one.home.allStonesHome() or self.player_two.home.allStonesHome():
                break
            current_player = current_player.oppositePlayer
        self.end_statistics()

    def menu(self):
        """
        Menu - displays a menu for the Backgammon game and prompts the user to select an option
        
        Returns: 
        Int - representing the user's choice (Either 1, 2, or 3)
        """
        self.clear_console()
        print("BACKGAMMON GAME")
        print("-" * 40)
        print("Created by: Martin Renner")
        print("-" * 40)
        print("1 - Player vs Player")
        print("2 - Player vs AI")
        print("3 - Exit")
        choice = input("Choose menu option (1-3): ")
        while choice not in ('1', '2', '3'):
            choice = input("Invalid choice. Choose menu option (1-3): ")
        return int(choice)

    def clear_console(self):
        """
        Clear_console - clears the console screen

        Returns:
        None
        """
        system('cls')

    def create_stones(self):
        """
        Create_stones - creates stones for the game board by pushing them onto the spikes of the board
        
        Returns:
        None
        """
        for i in range(NUM_SPIKES):
            for _ in range(STONES_LAYOUT[i]):
                self.spike_list[i].push(Stone(i, self.player_one))
                self.spike_list[NUM_SPIKES - i - 1].push(Stone(NUM_SPIKES - i - 1, self.player_two))

    def game_layout(self, rolled):
        """
        Game_layout - prints the current state of the backgammon board and the rolled dice.
        
        Parameters:
        rolled (list(int)): list of integers representing the values of the rolled dicies.
        
        Returns:
        None
        """
        self.clear_console()
        print("BACKGAMMON GAME")
        print("- " + colored("PLAYER 2", self.player_two.color) + " -----------------------------")
        print(self.player_two.home)
        print(self.player_two.jail)
        print("-------------------------")
        for spike in self.spike_list:
            print(spike)
        print("- " + colored("PLAYER 1", self.player_one.color) + " -----------------------------")
        print(self.player_one.jail)
        print(self.player_one.home)
        print("----------------------------------------")
        print(f"ROLL: {rolled}")
        print("----------------------------------------")

    def debug(self):
        """
        Debug - prints the spikes of both players for debugging purposes

        Returns:
        None
        """
        print("---------DEBUG--------------------------")
        print(self.player_one._spikes)
        print(self.player_two._spikes)

    def roll_double_dice(self):
        """
        Roll_double_dice - rolls two dicies; If the two numbers are the same, the function returns a list of four numbers.
        
        Returns:
        rolls(list(int)): a list of two or four integers, representing the result of rolling the dice.
        """
        rolls = [self.dice.roll(), self.dice.roll()]
        if rolls[0] == rolls[1]:
            rolls *= 2
        return rolls
    
    def all_possible_moves(self, rolled, current_player):
        unique_spikes = set(current_player.spikes)
        unique_rolls = set(rolled)
        possible_moves = []

        #check jail
        if not current_player.jail.isEmpty():
            for roll in unique_rolls:
                destination_index = eval("0" + current_player.increase + str(roll))
                if destination_index >= 0 and destination_index <= NUM_SPIKES - 1:
                    try:
                        player = self.spike_list[destination_index].peek().player
                    except: 
                        player = None
                    if not (player != current_player and len(self.spike_list[destination_index]) >= 2): 
                        possible_moves.append((0, roll, destination_index))
            return possible_moves
            
        #check home
        if all((i<= 5 or i >= 17) for i in unique_spikes):
            for index in unique_spikes:
                for roll in unique_rolls:
                    destination_index = eval(str(index) + current_player.increase + str(roll))
                    #is in range
                    if destination_index < 0 and destination_index > NUM_SPIKES - 1:
                        possible_moves.append((index, roll, "H"))
        
        #normal move
        for index in unique_spikes:
            for roll in unique_rolls:
                destination_index = eval(str(index) + current_player.increase + str(roll))
                #is in range
                if destination_index >= 0 and destination_index <= NUM_SPIKES - 1:
                    try:
                        player = self.spike_list[destination_index].peek().player
                    except: 
                        player = None
                    if not (player != current_player and len(self.spike_list[destination_index]) >= 2): 
                        possible_moves.append((index, roll, destination_index))
        print(possible_moves)
        return possible_moves

    def end_statistics(self):
        """
        End_statistics - displays the statistics of the backgammon game; after pressing any key, it shows game menu

        Returns:
        None
        """
        self.clear_console()
        print("BACKGAMMON GAME")
        print("----------------------------------------")
        print("Statistics:")
        print("Player1:")
        print("Player2:")
        input("Press any key...")
        self.menu()
        