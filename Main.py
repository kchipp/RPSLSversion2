from GameExplanation import GameExplanation
from Game import Game
from Players import Players
from Turn import Turn
from Shots import Shots
from Playagain import Playagain
from PlayRPSLS import PlayRPSLS

def Main():
    game = Game()
    game.startGame()
    game.getPlayers()
    game.getName()
    
    shot = Shots()
    shot.turnNumberToName()
    shot.turnNameToNumber()
    shot.playRPSLS(player1, player2)
    shot.decideWinner(2, 0)
    


if __name__ == "__main__":
    main()