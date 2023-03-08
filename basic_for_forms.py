from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
# key build in flask application
app.config['SECRET_KEY'] = 'mysecretkey'


# instance of wtfForm class
# inherits from FLaskForm
#
class InfoForm(FlaskForm):
    # attributes to send back to template
    breed = StringField("What breed are you?")
    submit = SubmitField('Submit')


# view funcction allow passing this form to template
@app.route('/', methods=['GET', 'POST'])
def index():
    breed = False
    # create instance of Form
    form = InfoForm()


    if form.validate_on_submit():
        # grab data from (form.<attribute_you_want>.data
        breed = form.breed.data
        form.breed.data = '' #I dont wnat to see smth in form
    return render_template('forms/index.html', form=form, breed=breed)


if __name__ == '__main__':
    app.run(debug=True)
