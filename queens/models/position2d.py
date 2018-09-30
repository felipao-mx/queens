from .position import Position


class Position2d(Position):

    row = 0
    column = 0

    def __init__(self, vector):
        if vector is None:
            vector = [0, 0]
        
        super().__init__(vector)
        self.setVector(vector)


    def setRow(self, row):
        self.row = row
        self.vector[1] = row

    def setColumn(self, column):
        self.column = column
        self.vector[0] = column

    def setPosition(self, row, column):
        self.setRow(row)
        self.setColumn(column)

    def setVector(self, vector):
        if len(vector) != 2:
            raise IndexError

        self.setPosition(vector[0], vector[1])
