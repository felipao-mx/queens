import pytest
from  strategies.implementations.recursiveresolver import RecursiveResolver


@pytest.mark.parametrize("rows,columns,expected",
    [
        (1, 1, 1),
        (2, 2, 0),
        (3, 3, 0),
        (4, 4, 2),
        (5, 5, 10),
        (6, 6, 4),
        (7, 7, 40),
        (8, 8, 92),
        (9, 9, 352),
        (10, 10, 724),
        (11, 11, 2680),
        (12, 12, 14200),
        # (13, 13, 73712),
        # (14, 14, 365596),
        # (15, 15, 2279184),
    ]
)

def test_board_solutions(rows, columns, expected):
    initialColumn = 1

    resolver = RecursiveResolver()
    resolver.resolve(rows, columns, initialColumn, [])

    assert len(resolver.solutions) == expected