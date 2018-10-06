from models.benchmark import Benchmark
import datetime

class BenchmarkService:
    def __init__(self, queensResolver, benchmarkRepository, queensRepository):
        self.benchmarkRepository = benchmarkRepository
        self.queensResolver = queensResolver
        self.queensRepository = queensRepository

    def singleSolution(self, queensCount):
        benchmark = Benchmark()
        benchmark.startDate = datetime.datetime.now()
        benchmark.name = "test " + str(queensCount) + str(benchmark.startDate)

        results = self.queensResolver.resolve(queensCount, queensCount)
        
        benchmark.endDate = datetime.datetime.now()

        self.benchmarkRepository.add(benchmark)
        self.queensRepository.add(results, benchmark.id)


    def manySolutions(self, first, last):
        for i in range(first, last + 1):
            self.singleSolution(i)