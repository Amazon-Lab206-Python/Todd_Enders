from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'users')

@app.route('/users')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', users=users)

@app.route('/users/new')
def new():
    return render_template('new.html')

@app.route('/users/create', methods=["POST"])
def create():
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first, :last, :email, NOW(), NOW())"
    data = {
        'first': request.form['first_name'],
        'last': request.form['last_name'],
        'email': request.form['email']
    }

    last_user_id = mysql.query_db(query, data)
    return redirect('/users/'+str(last_user_id))

@app.route('/users/<id>')
def show(id):
    query = "SELECT * FROM users WHERE id = :id"
    data = {
        'id': id
    }
    user = mysql.query_db(query, data) # list, remember?
    return render_template('show.html', user=user[0])

@app.route('/users/<id>/edit')
def edit(id):
    query = "SELECT * FROM users WHERE id = :id"
    data = {
        'id': id
    }
    user = mysql.query_db(query, data) # list, remember?
    return render_template('edit.html', user=user[0])

@app.route('/users/<id>', methods=["POST"])
def update(id):
    query = "UPDATE users SET first_name = :first, last_name = :last, email = :email, updated_at = NOW() WHERE id = :id"
    data = {
        'first': request.form['first_name'],
        'last': request.form['last_name'],
        'email': request.form['email'],
        'id': id
    }
    mysql.query_db(query, data)
    return redirect('/users/'+id)

@app.route('/users/<id>/destroy')
def destroy(id):
    query = "DELETE FROM users WHERE id = :id"
    data = {
        'id': id
    }
    mysql.query_db(query,data) 
    return redirect('/users')

app.run(debug=True)
