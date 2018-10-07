import flask
from flask import request, jsonify
from strategies.implementations.recursiveresolver import RecursiveResolver
from repositories.benchmarkrepository import BenchmarkRepository
from repositories.queensrepository import QueensPositionRepository
from repositories.tableinit import Session
from benchmarkservice import BenchmarkService

app = flask.Flask(__name__)
# app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''
    <h1> Queens resolver</h1>
    '''


@app.errorhandler(404)
def page_not_found(enumerate):
    return "<h1>404 :(</h1><p> The resource could not be found.</p>", 404


@app.route('/queens/<queensCount>/solutions')
def resolve(queensCount):
    session = Session()
    benchmarkService = BenchmarkService(RecursiveResolver(), BenchmarkRepository(
        session), QueensPositionRepository(session))
    return jsonify(benchmarkService.singleSolution(int(queensCount)))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
