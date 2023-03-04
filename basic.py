from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Go to /puppy_name/name and see the results!</h1>"

@app.route('/puppy_name/<name>')
def puppy_latin(name):
    return "<h1>Go to /puppy_name/name and see the results!</h1>"


# if __name__ == '__main__':
#     app.run()