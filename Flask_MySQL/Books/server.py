from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'books')

@app.route('/')
def index():
    query = 'SELECT * FROM books'
    books = mysql.query_db(query)
    print books
    return render_template('index.html', books=books)

@app.route('/add')
def add_book_on_your_face():
    return render_template('new.html')

@app.route('/create', methods=["POST"])
def create():
    print request.form
    # form data is in our hands. let's jam it
    query = 'INSERT INTO books (title, author, created_at, updated_at) VALUES (:title, :author, now(), now())'
    data = {
        'title': request.form['title'],
        'author': request.form['author']
    }
    mysql.query_db(query, data)

    return redirect('/')

@app.route('/destroy/<id>')
def destroy(id):
    # load the template to confirm delete
    print id
    query = 'SELECT * FROM books WHERE id = :id'
    data = {
        'id': id
    }
    books = mysql.query_db(query, data) # [{}]
    return render_template('destroy.html', book=books[0])

@app.route('/demolish/<id>')
def demolish(id):
    query = 'DELETE FROM books WHERE id = :id'
    data = {
        'id': id
    }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)