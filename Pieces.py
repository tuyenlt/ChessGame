import pygame
from broad import *
import math

from utils import toChessMove

class Chesspiece():
    broad = None
    def __init__(self,spawnX,spawnY,color = "white"):
        self.x = spawnX
        self.y = spawnY
        self.size = self.broad.box_size
        self.color = color
        self.image = pygame.image.load("lib/white_pawn.png")
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        self.rect = self.broad.box[self.x][self.y].rect
        self.moveAblePos = []
        self.broad.box[spawnX][spawnY].placed = self
        self.moved = False
        self.box = self.broad.box[spawnX][spawnY]
        self.disable = False
        
    
    def onClick(self,mouseX,mouseY):
        if self.rect.collidepoint(mouseX,mouseY):
            return True
        else :
            return False
        
    def moveTo(self,box,pre = None,log = True):
        self.rect = box.rect
        self.broad.box[self.x][self.y].placed = pre
        if log :
            print(f"{self.color} : {type(self).__name__} {toChessMove((self.x,self.y))} to ",end="")
        self.x , self.y = box.chesspos
        if log :
            print(f"{type(self).__name__} {toChessMove(box.chesspos)}")
        self.broad.box[self.x][self.y].placed = self
        self.moved = True
    
    def setBroad(self,broad):
        self.broad = broad
    
    def display(self,x = None,y = None):
        if x and y != None:
            self.x, self.y = (x, y)
        self.broad.broad_sur.blit(self.image, self.rect)
                
class Pawn(Chesspiece):
    def __init__(self,spawn_x = 0,spawn_y = 0,color = "white",):
        super().__init__(spawn_x,spawn_y,color)
        self.image = pygame.image.load("lib/" + self.color + "_pawn.png")
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        
    def getMoveAblePos(self):
        self.moveAblePos = []
        direction = 1
        spawn_y = 1
        if self.color == "white":
            direction = -1
            spawn_y = 6
            
        if self.broad.box[self.x][self.y+direction].placed == None:
            self.moveAblePos.append((self.x,self.y + direction)) 
            if self.y == spawn_y:   
                if self.broad.box[self.x][self.y + 2*direction].placed == None:
                    self.moveAblePos.append((self.x, self.y + 2*direction)) 
        try:
            if self.x > 0 and self.broad.box[self.x-1][self.y+direction].placed.color != self.color:
                self.moveAblePos.append((self.x-1,self.y+direction))
        except:
            pass   
        try:    
            if self.x < 7 and self.broad.box[self.x+1][self.y+direction].placed.color != self.color:
                self.moveAblePos.append((self.x+1,self.y+direction))
        except:
            pass
    def changeAble(self):
        if self.y == 0 or self.y == 7:
            return True
        return False
            
class Rook(Chesspiece):
    def __init__(self,spawn_x = 0,spawn_y = 0,color = "white",):
        super().__init__(spawn_x,spawn_y,color)
        self.image = pygame.image.load("lib/" + self.color + "_rook.png")
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        self.moveDir = [0,1], [0,-1], [1,0] , [-1,0]

    def getMoveAblePos(self):
        self.moveAblePos = []
        self.calcRookMoves(-1,self.x,self.y)
       
    def calcRookMoves(self,dir,x,y):
        if x > 7 or y > 7 or x < 0 or y < 0:
            return
        if dir == -1:
            for i in range(0,4):
                self.calcRookMoves(i,x+self.moveDir[i][0],y+self.moveDir[i][1])
        else : 
            if self.broad.box[x][y].placed == None :
                self.moveAblePos.append((x,y))
            elif self.broad.box[x][y].placed.color != self.color:
                self.moveAblePos.append((x,y))
                return
            else :
                return
            self.calcRookMoves(dir,x+self.moveDir[dir][0],y+self.moveDir[dir][1])

class Knight(Chesspiece):
    def __init__(self,spawn_x = 0,spawn_y = 0,color = "white",):
        super().__init__(spawn_x,spawn_y,color)
        self.image = pygame.image.load("lib/" + self.color + "_knight.png")
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
    
    def getMoveAblePos(self):
        self.moveAblePos = []
        move_dir = [(2,1),(1,2),(-1,-2),(-2,-1),(-1,2),(1,-2),(-2,1),(2,-1)]
        for x,y in move_dir:
            if self.x + x < 0 or self.x + x > 7 or self.y + y < 0 or self.y + y > 7:
                continue
            else :
                if (
                    self.broad.box[self.x + x][self.y+y].placed == None 
                    or self.broad.box[self.x + x][self.y+y].placed.color != self.color
                ):
                    self.moveAblePos.append((self.x+x,self.y+y))
                

class Bishop(Chesspiece):
    def __init__(self,spawn_x = 0,spawn_y = 0,color = "white",):
        super().__init__(spawn_x,spawn_y,color)
        self.image = pygame.image.load("lib/" + self.color + "_bishop.png")
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        self.moveDir = [1,1],[1,-1], [-1,1], [-1,-1]
        self.dir = 0
        
    def getMoveAblePos(self):
        self.moveAblePos = []
        self.calcBishopMoves(-1,self.x,self.y)
        
    def calcBishopMoves(self,dir,x,y):
        if x > 7 or y > 7 or x < 0 or y < 0:
            return
        if dir == -1:
            for i in range(0,4):
                self.calcBishopMoves(i,x+self.moveDir[i][0],y+self.moveDir[i][1])
        else : 
            if self.broad.box[x][y].placed == None :
                self.moveAblePos.append((x,y))
            elif self.broad.box[x][y].placed.color != self.color:
                self.moveAblePos.append((x,y))
                return
            else :
                return
            self.calcBishopMoves(dir,x+self.moveDir[dir][0],y+self.moveDir[dir][1])
                                
class King(Chesspiece):
    def __init__(self,spawn_x = 0,spawn_y = 0,color = "white",):
        super().__init__(spawn_x,spawn_y,color)
        self.image = pygame.image.load("lib/" + self.color + "_king.png")
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        self.shortCastlePos = None
        self.longCastlePos = None
        self.unableMoves = []

    
    def getMoveAblePos(self):
        self.moveAblePos = []
        move_dir = [(1,1),(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1)]
        for x,y in move_dir:
            if self.x + x < 0 or self.x + x > 7 or self.y + y < 0 or self.y + y > 7:
                continue
            else :
                if (
                        self.broad.box[self.x + x][self.y+y].placed == None 
                        or self.broad.box[self.x + x][self.y+y].placed.color != self.color 
                    ) and (self.x + x, self.y+y) not in self.unableMoves:
                    self.moveAblePos.append((self.x+x,self.y+y))                
        self.checkCastleAble()
    
    def checkCastleAble(self):
        if self.moved: 
            return 
        
        # long castle
        self.longCastlePos = (1,self.y)
        if( 
            self.broad.box[0][self.y].placed == None
            or self.broad.box[0][self.y].placed.moved == True
            or self.broad.box[1][self.y].placed != None
            or self.broad.box[2][self.y].placed != None
            or self.broad.box[3][self.y].placed != None
        ): self.longCastlePos = None
        # short castle
        self.shortCastlePos = (6,self.y)
        if( 
            self.broad.box[7][self.y].placed == None
            or self.broad.box[7][self.y].placed.moved == True
            or self.broad.box[6][self.y].placed != None
            or self.broad.box[5][self.y].placed != None
        ): self.shortCastlePos = None
        
        if self.shortCastlePos != None:
            self.moveAblePos.append(self.shortCastlePos)
            
        if self.longCastlePos != None:
            self.moveAblePos.append(self.longCastlePos)
            
class Queen(Rook,Bishop):
    def __init__(self,spawn_x = 0,spawn_y = 0,color = "white",):
        super().__init__(spawn_x,spawn_y,color)
        self.image = pygame.image.load("lib/" + self.color + "_queen.png")
        self.image = pygame.transform.scale(self.image,(self.size,self.size))

    def getMoveAblePos(self):
        self.moveDir = [0,1], [0,-1], [1,0] , [-1,0] # rook moves
        super().getMoveAblePos()
        self.moveDir = [1,1],[1,-1], [-1,1], [-1,-1] # bishop moves
        super().calcBishopMoves(-1,self.x,self.y)
        
        