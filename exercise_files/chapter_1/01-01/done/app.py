from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# decorator
@app.route('/boris/')
def boris():
    return jsonify(message='I am fonyuy boris lami')

if __name__ == '__main__':
    app.run()
