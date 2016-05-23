from Players import Players
from Turn import Turn
class Game:

    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.shots = None
        
    def getPlayers(self):
        name = self.getName()        
        self.player1 = Players(name)
        name = self.getName()
        self.player2 = Players(name)
    
    def getName(self, input):
        input = input("Enter Name ")
        return input
   

        
    