from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime, Interval, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

user = os.environ['POSTGRES_USER']
pwd = os.environ['POSTGRES_PASSWORD']
db = os.environ['POSTGRES_DB']
host = 'postgresdb'
port = '5432'

# dbString = "postgresql+psycopg2://queens:queens@192.168.99.100:5432/queensdb"
dbString = 'postgresql+psycopg2://%s:%s@%s:%s/%s' % (user, pwd, host, port, db)
print("connection string: " + dbString)

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
