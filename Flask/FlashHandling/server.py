from flask import Flask, render_template, redirect, request, flash 
app = Flask(__name__)
app.secret_key = "Blah"
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=["POST"])
def process():
    # validate!
    errors = False
    if (len(request.form['first_name']) == 0):
        errors = True
        flash('First Name cannot be blank')
       
    if (len(request.form['email']) == 0):
        errors = True
        flash('Email cannot be blank')
    elif not (EMAIL_REGEX.match(request.form['email'])):
        errors = True 
        flash('Email must be valid')
        
    if errors:
        return redirect('/')
    else:
        print request.form

app.run(debug=True)