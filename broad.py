import pygame
from pygame.locals import *
from GameConfig import *
from Chesspiece import Chesspiece


class Box:
    def __init__(self,box_size=100,pos_x=0,pos_y=0,color=COLOR_WHITE,placed = False):  
        self.rect = pygame.Rect(0,0,box_size,box_size)
        self.rect.center = (pos_x,pos_y)
        self.placed = ""
        self.color = color
        self.clicked = False
        self.chesspos = (0,0)
        self.hightlight = False
        self.hint = False
        
    

class ChessBroad:
    def __init__(self,broad_size = 800):
        self.broad_size = broad_size
        self.broad_sur = pygame.surface.Surface((broad_size,broad_size))
        self.box = []
        self.box_size = int(self.broad_size/8)
        for i in range(int(self.box_size/2), self.broad_size, self.box_size):
            row = []
            for j in range(int(self.box_size/2), self.broad_size, self.box_size):
                color_set = int((j+i)/(2*(self.box_size/2)))
                if color_set % 2 == 0:
                    box_color = COLOR_BROWN
                else:
                    box_color = COLOR_WHITE
                new_box = Box(self.box_size,i,j,box_color,False)
                new_box.chesspos = (i,j)
                row.append(new_box)
            self.box.append(row)
        
    def display(self,surface = pygame.Surface,pos_x=0,pos_y=0):
        surface.blit(self.broad_sur,(pos_x,pos_y))
        for i in range(0,8):
            for j in range(0,8):
                pygame.draw.rect(self.broad_sur,self.box[i][j].color, self.box[i][j].rect)
                if self.box[i][j].hightlight:
                    pygame.draw.rect(self.broad_sur,COLOR_LRED, self.box[i][j].rect,3)    
                if self.box[i][j].hint:
                    pygame.draw.circle(self.broad_sur,COLOR_LRED,self.box[i][j].rect.center,self.box_size/10)
        pygame.draw.line(self.broad_sur,COLOR_BLACK,(0,0),(self.broad_size,0),2)
        pygame.draw.line(self.broad_sur,COLOR_BLACK,(0,0),(0,self.broad_size-2),2)
        pygame.draw.line(self.broad_sur,COLOR_BLACK,(0,self.broad_size-2),(self.broad_size,self.broad_size-2),2)
        pygame.draw.line(self.broad_sur,COLOR_BLACK,(self.broad_size-2,0),(self.broad_size-2,self.broad_size-2),2)