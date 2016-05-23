class Shots:

    def __init__(self):
        return
        
    def turnNumberToName(self, number):
        if number == 0:
            return "rock"
        elif number == 1:
            return "spock"
        elif number == 2:
            return "paper"
        elif number == 3:
            return "lizard"
        elif number == 4:
            return "scissors"
              
    def turnNameToNumber(self, name):
        if name == "rock":
            return 0
        elif name == "spock":
            return 1
        elif name == "paper":
            return 2
        elif name == "lizard":
            return 3
        elif name == "scissors":
            return 4
     

    def decideWinner(self, player1Choice, player2Choice):
        results = (5 + player1Choice - player2Choice) % 5
        if results == 1 or results == 3:
           print ("self.player2 Wins!")
        elif results == 2 or results == 4:
           print ("self.player1 Wins!")
        else:
           print ("You Tied")
    
 