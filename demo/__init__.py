from flask import Flask
from flask_performance import PerfomanceCollector



def create_app():

    app = Flask(__name__)
    pc = PerfomanceCollector(app)

    return app


app = create_app()

