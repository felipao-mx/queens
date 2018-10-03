from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime, Interval, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

dbString = "postgresql+psycopg2://postgres:admin@192.168.99.100:5432/queensBenchmark"

db = create_engine(dbString)

base = declarative_base()


class BenchmarkRegister(base):
    __tablename__ = "benchmark"

    benchmarkId = Column(Integer, primary_key=True)
    name = Column(String)
    start = Column(DateTime, default=func.now())
    end = Column(DateTime)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

# benchmark = BenchmarkRegister(benchmarkId = 23, name = "test")
# session.add(benchmark)
# session.commit()

# benchmarks = session.query(benchmark)

# for b in benchmarks:
#     print(benchmark.benchmarkId)


class BenchmarkRepository:
    def add(self, benchmark):
        register = BenchmarkRegister(
            name=benchmark.name, start=benchmark.startDate, end=benchmark.endDate)
        session.add(register)
        session.commit()
