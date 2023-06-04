from src.classes.node import Node
from src.classes.home import Home
from src.classes.jail import Jail

#---------------------------------------------------------
#                       TEST DATA NODE
#---------------------------------------------------------
if __name__ == "__main__":
    test_node = Node()
    assert test_node.isEmpty() == True, "Node should be empty"
    assert (len(test_node) == 0), "Node should be empty"
    test_node.push("TEST")
    assert test_node.isEmpty() == False, "Node should not be empty"
    assert (len(test_node) == 1), "Node should have 1 stone"
    test_node.push("TEST2")
    test_node.push("TEST3")
    assert (len(test_node) == 3), "Node should have 3 stones"
    assert (len(test_node) != 2), "Number of added stones should not be 2 stones"


#---------------------------------------------------------
#                       TEST DATA HOME
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

#---------------------------------------------------------
#                       TEST DATA JAIL
#---------------------------------------------------------
if __name__ == "__main__":
    test_jail = Jail()
    assert test_jail.isEmpty() == True, "Jail should be empty"
    assert (len(test_jail) == 0), "Jail should be empty"
    test_jail.push("TEST")
    assert test_jail.isEmpty() == False, "Jail should not be empty"
    assert (len(test_jail) == 1), "Jail should have 1 stone"
    test_jail.pop()
    assert test_jail.isEmpty() == True, "Jail should be empty"
    assert (len(test_jail) == 0), "Jail should be empty"
    test_jail.push("TEST2")
    test_jail.push("TEST3")
    assert (len(test_jail) == 2), "Jail should have 3 stones"
    assert (len(test_jail) != 3), "Jail of added stones should not be 2 stones"