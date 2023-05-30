class Stone():
    def __init__(self, currentSpike, player):
        self._position = currentSpike
        self._player = player
        self._player.addSpike(currentSpike)
        self._history = []
        self._history.append(self._position)
    
    @property    
    def player(self):
        return self._player

    @property    
    def getPosition(self):
        return self._position
    
    @getPosition.setter
    def setPosition(self, spike) -> None:
        self._history.append(self._position)
        self._position = spike

    def addSpikeToHistory(self, spike):
        self._history.append(spike)

    def __str__(self):
        return f"{self._player.symbol}"