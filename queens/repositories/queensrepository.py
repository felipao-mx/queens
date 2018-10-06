from .tableinit import QueensPositionRegister
from utilities.columnutilities import numToString
class QueensPositionRepository:

    def __init__(self, session):
        self.session = session

    def add(self, queensSolutions, benchmarkId):
        i = 1
        for solution in queensSolutions:

            for queen in solution:
                queenRegister = QueensPositionRegister(
                    benchmarkId=benchmarkId, solution=i, row=queen.position.row, column=queen.position.column, columnChar=numToString(queen.position.column))
                self.session.add(queenRegister)
            
            i += 1

        self.session.commit()
