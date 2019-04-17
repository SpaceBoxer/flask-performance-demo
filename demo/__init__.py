from flask import Flask
from flask_performance import PerfomanceCollector



def create_app():

    app = Flask(__name__)
    pc = PerfomanceCollector(app)
    app.config['METRIC_DSN'] = 'https://metrics.spacebox.fun/v1/collector/c5b35bc078844a59a15dd506e08f3ae6'

    return app


app = create_app()

