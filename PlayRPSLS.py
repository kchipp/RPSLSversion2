def playRpsls(self, player1, player2):
        player1Choice = turnNameToNumber(player1.playerChoice)
        player2Choice = turnNameToNumber(player2.playerChoice)              
        self.decideWinner(player1Choice, player2Choice)