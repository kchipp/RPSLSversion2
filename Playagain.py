class Playagain:

    def __init__(self, playAgain):
        self.playAgain = playAgain
        
    def playAgain():
        choice = input("Do you want to play again? Yes or No ")
        if choice.lower() in ["no", "n"]:
            return False
        else:
            return True


    