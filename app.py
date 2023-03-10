from flask import Flask, render_template

app = Flask(__name__)

app.debug = True


# @app.route('/')
# def hello_world():  # put application's code here
#     return "<h1>Hello World!</h1>"
@app.route('/')
def index2():
    return render_template('basic.html')


@app.route('/render')
def index3():
    name = "JoseAlonso"
    letter = list(name)
    pup_dictionary = {'pup_name': 'Ssammy'}
    return render_template('basic2.html', name=name, letters=letter,
                           pup_dictionary=pup_dictionary)
@app.route('/render2')
def index4():
    #code
    user_logged_in =True

    puppies = ['reks', 'linda', 'sharik']
    pup_dictionary = {'pup_name': 'Ssammy'}
    return render_template('basic3.html', puppies=puppies)
@app.route('/login')
def login():
    #code
    user_logged_in =False
    return render_template('login.html', user_logged_in=user_logged_in)


@app.route('/information')
def info():  # put application's code here
    return "<h1>Cats are cute!</h1>"


@app.route('/some_page/<name>')
def other_page(name):  # put application's code here
    return 'User: {}'.format(name)


# dynamic route
@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>This is a page for {}</h1>".format(name.upper())


@app.route('/puppy100/<name>')
def puppy100(name):
    return "100th letter for {}".format(name[30])


# task
# 1. not end in y and y
# 2. end in y then ad iful
@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    if not name.endswith("y"):
        return 'Hi {}! Your latin name is {}'.format(name, name + 'y')
    else:
        return 'Hi {}! Your latin name is {}'.format(name, name[:-1] + 'iful')
#===================================================================================================================================
# template inheritence

@app.route('/home')
def root():
    return render_template('home.html')

@app.route('/puppys/<name>')
def pup_name(name):
    return render_template('puppy.html', name=name)




if __name__ == '__main__':
    app.run(debug=True)
