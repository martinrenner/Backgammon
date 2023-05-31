class Stone():
    def __init__(self, player):
        self._player = player
        self._history = []
    
    @property    
    def player(self):
        return self._player

    def addSpikeToHistory(self, spike):
        self._history.append(spike)

    def __str__(self):
        return f"{self._player.symbol}"