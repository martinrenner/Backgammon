from abc import ABC,abstractmethod #abstract class
from src.classes.jail import Jail
from src.classes.home import Home

class Player(ABC):
    def __init__(self, increase, symbol, color):
        self._spikes = []
        self._possibleMoves = []
        self._oppositePlayer = None
        self._home = Home()
        self._jail = Jail()
        self._increase = increase
        self._symbol = symbol
        self._color = color

    @property
    def home(self):
        return self._home
    
    @property
    def jail(self):
        return self._jail
    
    @property
    def oppositePlayer(self):
        return self._oppositePlayer

    @property
    def color(self):
        return self._color.name
    
    @property
    def symbol(self):
        return self._symbol

    @oppositePlayer.setter
    def oppositePlayer(self, player):
        self._oppositePlayer = player

    @color.setter
    def color(self, color):
        self._color = color

    def addSpike(self, spike):
        self._spikes.append(spike)
    
    def popSpike(self, spike):
        self._spikes.remove(spike)

    @abstractmethod
    def moveToHome(self, stone):
        ...

    @abstractmethod
    def moveStone(self):
        ...
    