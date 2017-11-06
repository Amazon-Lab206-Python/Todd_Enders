from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "secret_sauce"
mysql = MySQLConnector(app, 'the_wall')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=["POST"])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    c_password = request.form['c_password']
    
    errors = False
    if len(first_name) == 0:
        flash('First Name is required')
        errors = True
    elif not first_name.isalpha():
        flash('First Name can only contain letters')
        errors = True 
    if len(last_name) == 0:
        flash('Last Name is required')
        errors = True
    elif not last_name.isalpha():
        flash('Last Name can only contain letters')
        errors = True 
    if len(email) == 0:
        flash('Email is required')
        errors = True 
    elif not EMAIL_REGEX.match(email):
        flash('Invalid Email')
        errors = True 
    if len(password) == 0:
        flash('Password is required')
        errors = True 
    elif len(password) < 8:
        flash('Password must be at least 8 characters')
        errors = True
    if len(c_password) == 0:
        flash('Password Confirmation is required')
        errors = True 
    elif password != c_password:
        flash('Passwords must match')
        errors = True
    if errors:
        return redirect('/')
    
    # See if there's an existing email
    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data = {
        'email': email
    }
    users = mysql.query_db(query, data) 
    if len(users) > 0:
        flash('Email already taken')
        return redirect('/')

    query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first, :last, :email, :password, NOW(), NOW())"
    data = {
        'first': first_name,
        'last': last_name,
        'email': email,
        'password': bcrypt.generate_password_hash(password)
    }

    user_id = mysql.query_db(query, data)
    session['user_id'] = user_id
    session['first_name'] = first_name.capitalize()
    
    return redirect('/wall')

@app.route('/login', methods=["POST"])
def login():
    email = request.form['email']
    password = request.form['password']

    #Check users table for existing user with that email
    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data = {
        'email': email 
    }
    users = mysql.query_db(query,data)
    if len(users) > 0:
        user = users[0]
        if bcrypt.check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['first_name'] = user['first_name'].capitalize()
            return redirect('/wall')
        else:
            flash('Invalid Email/Password Combination')
            return redirect('/')
    else:
        flash('Invalid Email/Password Combination')
        return redirect('/')

@app.route('/wall')
def success():
    messages_query = 'SELECT messages.id, messages.message, messages.created_at, users.first_name, users.last_name FROM messages JOIN users ON messages.user_id = users.id ORDER BY messages.created_at DESC'
    comments_query = 'SELECT comments.*, users.first_name, users.last_name FROM comments JOIN users ON comments.user_id = users.id ORDER BY comments.created_at ASC'
    messages = mysql.query_db(messages_query)
    comments = mysql.query_db(comments_query)

    return render_template('wall.html', messages=messages, comments=comments)

@app.route('/messages/create', methods=["POST"])
def create_message():
    query = 'INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())'
    data = {
        'user_id': session['user_id'],
        'message': request.form['message']
    }
    mysql.query_db(query, data) 

    return redirect('/wall')

@app.route('/comments/create', methods=["POST"])
def create_comment():
    query = 'INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES (:user_id, :message_id, :comment, NOW(), NOW())'
    data = {
        'user_id': session['user_id'],
        'message_id': request.form['message_id'],
        'comment': request.form['comment']
    }
    mysql.query_db(query, data) 

    return redirect('/wall')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)