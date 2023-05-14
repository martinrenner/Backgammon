from colors import Colors

class Stone():
    def __init__(self, currentSpike, color: Colors):
        self._position = currentSpike
        self._color = color
        
        self._history = []
        self._history.append(self._position)
    
    @property    
    def getPosition(self):
        return self._position
    
    @getPosition.setter
    def setPosition(self, spike) -> None:
        self._history.append(self._position)
        self._position = spike

    def addSpikeToHistory(self, spike):
        self._history.append(spike)