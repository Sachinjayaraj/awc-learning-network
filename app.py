from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/user/<name>')
def hello_user(name):
    return f'Hello, {name}!'


if __name__ == '__main__':
    app.run(debug=True)
