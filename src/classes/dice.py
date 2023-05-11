from random import choice

class Dice():
    def __init__(self, sides=6):
        self.__sides = [i for i in range(1,sides+1)]

    def roll(self) -> int:
        return choice(self.__sides)