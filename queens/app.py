import argparse
import sys
from strategies.implementations.recursiveresolver import RecursiveResolver


print(sys.path)

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--rows", help="rows")
parser.add_argument("-c", "--cols", help="columns")
parser.add_argument("-q", "--queens", help="queens")

arguments = parser.parse_args()

if arguments.rows is None or arguments.cols is None:
    print("Setting default rows and columns: 8x8")
    arguments.rows = 8
    arguments.cols = 8

if arguments.queens is None:
    print("Settings default queens: 8")
    arguments.queens = 8

print("rows: " + str(arguments.rows))
print("columns: " + str(arguments.cols))
print("queens: " + str(arguments.queens))

resolver = RecursiveResolver()
resolver.resolve(arguments.rows, arguments.cols, 1, [])
print("Solutions found: " + str(len(resolver.solutions)))