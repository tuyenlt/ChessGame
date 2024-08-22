import pygame
from broad import *
import math

class Chesspiece():
    broad = ""
    def __init__(self,spawn_x,spawn_y,color = "white"):
        self.pos_x = spawn_x
        self.pos_y = spawn_y
        self.size = self.broad.box_size
        self.color = color
        self.enemy_color = "black"
        if self.color == "black":
            self.enemy_color = "white"
        self.image = pygame.image.load("lib/white_pawn.png")
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        self.rect = self.broad.box[self.pos_x][self.pos_y].rect
        self.chossing = False
        self.move_able_pos = []
    
    def collidepoint(self,point_x,point_y):
        if self.rect.collidepoint(point_x,point_y):
            return True
        else :
            return False
        
    def move_to(self,box,i,j):
        self.rect = box
        self.pos_x, self.pos_y = (i,j)

    
    def display(self,br ,pos_x = None,pos_y = None):
        if pos_x and pos_y != None:
            self.pos_x, self.pos_y = (pos_x, pos_y)
        br.broad_sur.blit(self.image, self.rect)
                
class Pawn(Chesspiece):
    def __init__(self,spawn_x = 0,spawn_y = 0,color = "white",):
        super().__init__(spawn_x,spawn_y,color)
        self.image = pygame.image.load("lib/" + self.color + "_pawn.png")
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        
    def get_move_able_pos(self):
        self.move_able_pos = []
        direction = 1
        spawn_y = 1
        if self.color == "white":
            direction = -1
            spawn_y = 6
            
        if self.broad.box[self.pos_x][self.pos_y+direction].placed == "":
            self.move_able_pos.append((self.pos_x,self.pos_y + direction)) 
            if self.pos_y == spawn_y:   
                if self.broad.box[self.pos_x][self.pos_y + 2*direction].placed == "":
                    self.move_able_pos.append((self.pos_x, self.pos_y + 2*direction)) 
        
               
        if self.pos_x > 0 and self.broad.box[self.pos_x-1][self.pos_y+direction].placed == self.enemy_color:
            self.move_able_pos.append((self.pos_x-1,self.pos_y+direction))
            print(self.enemy_color)
            
        if self.pos_x < 7 and self.broad.box[self.pos_x+1][self.pos_y+direction].placed == self.enemy_color:
            self.move_able_pos.append((self.pos_x+1,self.pos_y+direction))
        
        if self.pos_y == 0 or self.pos_y == 7:
            self.change_piece == True
        
            
class Rook(Chesspiece):
    def __init__(self,spawn_x = 0,spawn_y = 0,color = "white",):
        super().__init__(spawn_x,spawn_y,color)
        self.image = pygame.image.load("lib/" + self.color + "_rook.png")
        self.image = pygame.transform.scale(self.image,(self.size,self.size))

    def get_move_able_pos(self):
        self.move_able_pos = []
        if self.pos_x < 7: 
            for i in range(self.pos_x+1,8):
                print(self.broad.box[i][self.pos_y].placed)
                if self.broad.box[i][self.pos_y].placed == "":
                    self.move_able_pos.append((i,self.pos_y))
                elif self.broad.box[i][self.pos_y].placed == self.enemy_color:
                        self.move_able_pos.append((i,self.pos_y))
                        break
                else: 
                    break
        
        if self.pos_x > 0:
            for i in range(self.pos_x-1,-1,-1):
                if self.broad.box[i][self.pos_y].placed == "":
                    self.move_able_pos.append((i,self.pos_y))
                elif self.broad.box[i][self.pos_y].placed == self.enemy_color:
                        self.move_able_pos.append((i,self.pos_y))
                        break
                else: 
                    break
        if self.pos_y < 7:
            for i in range(self.pos_y+1,8):
                if self.broad.box[self.pos_x][i].placed == "":
                    self.move_able_pos.append((self.pos_x,i))
                elif self.broad.box[self.pos_x][i].placed == self.enemy_color:
                        self.move_able_pos.append((self.pos_x,i))
                        break
                else: 
                    break
        if self.pos_y > 0:
            for i in range(self.pos_y-1,-1,-1):
                if self.broad.box[self.pos_x][i].placed == "":
                    self.move_able_pos.append((self.pos_x,i))
                elif self.broad.box[self.pos_x][i].placed == self.enemy_color:
                        self.move_able_pos.append((self.pos_x,i))
                        break
                else: 
                    break


        
class Knight(Chesspiece):
    def __init__(self,spawn_x = 0,spawn_y = 0,color = "white",):
        super().__init__(spawn_x,spawn_y,color)
        self.image = pygame.image.load("lib/" + self.color + "_knight.png")
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
    
    def get_move_able_pos(self):
        self.move_able_pos = []
        move_dir = [(2,1),(1,2),(-1,-2),(-2,-1),(-1,2),(1,-2),(-2,1),(2,-1)]
        for x,y in move_dir:
            if self.pos_x + x < 0 or self.pos_x + x > 7 or self.pos_y + y < 0 or self.pos_y + y > 7:
                continue
            else :
                if self.broad.box[self.pos_x + x][self.pos_y+y].placed != self.color:
                    self.move_able_pos.append((self.pos_x+x,self.pos_y+y))
                

class Bishop(Chesspiece):
    def __init__(self,spawn_x = 0,spawn_y = 0,color = "white",):
        super().__init__(spawn_x,spawn_y,color)
        self.image = pygame.image.load("lib/" + self.color + "_bishop.png")
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        
    def get_move_able_pos(self):
        self.move_able_pos = []
        
        if self.pos_x < 7 and self.pos_y <7 :
            for i in range(1,min(7-self.pos_x,7-self.pos_y)+1):
                if self.broad.box[self.pos_x+i][self.pos_y + i].placed == "":
                    self.move_able_pos.append((self.pos_x+i,self.pos_y+i))
                
                elif self.broad.box[self.pos_x+i][self.pos_y + i].placed == self.enemy_color:
                    self.move_able_pos.append((self.pos_x+i,self.pos_y+i))
                    break
                
                else :
                    break
        
        if self.pos_x < 7 and self.pos_y > 0:
            for i in range(1,min(7-self.pos_x,self.pos_y)+1):
                if self.broad.box[self.pos_x+i][self.pos_y - i].placed == "":
                    self.move_able_pos.append((self.pos_x+i,self.pos_y-i))
                
                elif self.broad.box[self.pos_x+i][self.pos_y - i].placed == self.enemy_color:
                    self.move_able_pos.append((self.pos_x+i,self.pos_y-i))
                    break
                
                else :
                    break
        
        if self.pos_x > 0 and self.pos_y > 0:
            for i in range(1,min(self.pos_x,self.pos_y)+1,1):
                if self.broad.box[self.pos_x-i][self.pos_y - i].placed == "":
                    self.move_able_pos.append((self.pos_x-i,self.pos_y-i))
                elif self.broad.box[self.pos_x-i][self.pos_y - i].placed == self.enemy_color:
                    self.move_able_pos.append((self.pos_x-i,self.pos_y-i))
                    break
                else :
                    break
        
        if self.pos_x > 0 and self.pos_y <7 :
            for i in range(1,min(self.pos_x,7-self.pos_y)+1):
                if self.broad.box[self.pos_x-i][self.pos_y + i].placed == "":
                    self.move_able_pos.append((self.pos_x-i,self.pos_y+i))
                
                elif self.broad.box[self.pos_x-i][self.pos_y + i].placed == self.enemy_color:
                    self.move_able_pos.append((self.pos_x-i,self.pos_y+i))
                    break
                
                else :
                    break
                
class King(Chesspiece):
    def __init__(self,spawn_x = 0,spawn_y = 0,color = "white",):
        super().__init__(spawn_x,spawn_y,color)
        self.image = pygame.image.load("lib/" + self.color + "_king.png")
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
    
    def get_move_able_pos(self):
        self.move_able_pos = []
        move_dir = [(1,1),(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1)]
        for x,y in move_dir:
            if self.pos_x + x < 0 or self.pos_x + x > 7 or self.pos_y + y < 0 or self.pos_y + y > 7:
                continue
            else :
                if self.broad.box[self.pos_x + x][self.pos_y+y].placed != self.color:
                    self.move_able_pos.append((self.pos_x+x,self.pos_y+y))
        
        
class Queen(Bishop,Rook):
    def __init__(self,spawn_x = 0,spawn_y = 0,color = "white",):
        super().__init__(spawn_x,spawn_y,color)
        self.image = pygame.image.load("lib/" + self.color + "_queen.png")
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
    
    def get_move_able_pos(self):
        super().get_move_able_pos()
        if self.pos_x < 7: 
            for i in range(self.pos_x+1,8):
                print(self.broad.box[i][self.pos_y].placed)
                if self.broad.box[i][self.pos_y].placed == "":
                    self.move_able_pos.append((i,self.pos_y))
                elif self.broad.box[i][self.pos_y].placed == self.enemy_color:
                        self.move_able_pos.append((i,self.pos_y))
                        break
                else: 
                    break
        
        if self.pos_x > 0:
            for i in range(self.pos_x-1,-1,-1):
                if self.broad.box[i][self.pos_y].placed == "":
                    self.move_able_pos.append((i,self.pos_y))
                elif self.broad.box[i][self.pos_y].placed == self.enemy_color:
                        self.move_able_pos.append((i,self.pos_y))
                        break
                else: 
                    break
        if self.pos_y < 7:
            for i in range(self.pos_y+1,8):
                if self.broad.box[self.pos_x][i].placed == "":
                    self.move_able_pos.append((self.pos_x,i))
                elif self.broad.box[self.pos_x][i].placed == self.enemy_color:
                        self.move_able_pos.append((self.pos_x,i))
                        break
                else: 
                    break
        if self.pos_y > 0:
            for i in range(self.pos_y-1,-1,-1):
                if self.broad.box[self.pos_x][i].placed == "":
                    self.move_able_pos.append((self.pos_x,i))
                elif self.broad.box[self.pos_x][i].placed == self.enemy_color:
                        self.move_able_pos.append((self.pos_x,i))
                        break
                else: 
                    break
        
        