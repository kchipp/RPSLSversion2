class Players:

    def __init__(self, player):
        self.player = player       
        self.playerChoice = None 
        
    def chooseShot():
        playerChoice = input("Player-Make your Choice: ")
        playerChoice = playerChoice.lower()
        aValidChoice = self.validChoice(playerChoice)
        if aValidChoice == True:
            self.playerChoice = playerChoice
        else:
            print ("Please enter a valid choice-Rock, Paper, Scissors, Lizard, or Spock")
            chooseShot()
   
    

    def validateChoice(playerChoice):
        if playerChoice == "Rock" or playerChoice == "Spock" or playerChoice == "Paper" or playerChoice == "Lizard" or playerChoice == "Scissors":
            return True
        else:
            return False 


        
    