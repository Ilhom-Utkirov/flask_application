from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

#instance of wtfForm class
# inherits from FLaskForm
class InfoForm(FlaskForm):

    breed = StringField("What breed are you?")
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    breed = False
    #create instance of Form
    form = InfoForm()

    if form.validate_on_submit():
        #grab data from form
        breed = form.breed.data
        form.breed.data = ''
    return render_template('forms/home.html', form=form, breed=breed)


if __name__ == '__main__':
    app.run(debug=True)
