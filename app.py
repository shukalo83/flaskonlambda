from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello World!"})

@app.route('/hello')
def another_hello():
    return jsonify({"message": "pozdrav"})

if __name__ == '__main__':
 app.run()
