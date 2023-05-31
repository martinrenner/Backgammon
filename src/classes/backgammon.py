from src.classes.spike import Spike
from src.classes.AI import AI
from src.classes.human import Human
from src.classes.stone import Stone
from src.classes.colors import Colors
from src.classes.dice import Dice
from sys import exit
from os import system, name
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
            self.player_one = Human("PLAYER 1", "+", "X", Colors.red, -1, 24, [18,19,20,21,22,23,"H"])
            self.player_two = Human("PLAYER 2", "-", "Y", Colors.blue, 24, -1, [0,1,2,3,4,5,"H"])
        elif mode == 2:
            # Player vs AI
            self.player_one = Human("PLAYER 1", "+", "X", Colors.red, -1, 24, [18,19,20,21,22,23,"H"])
            self.player_two = AI("PLAYER 2", "-", "Y", Colors.blue, 24, -1, [0,1,2,3,4,5,"H"])
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
                self.game_layout(rolled, current_player)
                possible_moves = self.all_possible_moves(rolled, current_player)
                if not possible_moves:
                    current_player.last_round_moves += "[No possible move]"
                    break
                from_spike, roll_choice, to_spike = current_player.turn(possible_moves)
                print(current_player.last_round_moves)
                current_player.last_round_moves += f"[{from_spike}, {roll_choice}, {to_spike}], "
                rolled.remove(roll_choice)
                self.move(current_player, from_spike, to_spike)
                if self.player_one.home.allStonesHome() or self.player_two.home.allStonesHome():
                    break
            if self.player_one.home.allStonesHome() or self.player_two.home.allStonesHome():
                break
            current_player = current_player.oppositePlayer
            current_player.resetLastRoundMove()
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
        while True:
            try:
                choice = int(input("Choose menu option (1-3): "))
                if choice > 0 and choice < 4:
                    break
                else:
                    print(f"Invalid choice. Choose option (0-3).")
            except ValueError:
                print(f"Invalid choice. Choose option (0-3).")
        return choice

    def clear_console(self):
        """
        Clear_console - clears the console screen

        Returns:
        None
        """
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def create_stones(self):
        """
        Create_stones - creates stones for the game board by pushing them onto the spikes of the board
        
        Returns:
        None
        """
        for i in range(NUM_SPIKES):
            for _ in range(STONES_LAYOUT[i]):
                self.spike_list[i].push(Stone(self.player_one))
                self.spike_list[NUM_SPIKES - i - 1].push(Stone(self.player_two))

    def game_layout(self, rolled, current_player):
        """
        Game_layout - prints the current state of the backgammon board and the rolled dice.
        
        Parameters:
        rolled (list(int)): list of integers representing the values of the rolled dicies.
        
        Returns:
        None
        """
        self.clear_console()
        print("BACKGAMMON GAME")
        print("- " + colored(self.player_two.name, self.player_two.color) + " -----------------------------")
        print(self.player_two.home)
        print(self.player_two.jail)
        print("----------------------------------------")
        for spike in self.spike_list:
            print(spike)
        print("- " + colored(self.player_one.name, self.player_one.color) + " -----------------------------")
        print(self.player_one.jail)
        print(self.player_one.home)
        print("- TURN ---------------------------------")
        print(f"{colored(current_player.name, current_player.color)}")
        if self.player_one != current_player:
            print(f"Opponents history: {self.player_one.last_round_moves:}")
        else:
            print(f"Opponents history: {self.player_two.last_round_moves:}")
        print(f"ROLL: {rolled}")

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
        """
        All_possible_moves - calculates a list of all possible moves of stones for the current player
        
        Parameters:
        rolled: A list of integers representing the values rolled on the dice
        current_player: The player whose possible moves are being calculated.

        Returns:
        possible_moves(list(from, step, to)) - a list of possible moves a player can make based on the dice roll and their current position
        """
        unique_spikes = set(current_player.spikes)
        unique_rolls = set(rolled)
        possible_moves = []

        # Check jail
        if not current_player.jail.isEmpty():
            for roll in unique_rolls:
                destination_index = eval(str(current_player.min) + current_player.increase + str(roll))
                if destination_index >= 0 and destination_index <= NUM_SPIKES - 1:
                    try:
                        player = self.spike_list[destination_index].peek().player
                    except: 
                        player = None
                    if not (player != current_player and len(self.spike_list[destination_index]) >= 2): 
                        possible_moves.append(("J", roll, destination_index))
            return possible_moves

        # Check home
        if all((i in current_player.toHomeArea) for i in unique_spikes):
            for index in unique_spikes:
                if(index == "H"):
                    continue
                for roll in unique_rolls:
                    destination_index = eval(str(index) + current_player.increase + str(roll))
                    # is in range
                    if destination_index < 0 or destination_index > NUM_SPIKES - 1:
                        possible_moves.append((index, roll, "H"))

        # Normal move
        for index in unique_spikes:
            if(index == "H"):
                continue
            for roll in unique_rolls:
                destination_index = eval(str(index) + current_player.increase + str(roll))
                # is in range
                if destination_index >= 0 and destination_index <= NUM_SPIKES - 1:
                    try:
                        player = self.spike_list[destination_index].peek().player
                    except: 
                        player = None
                    if not (player != current_player and len(self.spike_list[destination_index]) >= 2): 
                        possible_moves.append((index, roll, destination_index))
        return possible_moves


    def move(self, current_player, from_spike, to_spike):
        """
        Move - moves a stone from one spike to another based on the current location

        Parameters:
        current_player (Player): The player whose stone is being moved.
        from_spike (int): The spike from which the stone is being moved.
        to_spike (int): The spike to which the stone is being moved.

        Returns:
        None
        """
        try:
            peek = self.spike_list[to_spike].peek()
            if(peek.player != current_player):
                stone = self.spike_list[to_spike].pop()
                current_player.oppositePlayer.jail.push(stone)
        except:
            pass

        if(from_spike == "J"):
            stone = current_player.jail.pop()
        else:
            stone = self.spike_list[from_spike].pop()

        if(to_spike == "H"):
            current_player.home.push(stone)
        else:
            self.spike_list[to_spike].push(stone)

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
        self.run()
        