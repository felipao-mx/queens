import argparse
from strategies.implementations.recursiveresolver import RecursiveResolver
from repositories.benchmarkrepository import BenchmarkRepository
from repositories.queensrepository import QueensPositionRepository
from repositories.tableinit import Session
from benchmarkservice import BenchmarkService

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--rows", help="rows")
parser.add_argument("-c", "--cols", help="columns")

arguments = parser.parse_args()

if arguments.rows is None or arguments.cols is None:
    print("Setting default rows and columns: 8x8, 8 queens")
    arguments.rows = 8
    arguments.cols = 8

print("rows: " + str(arguments.rows))
print("columns: " + str(arguments.cols))

session = Session()
benchmarkService = BenchmarkService(RecursiveResolver(), BenchmarkRepository(session), QueensPositionRepository(session))

benchmarkService.singleSolution(int(arguments.rows))