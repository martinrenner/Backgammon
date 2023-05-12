from src.classes.node import Node

class Home(Node):
    def __init__(self, sumOfAllStones = 15):
        """
        Constructor - initialize home

        Parameters:
        sumOfAllStones (Int): number of stones that determine end of game
        """
        super().__init__()
        self.sumOfAllStones = sumOfAllStones

    def allStonesHome(self):
        """
        AllStonesHome - check if all stones are home

        Returns: 
        Bool - False unless all stones are home, otherwise True
        """
        return False if len(self.stones) < self.sumOfAllStones else True  
    
#---------------------------------------------------------
#                       TEST DATA
#---------------------------------------------------------
if __name__ == "__main__":
    test_home = Home(3)
    assert test_home.isEmpty() == True, "Home should be empty"
    assert (len(test_home) == 0), "Home should be empty"
    test_home.push("TEST")
    assert test_home.isEmpty() == False, "Home should not be empty"
    assert (len(test_home) == 1), "Home should have 1 stone"
    test_home.push("TEST2")
    assert test_home.allStonesHome() == False, "Not all stones should be home"
    test_home.push("TEST3")
    assert test_home.allStonesHome() == True, "All stones should be home"
    assert (len(test_home) == 3), "Home should have 3 stones"
    assert (len(test_home) != 2), "Number of added stones should not be 2 stones"