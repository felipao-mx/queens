from models.queen import Queen
from models.position2d import Position2d


def test_column_collision():
    column = 5

    queen1 = Queen(Position2d([column, 3]))
    queen2 = Queen(Position2d([column, 5]))

    assert queen1.isInColumnCollisionWith(queen2)


def test_not_column_collision():
    queen1 = Queen(Position2d([3, 5]))
    queen2 = Queen(Position2d([9, 4]))

    assert not(queen1.isInColumnCollisionWith(queen2))


def test_row_collision():
    row = 3

    queen1 = Queen(Position2d([8, row]))
    queen2 = Queen(Position2d([3, row]))

    assert queen1.isInRowCollisionWith(queen2)


def test_not_row_collision():
    queen1 = Queen(Position2d([9, 5]))
    queen2 = Queen(Position2d([9, 3]))

    assert not(queen1.isInRowCollisionWith(queen2))


def test_diagonal_collision():
    queen1 = Queen(Position2d([2, 2]))
    queen2 = Queen(Position2d([4, 4]))

    assert queen1.isInDiagonalCollisionWith(queen2)


def test_not_diagonal_collision():
    queen1 = Queen(Position2d([2, 2]))
    queen2 = Queen(Position2d([5, 4]))

    assert not(queen1.isInDiagonalCollisionWith(queen2))
