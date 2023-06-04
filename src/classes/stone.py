class Stone():
    def __init__(self, player):
        self._player = player
        self._history = []
    
    
    def setHistory(self, history):
        self._history = history

    @property    
    def player(self):
        return self._player

    @property    
    def history(self):
        return self._history

    def addSpikeToHistory(self, spike):
        self._history.append(spike)

    def __str__(self):
        return f"{self._player.symbol}"