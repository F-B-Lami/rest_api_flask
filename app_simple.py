from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# simple
@app.route('/boris/')
def boris():
    return jsonify(message='I am fonyuy boris lami')


# not found
@app.route('/not_found')
def not_found():
    return jsonify(message='That resource was not found'), 404


# parameters
@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message='Sorry ' + name + ', you are not old enough.'), 401
    else:
        return jsonify(message='Welcome ' + name + ', you are old enough!')


# url_variables
@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
    if age < 18:
        return jsonify(message='Sorry ' + name + ', you are not old enough.'), 401
    else:
        return jsonify(message='Welcome ' + name + ', you are old enough!')


if __name__ == '__main__':
    app.run()
