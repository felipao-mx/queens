from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime, Interval, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

user = os.environ['POSTGRES_USER']
pwd = os.environ['POSTGRES_PASSWORD']
db = os.environ['POSTGRES_DB']
host = os.environ['DB_HOST']
port = os.environ['DB_PORT']

dbString = 'postgresql+psycopg2://%s:%s@%s:%s/%s' % (user, pwd, host, port, db)
print("connection string: " + dbString)
db = create_engine(dbString)

base = declarative_base()

class BenchmarkRegister(base):
    __tablename__ = "benchmark"

    benchmarkId = Column(Integer, primary_key=True)
    name = Column(String)
    start = Column(DateTime, default=func.now())
    end = Column(DateTime)


class QueensPositionRegister(base):
    __tablename__ = "queens"

    queenId = Column(Integer, primary_key=True)
    benchmarkId = Column(Integer)
    solution = Column(Integer)
    row = Column(Integer)
    column = Column(Integer)
    columnChar = Column(String)


Session = sessionmaker(db)
base.metadata.create_all(db)