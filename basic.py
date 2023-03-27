from flask import Flask, render_template, request
from flask import request

# creating application object as instance of the class Class imported from Flask package of first line
#__name__ use location that is passed in
app = Flask(__name__)

# @app.route --define index of funct
@app.route('/')
def index():
    return render_template('front/index.html')

#test
@app.route('/signup_form')
def signup_form():
    return render_template('front/signup_form.html')


@app.route('/thankyou')
def thank_you():
    first = request.args.get('first')  # grab info that is sent from the form
    last = request.args.get('last')
    return render_template('front/thank_you.html', first_name=first,
                           last_name=last)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('front/404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
