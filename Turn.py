from Shots import Shots
class Turn:

    def __init__(self, shot):
        self.shot = shot

    def takeTurn(self, player1, player2):    
        player1.chooseShot()
        player2.chooseShot()
        self.shot = Shots()
        shot.playRpsls(player1, player2) 

    