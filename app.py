from flask import Flask, render_template, request
from flask import request

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('base/basic.html')


@app.route('/info')
def info():  # put application's code here
    return "<h1>Cute Puppy</h1>"


@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>page for {} </h1>".format(name)


@app.route('/puppy_upper/<name>')
def puppy_upper(name):
    return "<h1>upper {} </h1>".format(name.upper())


@app.route('/puppy_2nd_letter/<name>')
def puppy_2nd_letter(name):
    return "<h1>2nd letter {} </h1>".format(name[2])


@app.route('/puppy_name_latin/<name>')
def puppylatin(name):
    puppyname = ''

    if name[-1] == 'y':
        puppyname = name[:-1] + 'iful'
    else:
        puppyname = name + 'y'
    return "<h1> pupy name = {}".format(puppyname)


if __name__ == '__main__':
    app.run(debug=True)
