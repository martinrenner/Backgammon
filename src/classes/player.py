from abc import ABC, abstractmethod  # abstract class
from src.classes.jail import Jail
from src.classes.home import Home


class Player(ABC):
    """
    Player class
    """

    def __init__(self, name, increase, symbol, color, to_home_area):
        self._spikes = []
        self._last_round_moves = ""
        self._name = name
        self._opposite_player = None
        self._home = Home()
        self._jail = Jail()
        self._increase = increase
        self._symbol = symbol
        self._color = color
        self._min = -1 if increase == "+" else 24
        self._max = 24 if increase == "+" else -1
        self._to_home_area = to_home_area

    @property
    def name(self):
        return self._name

    @property
    def last_round_moves(self):
        return self._last_round_moves

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

    @property
    def min(self):
        return self._min

    @property
    def max(self):
        return self._max

    @property
    def to_home_area(self):
        return self._to_home_area

    @opposite_player.setter
    def opposite_player(self, player):
        self._opposite_player = player

    @color.setter
    def color(self, color):
        self._color = color

    @last_round_moves.setter
    def last_round_moves(self, move):
        self._last_round_moves = move

    def addSpike(self, spike):
        self._spikes.append(spike)

    def popSpike(self, spike):
        self._spikes.remove(spike)

    def resetLastRoundMove(self):
        self._last_round_moves = ""

    def checkWinType(self):
        if self.opposite_player.home.stonesHome() == 0 and any(i in self.opposite_player.spikes for i in self.to_home_area) or not self.opposite_player.jail.isEmpty():
                return "WON (Backgammon)"
        elif self.opposite_player.home.stonesHome() == 0:
            return "WON (Gammon)"
        elif self.opposite_player.home.stonesHome() >= 1 and self.opposite_player.home.stonesHome() < 15:
            return "WON (Game)"
        else:
            return "LOST"

    @abstractmethod
    def turn(self, possible_moves):
        ...
        