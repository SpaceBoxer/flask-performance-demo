from flask import Flask
from flask_performance import PerformanceCollector


def create_app():

    app = Flask(__name__)
    app.config['METRIC_DSN'] = 'https://metrics.spacebox.fun/v1/collector/c5b35bc078844a59a15dd506e08f3ae6'
    pc = PerformanceCollector(app)
    
    return app


app = create_app()

from .views import users
