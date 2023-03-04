from flask import Flask

app = Flask(__name__)

app.debug = True

@app.route('/')
def hello_world():  # put application's code here
    return "<h1>Hello World!</h1>"

@app.route('/information')
def info():  # put application's code here
    return "<h1>Cats are cute!</h1>"

@app.route('/some_page/<name>')
def other_page(name):  # put application's code here
    return 'User: {}'.format(name)

#dynamic route
@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>This is a page for {}</h1>".format(name.upper())

@app.route('/puppy100/<name>')
def puppy100(name):
    return "100th letter for {}".format(name[30])

#task
# 1. not end in y and y
# 2. end in y then ad iful
@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    if not name.endswith("y"):
        return 'Hi {}! Your latin name is {}'.format(name,name+'y')
    else:
        return 'Hi {}! Your latin name is {}'.format(name,name[:-1]+'iful')


if __name__ == '__main__':
    app.run(debug=True)
