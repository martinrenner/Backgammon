from abc import ABC,abstractmethod #abstract class
from src.classes.jail import Jail
from src.classes.home import Home

class Player(ABC):
    def __init__(self, increase, symbol, color):
        self._spikes = []
        self._opposite_player = None
        self._home = Home()
        self._jail = Jail()
        self._increase = increase
        self._symbol = symbol
        self._color = color

    @property
    def spikes(self):
        return self._spikes

    @property
    def home(self):
        return self._home
    
    @property
    def jail(self):
        return self._jail
    
    @property
    def opposite_player(self):
        return self._opposite_player

    @property
    def color(self):
        return self._color.name
    
    @property
    def symbol(self):
        return self._symbol
    
    @property
    def increase(self):
        return self._increase

    @opposite_player.setter
    def opposite_player(self, player):
        self._opposite_player = player

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
    