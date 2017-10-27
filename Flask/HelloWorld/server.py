from flask import Flask, render_template, request 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/account')
def account():
    return render_template('account.html')

app.run(debug=True)