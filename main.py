import pygame,sys
from pygame.locals import *
from GameConfig import *
from broad import *
from Chesspiece import *


pygame.init()

screen = pygame.display.set_mode((SRC_WIDTH, SRC_HEIGHT))
mainbroad = ChessBroad(SRC_WIDTH)
Chesspiece.broad = mainbroad
    

white_player = []
for x,y in WHITE_PAWN_SPAWN:
    white_player.append(Pawn(x,y,"white"))
    mainbroad.box[x][y].placed = "white"
for i in range(0,8):
    mainbroad.box[i][7].placed = "white"
white_player.append(Rook(0,7,"white"))
white_player.append(Rook(7,7,"white"))
white_player.append(Knight(1,7,"white"))
white_player.append(Knight(6,7,"white"))
white_player.append(Bishop(5,7,"white"))
white_player.append(Bishop(2,7,"white"))
white_player.append(King(3,7,"white"))
white_player.append(Queen(4,7,"white"))

black_player = []
for x,y in BLACK_PAWN_SPAWN:
    black_player.append(Pawn(x,y,"black"))
    mainbroad.box[x][y].placed = "black"
for i in range(0,8):
    mainbroad.box[i][0].placed = "black"
black_player.append(Rook(0,0,"black"))
black_player.append(Rook(7,0,"black"))
black_player.append(Knight(1,0,"black"))
black_player.append(Knight(6,0,"black"))
black_player.append(Bishop(5,0,"black"))
black_player.append(Bishop(2,0,"black"))
black_player.append(King(4,0,"black"))
black_player.append(Queen(3,0,"black"))

chessChossing = False
end_game = False
player_turn = 0
player = [white_player,black_player]

font = pygame.font.Font('freesansbold.ttf', 16)
text1 = font.render("PLAYER 1",True,COLOR_LBLUE)
text2 = font.render("PLAYER 2",True,COLOR_LBLUE)


time = 60
fps = 60

while not end_game:
    pygame.time.Clock().tick(fps)
    mouse_x,mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            for player_piece in player[player_turn]:
                if player_piece.collidepoint(mouse_x,mouse_y - 100):
                    for player_piece1 in player[player_turn]:
                        player_piece1.chossing = False
                    for row in mainbroad.box:
                        for box in row:
                            box.hightlight = False
                            box.hint = False    
                    player_piece.chossing = True
                    chessChossing = True
                    player_piece.get_move_able_pos()
                    print(player_piece.move_able_pos)
                    print(type(player_piece))
                        
            if chessChossing:
                for player_piece in player[player_turn]:
                    if player_piece.chossing:
                        mainbroad.box[player_piece.pos_x][player_piece.pos_y].hightlight = True
                        if type(player_piece) == King:
                           pass
                        for x,y in player_piece.move_able_pos:
                            mainbroad.box[x][y].hint = True  
                            if mainbroad.box[x][y].rect.collidepoint(mouse_x, mouse_y-100):
                                mainbroad.box[player_piece.pos_x][player_piece.pos_y].placed = ""
                                player_piece.move_to(mainbroad.box[x][y].rect,x,y)
                                mainbroad.box[x][y].placed = player_piece.color
                                if type(player_piece) == Pawn and (player_piece.pos_y == 0 or player_piece.pos_y == 7):
                                    player[player_turn].append(Queen(player_piece.pos_x,player_piece.pos_y,player_piece.color))
                                    player[player_turn].remove(player_piece)
                                if player_turn == 1:
                                    player_turn = 0
                                else:
                                    player_turn = 1
                                for orther_player_piece in player[player_turn]:
                                    if orther_player_piece.pos_x == x and orther_player_piece.pos_y == y:
                                        if type(orther_player_piece) == King:
                                            end_game = True
                                        player[player_turn].remove(orther_player_piece)
                                player_piece.chossing = False
                                chessChossing = False
                                for row in mainbroad.box:
                                    for box in row:
                                        box.hightlight = False
                                        box.hint = False
                                time = 60
                                break
                        
    pygame.display.update()
    Chesspiece.broad = mainbroad
    screen.fill(COLOR_WHITE)
    mainbroad.display(screen,0,(SRC_HEIGHT-SRC_WIDTH)/2)
    for pl in player:
        for player_piece in pl:
            player_piece.display(mainbroad)
    if player_turn == 1:
        text3 = font.render("TIMELEFT:" + str(int(time)),True,COLOR_LBLUE)
        text4 = font.render("TIMELEFT: 60",True,COLOR_LBLUE)
    else:
        text4 = font.render("TIMELEFT:" + str(int(time)),True,COLOR_LBLUE)
        text3 = font.render("TIMELEFT: 60",True,COLOR_LBLUE)
        
    
    screen.blit(text1,(100,50))
    screen.blit(text2,(100,950))
    screen.blit(text3,(650,50))
    screen.blit(text4,(650,950))
    
    time -= 1/fps
    if time <= 0:
        time = 60
        if player_turn == 1:
            player_turn = 0
        else:
            player_turn = 1