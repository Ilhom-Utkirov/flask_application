from flask import Flask, render_template, request
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('task1_name_check/index.html')


@app.route('/report')
def report():
    #### official solution
    lower_letter = False
    upper_letter = False
    num_end = False

    username = request.args.get('name')
    lower_letter = any(c.islower() for c in username)
    upper_letter = any(c.isupper() for c in username)
    num_end = username[-1].isdigit()

    status = lower_letter and upper_letter and num_end
    return render_template("task1_name_check/report.html", status=status, lower_letter=lower_letter,
                           upper_letter=upper_letter, num_end=num_end)

    """
    #this is my way 
    
    status = False
    name = request.args.get('name')  # grab info that is sent from the form
    error_code = []
    if not name[-1].isdigit():
        status = True
        error_code.append("you didnot end ur username with number")
    if name.islower() or name.isdigit():
        status = True
        error_code.append("You should use an uppercase letters")
    if name.isupper() or name.isdigit():
        status = True
        error_code.append("Ypu should use lowercase letters")

    return render_template('task1_name_check/report.html', status=status,
                           name=name, error_code=error_code)
    """


@app.errorhandler(404)
def page_not_found2(e):
    return render_template('front/404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
