from GameConfig import WHITE_PAWN_SPAWN
from Pieces import *

class Player:
    def __init__(self,broad,color="white",countDown = 2400):
        self.broad = broad
        Chesspiece.broad = broad
        self.pieces = []
        self.color = color
        self.countDown = countDown
        self.isChecking = False
        if color == "white" :
            self.whiteInit()
        if color == "black" :
            self.blackInit()
            
    def whiteInit(self):
        for x,y in WHITE_PAWN_SPAWN:
            self.pieces.append(Pawn(x,y,"white"))
        self.pieces.append(Rook(0,7,"white"))
        self.pieces.append(Rook(7,7,"white"))
        self.pieces.append(Knight(1,7,"white"))
        self.pieces.append(Knight(6,7,"white"))
        self.pieces.append(Bishop(5,7,"white"))
        self.pieces.append(Bishop(2,7,"white"))
        self.pieces.append(Queen(3,7,"white"))
        
        self.king = King(4,7,"white")
        self.pieces.append(self.king)

    def blackInit(self):
        for x,y in BLACK_PAWN_SPAWN:
            self.pieces.append(Pawn(x,y,"black"))
        self.pieces.append(Rook(0,0,"black"))
        self.pieces.append(Rook(7,0,"black"))
        self.pieces.append(Knight(1,0,"black"))
        self.pieces.append(Knight(6,0,"black"))
        self.pieces.append(Bishop(5,0,"black"))
        self.pieces.append(Bishop(2,0,"black"))
        self.pieces.append(Queen(3,0,"black"))

        self.king = King(4,0,"black")
        self.pieces.append(self.king)
    
    def changePawn(self, pawn):
        self.pieces.append(Queen(pawn.x,pawn.y,self.color))
        self.pieces.remove(pawn)
    
    def getAllMove(self):
        moves = []
        for piece in self.pieces:
            piece.getMoveAblePos()
            for move in piece.moveAblePos:
                moves.append(move)
        return moves
    
    def setIsChecking(self, nextPlayer):
        for piece in nextPlayer.pieces:
            if piece.disable : 
                continue
            piece.getMoveAblePos()
            if (self.king.x , self.king.y) in piece.moveAblePos:
                return True
        return False
    
    def getMoveWhileIsChecking(self,nextPlayer):
        for piece in self.pieces:
            piece.getMoveAblePos()
            pre_x = piece.x
            pre_y = piece.y
            newMoveAblePos = []
            currBoxState = None
            prevBoxState = None
            for (x,y) in piece.moveAblePos:
                currBoxState = self.broad.box[x][y].placed
                if self.broad.box[x][y].placed != None:
                    self.broad.box[x][y].placed.disable = True
                piece.moveTo(self.broad.box[x][y],prevBoxState)        
                if self.setIsChecking(nextPlayer) == False:
                    newMoveAblePos.append((x,y))        
                    
                if (x,y) == piece.moveAblePos[-1]:
                    piece.moveTo(self.broad.box[pre_x][pre_y])
                self.broad.box[x][y].placed = currBoxState
                prevBoxState = currBoxState
                if self.broad.box[x][y].placed != None:
                    self.broad.box[x][y].placed.disable = False
            piece.moveAblePos = newMoveAblePos