from models.queen import Queen
from models.position2d import Position2d


class RecursiveResolver:
    def __init__(self):
        self.solutions = []

    def resolve(self, rows, columns, currentColumn, pieces):

        for row in range(1, rows + 1):
            currentPiece = Queen(Position2d([currentColumn, row]))

            isInCollision = self.checkCollision(currentPiece, pieces)

            if not(isInCollision):
                pieces.append(currentPiece)

                if currentColumn < columns:
                    self.resolve(rows, columns, currentColumn + 1, pieces)
                else:
                    self.solutions.append(pieces.copy())

                pieces.pop()

            else:
                continue

    def checkCollision(self, currentPiece, pieces):
        for piece in pieces:
            if currentPiece.isInCollision(piece):
                return True

        return False