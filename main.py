import pygame,sys
from pygame.locals import *
from GameConfig import *
from GameEvent import GameState
from Player import Player
from broad import ChessBroad


pygame.init()

def runGame(mainbroad, white_player, black_player):
    screen = pygame.display.set_mode((SRC_WIDTH, SRC_HEIGHT))
    player = {
        "white" : white_player,
        "black": black_player
    }

    font = pygame.font.Font('freesansbold.ttf', 16)
    text1 = font.render("PLAYER 1",True,COLOR_LBLUE)
    text2 = font.render("PLAYER 2",True,COLOR_LBLUE)


    time = 60
    fps = 60

    gameState = GameState()

    while gameState.winner == None:
        pygame.time.Clock().tick(fps)
        mouse_x,mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                for piece in player[gameState.currentPlayer].pieces:
                    if piece.onClick(mouse_x,mouse_y - 100): # handle when chossing a piece
                        if piece != gameState.chossingPiece: # reset hint on broad when chossing other piece
                            mainbroad.resetState()
                            
                        if piece == player[gameState.currentPlayer].king:
                            piece.unableMoves = player[gameState.nextPlayer].getAllMove()
                            print(piece.unableMoves)
                            
                        if player[gameState.currentPlayer].isChecking:
                            #handle checking 
                            print("is checking")
                            player[gameState.currentPlayer].getMoveWhileIsChecking(player[gameState.nextPlayer])
                            gameState.setChossingState(chossingPiece= piece,checking = True)
                        else : 
                            gameState.setChossingState(chossingPiece= piece,checking = False)    
                        mainbroad.setState(gameState)
                        
                        
                        for boxRow in mainbroad.box: # print chess table 
                            for box in boxRow:
                                if box.placed == None:
                                    print("  *  ", end=" ")
                                elif box.placed == gameState.chossingPiece:
                                    print("choss",end=" ")
                                else : print(box.placed.color, end=" ")
                            print()
                        print("===============================================================")
                gameState.boxClicked = mainbroad.getBoxClicked(mouse_x,mouse_y - 100)
                # ===============================================================  handle move            
                if (
                        gameState.boxClicked != None
                    and gameState.chossingPiece != None
                    and gameState.boxClicked.placed != gameState.chossingPiece 
                    and gameState.boxClicked.chesspos in gameState.chossingPiece.moveAblePos
                    ):
                    # ========================================================= handle king  move
                    if gameState.chossingPiece == player[gameState.currentPlayer].king:
                        
                        if gameState.boxClicked.chesspos == player[gameState.currentPlayer].king.longCastlePos: # if short castle
                            mainbroad.box[0][gameState.chossingPiece.y].placed.moveTo(mainbroad.box[2][gameState.chossingPiece.y])
                            
                        if gameState.boxClicked.chesspos == player[gameState.currentPlayer].king.shortCastlePos: # if long castle
                            mainbroad.box[7][gameState.chossingPiece.y].placed.moveTo(mainbroad.box[5][gameState.chossingPiece.y])
                            
                    mainbroad.onPlacing(gameState, player[gameState.nextPlayer].pieces)
                    gameState.chossingPiece.moveTo(gameState.boxClicked)
                    
                    if type(gameState.chossingPiece).__name__ == "Pawn" and gameState.chossingPiece.changeAble() : # handle whatever "Phong Hậu" call in english
                        player[gameState.currentPlayer].changePawn(gameState.chossingPiece)
                    
                    gameState.handleOnplaced(player[gameState.currentPlayer], player[gameState.nextPlayer])
                    mainbroad.resetState()    
                    
                        
                    
        pygame.display.update()
        screen.fill(COLOR_WHITE)
        
        if gameState.isChossing:
            pass
        
        
        mainbroad.display(screen,0,(SRC_HEIGHT-SRC_WIDTH)/2)
        for piece in player["white"].pieces:
            piece.display()
        for piece in player["black"].pieces:
            piece.display()
        text3 = font.render(f"TIMELEFT:{int(player["black"].countDown)}",True,COLOR_LBLUE)
        text4 = font.render(f"TIMELEFT: {int(player["white"].countDown)}",True,COLOR_LBLUE)
            
        screen.blit(text1,(100,50))
        screen.blit(text2,(100,950))
        screen.blit(text3,(650,50))
        screen.blit(text4,(650,950))
        
        player[gameState.currentPlayer].countDown -= 1/fps
        if player[gameState.currentPlayer].onCheckMate:
            gameState.winner = gameState.nextPlayer
        
        time -= 1/fps
        if time <= 0:
            time = 60
            gameState.swapTurn()



mainbroad = ChessBroad(SRC_WIDTH)
white_player = Player(mainbroad,"white")
black_player = Player(mainbroad,"black")

runGame(mainbroad, white_player, black_player)