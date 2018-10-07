from models.benchmark import Benchmark
from utilities.columnutilities import numToString
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

        databaseTime = datetime.datetime.now()

        self.benchmarkRepository.add(benchmark)
        self.queensRepository.add(results, benchmark.id)

        solution_runtime = benchmark.endDate - benchmark.startDate
        database_runtime = datetime.datetime.now() - databaseTime

        queensSolutions = self.toDictionary(results)

        info = {
            'queens': queensCount,
            'solutions_count': len(results),
            'solution_runtime': str(solution_runtime),
            'database_runtime': str(database_runtime),
            'solutions': queensSolutions
        }
        
        return info

    def manySolutions(self, first, last):
        for i in range(first, last + 1):
            self.singleSolution(i)

    def toDictionary(self, results):
        elements = []
        i = 1

        for result in results:
            r = {
                'solution': i,
                'queens': []
            }
            for queen in result:
                q = {
                    'row': queen.position.row,
                    'col': queen.position.column,
                    'colChar': numToString(queen.position.column)
                }

                r['queens'].append(q)

            elements.append(r)
            i += 1
        
        return elements
