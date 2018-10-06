from .tableinit import BenchmarkRegister

class BenchmarkRepository:

    def __init__(self, session):
        self.session = session

    def add(self, benchmark):
        register = BenchmarkRegister(
            name=benchmark.name, start=benchmark.startDate, end=benchmark.endDate)
        self.session.add(register)
        self.session.commit()
