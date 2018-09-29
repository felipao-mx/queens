from  src.strategies.implementations.DF.RecursiveResolver import RecursiveResolver



def test_1x1_board_solutions():
    rows = 1
    columns = 1
    initialColumn = 1

    resolver = RecursiveResolver()
    resolver.resolve(rows, columns, initialColumn, [])

    assert len(resolver.solutions) == 1
    del resolver

def test_2x2_board_solutions():
    rows = 2
    columns = 2
    initialColumn = 1

    resolver = RecursiveResolver()
    resolver.resolve(rows, columns, initialColumn, [])

    assert len(resolver.solutions) == 0
    del resolver


def test_3x3_board_solutions():
    rows = 3
    columns = 3
    initialColumn = 1

    resolver = RecursiveResolver()
    resolver.resolve(rows, columns, initialColumn, [])

    assert len(resolver.solutions) == 0
    del resolver

def test_4x4_board_solutions():
    rows = 4
    columns = 4
    initialColumn = 1

    resolver = RecursiveResolver()
    resolver.resolve(rows, columns, initialColumn, [])

    assert len(resolver.solutions) == 2
    del resolver


def test_5x5_board_solutions():
    rows = 5
    columns = 5
    initialColumn = 1

    resolver = RecursiveResolver()
    resolver.resolve(rows, columns, initialColumn, [])

    assert len(resolver.solutions) == 10


def test_6x6_board_solutions():
    rows = 6
    columns = 6
    initialColumn = 1

    resolver = RecursiveResolver()
    resolver.resolve(rows, columns, initialColumn, [])

    assert len(resolver.solutions) == 4

def test_7x7_board_solutions():
    rows = 7
    columns = 7
    initialColumn = 1

    resolver = RecursiveResolver()
    resolver.resolve(rows, columns, initialColumn, [])

    assert len(resolver.solutions) == 40

def test_8x8_board_solutions():
    rows = 8
    columns = 8
    initialColumn = 1

    resolver = RecursiveResolver()
    resolver.resolve(rows, columns, initialColumn, [])

    assert len(resolver.solutions) == 92


def test_9x9_board_solutions():
    rows = 9
    columns = 9
    initialColumn = 1

    resolver = RecursiveResolver()
    resolver.resolve(rows, columns, initialColumn, [])

    assert len(resolver.solutions) == 352

def test_10x10_board_solutions():
    rows = 10
    columns = 10
    initialColumn = 1

    resolver = RecursiveResolver()
    resolver.resolve(rows, columns, initialColumn, [])

    assert len(resolver.solutions) == 724

def test_11x11_board_solutions():
    rows = 11
    columns = 11
    initialColumn = 1

    resolver = RecursiveResolver()
    resolver.resolve(rows, columns, initialColumn, [])

    assert len(resolver.solutions) == 2680

def test_12x12_board_solutions():
    rows = 12
    columns = 12
    initialColumn = 1

    resolver = RecursiveResolver()
    resolver.resolve(rows, columns, initialColumn, [])

    assert len(resolver.solutions) == 14200

def test_13x13_board_solutions():
    rows = 13
    columns = 13
    initialColumn = 1

    resolver = RecursiveResolver()
    resolver.resolve(rows, columns, initialColumn, [])

    assert len(resolver.solutions) == 73712

def test_14x14_board_solutions():
    rows = 14
    columns = 14
    initialColumn = 1

    resolver = RecursiveResolver()
    resolver.resolve(rows, columns, initialColumn, [])

    assert len(resolver.solutions) == 365596

def test_15x15_board_solutions():
    rows = 14
    columns = 14
    initialColumn = 1

    resolver = RecursiveResolver()
    resolver.resolve(rows, columns, initialColumn, [])

    assert len(resolver.solutions) ==  2279184