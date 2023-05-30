from src.classes.spike import Spike
from src.classes.AI import AI
from src.classes.human import Human
from src.classes.stone import Stone
from src.classes.colors import Colors
from src.classes.dice import Dice
from sys import exit
from os import system
from termcolor import colored

NUMBER_OF_SPIKES = 24
STONES_LAYOUT = [2,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,3,0,5,0,0,0,0,0]

class Backgammon:
    def __init__(self):
        self.spikes = [Spike(i+1) for i in range(NUMBER_OF_SPIKES)]
        self.dice = Dice()

    def play(self):
        mode = self.menu()
        self.clear_console()
        if mode == 1:
            # PC vs PC
            self.player1 = Human("+", "X", Colors.red)
            self.player2 = Human("-", "Y", Colors.blue)
        elif mode == 2:
            # PC vs AI
            self.player1 = Human("+", "X", Colors.red)
            self.player2 = AI("-", "Y", Colors.blue)
        else:
            exit()

        self.player1.oppositePlayer = self.player2
        self.player2.oppositePlayer = self.player1

        self.create_stones()
        self.start_game()

    def start_game(self):
        activePlayer = self.player1
        while True:
            rolled = self.roll_double_dice()
            while rolled:
                self.game_layout(rolled)
                possible_moves = self.all_possible_moves(rolled)
                if possible_moves == []:
                    break

                rolled = activePlayer.turn(possible_moves, rolled)

                if self.player1.home.allStonesHome() or self.player2.home.allStonesHome():
                    break

            if self.player1.home.allStonesHome() or self.player2.home.allStonesHome():
                break
            activePlayer = activePlayer.oppositePlayer
        self.end_statistics()

    def menu(self):
        self.clear_console()
        print("BACKGAMMON GAME")
        print("----------------------------------------")
        print("Created by: Martin Renner")
        print("----------------------------------------")
        print("1 - PC vs PC")
        print("2 - PC vs AI")
        print("3 - Exit")
        choice = input("Choose menu option (1-3): ")
        while choice not in ['1', '2', '3']:
            choice = input("Invalid choice.  Choose menu option (1-3): ")
        return int(choice)

    def clear_console(self):
        system('cls')

    def create_stones(self):
        length = len(STONES_LAYOUT) 
        for spike in range(length):
            for _ in range(STONES_LAYOUT[spike]):
                self.spikes[spike].push(Stone(spike, self.player1))
                self.spikes[length - spike - 1].push(Stone(length - spike - 1, self.player2))

    def game_layout(self, rolled):
        self.clear_console()
        print("BACKGAMMON GAME")
        print("- " + colored("PLAYER 2", self.player2.color) + " -----------------------------")
        print(self.player2.home)
        print(self.player2.jail)
        print("-------------------------")
        for spike in self.spikes:
            print(spike)
        print("- " + colored("PLAYER 1", self.player1.color) + " -----------------------------")
        print(self.player1.jail)
        print(self.player1.home)
        print("----------------------------------------")
        print(f"ROLL: {rolled}")
        print("----------------------------------------")

    def debug(self):
        print("---------DEBUG--------------------------")
        print(self.player1._spikes)
        print(self.player2._spikes)

    def roll_double_dice(self):
        rolls = [self.dice.roll(), self.dice.roll()]
        if rolls[0] == rolls[1]:
            rolls *= 2
        return rolls
    
    def all_possible_moves(self, rolled):
        #prvni moznost: dostat se z jailu na hraci plochu (if hrac.jail neni prazdny)
        #druha moznost: z plochy na plochu
        #treti moznost: z posledniho sestive spiku domu (if set indexu kamenu <= 6 || >= 18)


        return []

    def end_statistics(self):
        self.clear_console()
        print("BACKGAMMON GAME")
        print("----------------------------------------")
        print("Statistics .....")
        print("Player1 .....")
        print("Player2 .....")
        input("Press any key...")
        self.menu()
        