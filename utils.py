def getKing(playerPieces):
    for piece in playerPieces:
        if type(piece).__name__ == "King":
            return piece

def toChessMove(pos):
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    x ,y = pos
    if 0 <= x < 8 and 0 <= y < 8:
        column = columns[x]
        row = str(y + 1)
        return column + row
    else:
        return "wrong value bitch"