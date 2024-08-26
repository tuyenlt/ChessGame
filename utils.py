def getKing(playerPieces):
    for piece in playerPieces:
        if type(piece).__name__ == "King":
            return piece