from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime, Interval, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

dbString = "postgresql+psycopg2://postgres:admin@192.168.99.100:5432/queensBenchmark"

db = create_engine(dbString)

base = declarative_base()


class QueensPositionRegister(base):
    __tablename__ = "queens"

    queenId = Column(Integer, primary_key=True)
    benchmarkId = Column(Integer)
    solution = Column(Integer)
    row = Column(Integer)
    column = Column(Integer)
    columnChar = Column(String)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)


class QueensPositionRepository:

    def add(self, queensSolutions):
        i = 1
        for solution in queensSolutions:

            for queen in solution:
                queenRegister = QueensPositionRegister(
                    benchmarkId=0, solution=i, row=queen.position.row, column=queen.position.column, columnChar="A")
                session.add(queenRegister)
            
            i += 1

        session.commit()
