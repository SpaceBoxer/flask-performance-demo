
from flask import jsonify
from demo import app


@app.route('/users/')
def users():
    users = {
        "Zack Mark": {
            "age": 25,
            "address": "New York",
            "gender": 'male'
        },
        "Lily": {
            "age": 30,
            "address": "Silicon Valley",
            "gender": 'female'
        }
    }

    return jsonify(users)
