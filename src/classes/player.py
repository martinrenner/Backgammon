from abc import ABC #abstract class

class Player(ABC):
    def __init__(self):
        self._color = None
        self._spikes = []
        self._possibleMoves = []
        self._opositPlayer = None
        self._home = None

    @property
    def home(self):
        return self._home

    @property
    def color(self):
        return self._color

    @home.setter
    def home(self, node):
        self._home = node

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
    