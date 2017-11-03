from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = "secret_sauce"
mysql = MySQLConnector(app, 'email_validation')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=["POST"])
def create():
    errors = False
    if len(request.form['email']) == 0:
        flash('Email is required')
        errors = True 
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email')
        errors = True 
    if errors:
        return redirect('/')

    query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
    data = {
        'email': request.form['email']
    }

    mysql.query_db(query, data)

    return redirect('/success')

@app.route('/success')
def success():
    emails = mysql.query_db('SELECT * FROM emails')
    last_email = emails[-1]['email']
    return render_template('success.html', emails=emails, last_email=last_email) 



app.run(debug=True)