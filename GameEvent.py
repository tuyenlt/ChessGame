from Pieces import Pawn
from broad import ChessBroad
from utils import getKing

class GameState():
    gameBroad = ChessBroad() # type: ignore
    def __init__(self):
        self.isChossing = False
        self.isChecking = False
        self.isCheckMate = False
        self.currentPlayer = "white"
        self.nextPlayer = "black"
        self.countDown = 1200
        self.chossingPiece = None
        self.boxClicked = None
        self.winner = None
    
    def swapTurn(self):
        self.isChossing = False
        self.isCheckMate = False
        if self.currentPlayer == "white":
            self.currentPlayer = "black"
            self.nextPlayer = "white"
        else :
            self.currentPlayer = "white"
            self.nextPlayer = "black"
        self.chossingPiece = None
        self.boxClicked = None
            
    def setChossingState(self, chossingPiece, checking = False):
        self.isChossing = True
        self.chossingPiece = chossingPiece
        if chossingPiece.disable :
            return
        if not checking : 
            chossingPiece.getMoveAblePos()
    
    def handleOnplaced(self, currentPlayer, nextPlayer):
        nextPlayer.isChecking = False
        for piece in currentPlayer.pieces:
            piece.getMoveAblePos()
            if (nextPlayer.king.x , nextPlayer.king.y) in piece.moveAblePos:
                nextPlayer.isChecking = True
        nextPlayer.getMoveWhileIsChecking(currentPlayer)
        if nextPlayer.onCheckMate:
            self.winner = currentPlayer.color    
        self.swapTurn()    
        
    
        
        