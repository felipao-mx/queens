from piece import Piece


class Queen(Piece):
    def isInCollision(self, piece):
        return self.isInColumnCollisionWith(piece) or self.isInRowCollisionWith(piece) or self.isInDiagonalCollisionWith(piece)

    def isInDiagonalCollisionWith(self, piece):
        rowDistance = abs(self.position.row - piece.position.row)
        colDistance = abs(self.position.column - piece.position.column)

        return rowDistance == colDistance

    def isInRowCollisionWith(self, piece):
        return self.position.row == piece.position.row

    def isInColumnCollisionWith(self, piece):
        return self.position.column == piece.position.column